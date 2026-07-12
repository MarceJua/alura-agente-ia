from datetime import datetime, timezone
import json
from pathlib import Path
import sys
from time import perf_counter

from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_cohere import ChatCohere, CohereEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain


PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))


CHROMA_DIR = PROJECT_ROOT / "chroma_db"
LOGS_DIR = PROJECT_ROOT / "logs"
LOG_FILE = LOGS_DIR / "agent_execution.jsonl"
COLLECTION_NAME = "clinic_policies"
MODEL_NAME = "command-r-plus-08-2024"


def build_vector_store() -> Chroma:
	load_dotenv()
	embeddings = CohereEmbeddings(model="embed-multilingual-v3.0")
	return Chroma(
		collection_name=COLLECTION_NAME,
		persist_directory=str(CHROMA_DIR),
		embedding_function=embeddings,
	)


def build_rag_chain(vector_store: Chroma):
	llm = ChatCohere(model=MODEL_NAME, temperature=0)
	prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            (
                "Eres 'Sani', el asistente corporativo experto de la Clínica Sanitas Innova.\n"
                "Tu objetivo es responder a la pregunta del usuario basándote ÚNICAMENTE en el siguiente contexto.\n\n"
                "Contexto:\n{context}\n\n"
                "Reglas estrictas:\n"
                "- Si el usuario te saluda (ej. 'Hola', 'Buenos días', 'Buenas tardes'), preséntate amigablemente como Sani e indica que estás aquí para ayudar a resolver dudas sobre las políticas y protocolos de la clínica.\n"
                "- Para cualquier otra consulta, lee cuidadosamente todo el contexto proporcionado, prestando especial atención a los datos dentro de las tablas.\n"
                "- Si la información para responder está en el contexto, redacta una respuesta clara y directa.\n"
                "- Si el contexto NO contiene la información necesaria para responder, tu respuesta obligatoria debe ser exactamente: 'No encontré esta información en los documentos disponibles'.\n"
                "- No utilices conocimiento externo bajo ninguna circunstancia."
            ),
        ),
        ("human", "{input}"),
    ]
)
	question_answer_chain = create_stuff_documents_chain(llm, prompt)
	retriever = vector_store.as_retriever(search_kwargs={"k": 3})
	return create_retrieval_chain(retriever, question_answer_chain), retriever


def format_sources(documents) -> list[dict[str, str]]:
	sources = []
	for document in documents:
		sources.append(
			{
				"content": document.page_content,
				"metadata": document.metadata,
			}
		)
	return sources


def append_log(question: str, answer: str, sources: list[dict[str, str]], latency_seconds: float) -> None:
	LOGS_DIR.mkdir(parents=True, exist_ok=True)
	log_entry = {
		"pregunta": question,
		"respuesta": answer,
		"fuentes": sources,
		"latencia_segundos": round(latency_seconds, 4),
		"timestamp": datetime.now(timezone.utc).isoformat(),
	}
	with LOG_FILE.open("a", encoding="utf-8") as log_handle:
		log_handle.write(json.dumps(log_entry, ensure_ascii=False) + "\n")


def ask_agent(question: str, rag_chain, retriever) -> str:
	start_time = perf_counter()
	retrieved_documents = retriever.invoke(question)
	response = rag_chain.invoke({"input": question})
	latency_seconds = perf_counter() - start_time
	answer = response["answer"]
	sources = format_sources(retrieved_documents)
	append_log(question, answer, sources, latency_seconds)

	print(f"\nRespuesta:\n{answer}")
	print(f"\nLatencia: {latency_seconds:.2f} segundos")
	if sources:
		print("\nFuentes recuperadas:")
		for index, source in enumerate(sources, start=1):
			print(f"  Fuente {index}: {source['metadata']}")

	return answer


def main() -> None:
	vector_store = build_vector_store()
	rag_chain, retriever = build_rag_chain(vector_store)

	print("Agente listo. Escribe tu pregunta o 'salir' para terminar.")

	while True:
		question = input("\nPregunta: ").strip()
		if not question:
			continue

		if question.lower() == "salir":
			print("Saliendo del agente.")
			break

		ask_agent(question, rag_chain, retriever)


if __name__ == "__main__":
	main()

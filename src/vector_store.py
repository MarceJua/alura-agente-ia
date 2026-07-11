from pathlib import Path
from typing import Sequence
import sys

from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_cohere import CohereEmbeddings

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

from src.document_loader import load_markdown_document, split_markdown_by_headers


SOURCE_FILE = PROJECT_ROOT / "data" / "politicas-clinica.md"
CHROMA_DIR = PROJECT_ROOT / "chroma_db"
COLLECTION_NAME = "clinic_policies"
TEST_QUERY = "¿Cuánto tiempo se guardan las fichas en papel?"


def build_embeddings() -> CohereEmbeddings:
	load_dotenv()

	return CohereEmbeddings(model="embed-multilingual-v3.0")


def build_vector_store(chunks: Sequence, embeddings: CohereEmbeddings) -> Chroma:
	return Chroma.from_documents(
		documents=list(chunks),
		embedding=embeddings,
		collection_name=COLLECTION_NAME,
		persist_directory=str(CHROMA_DIR),
	)


def print_best_match(query: str, vector_store: Chroma) -> None:
	results = vector_store.similarity_search(query, k=1)

	print(f"\nConsulta de prueba: {query}")

	if not results:
		print("No se encontró ningún chunk relevante.")
		return

	best_match = results[0]
	print("\nChunk más relevante encontrado:")

	if best_match.metadata:
		print("Headers:")
		for header_name in ("H1", "H2", "H3"):
			if header_name in best_match.metadata:
				print(f"  {header_name}: {best_match.metadata[header_name]}")

	print("Content:")
	print(best_match.page_content.strip())


def main() -> None:
	document_text = load_markdown_document(SOURCE_FILE)
	chunks = split_markdown_by_headers(document_text)

	embeddings = build_embeddings()
	vector_store = build_vector_store(chunks, embeddings)

	print(f"Base vectorial persistente creada en: {CHROMA_DIR}")
	print(f"Chunks indexados: {len(chunks)}")

	print_best_match(TEST_QUERY, vector_store)


if __name__ == "__main__":
	main()

from html import escape
from time import perf_counter

import streamlit as st

from src.agent import append_log, build_rag_chain, build_vector_store, format_sources


def apply_styles() -> None:
	st.markdown(
		"""
		<style>
			/* Fondo general clínico suave */
			.stApp,
			[data-testid="stAppViewContainer"],
			.main,
			.block-container {
				background: #F8FAFC;
			}

			/* Encabezado superior */
			[data-testid="stHeader"] {
				background: rgba(248, 250, 252, 0.85);
			}

			/* Títulos y etiquetas en Azul Zafiro */
			h1, h2, h3, h4, h5, h6,
			label {
				color: #0F52BA !important;
				font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
			}

			/* Texto general en Azul Pizarra Oscuro */
			.stMarkdown,
			.stText,
			p, li, span, div {
				color: #1E293B;
			}

			/* Enlaces en Azul Cielo Digital */
			[data-testid="stAppViewContainer"] a {
				color: #4A90E2;
			}

			/* Botón Principal (Azul Zafiro) */
			.stButton > button {
				background: linear-gradient(135deg, #0F52BA 0%, #3B82F6 100%);
				color: #FFFFFF;
				border: none;
				font-weight: 600;
				border-radius: 8px;
			}

			/* Botón Hover (Azul Cielo) */
			.stButton > button:hover {
				background: linear-gradient(135deg, #4A90E2 0%, #0F52BA 100%);
				color: #FFFFFF;
			}

			/* Caja de Entrada del Chat (Input) */
			[data-testid="stChatInput"] textarea {
				background: #FFFFFF;
				color: #1E293B;
				border: 1px solid #4A90E2;
			}

			/* Placeholder del Chat */
			[data-testid="stChatInput"] textarea::placeholder {
				color: #64748B;
			}

			/* Burbuja del Usuario (Azul Zafiro Institucional) */
			.user-bubble {
				background: linear-gradient(135deg, #0F52BA 0%, #4A90E2 100%);
				color: #FFFFFF;
				padding: 1rem 1.1rem;
				border-radius: 1rem;
				border: none;
				white-space: pre-wrap;
			}
			
			/* Asegura que el texto dentro de la burbuja de usuario sea blanco */
			.user-bubble p, .user-bubble span, .user-bubble div {
				color: #FFFFFF !important;
			}

			/* Burbuja del Asistente (Blanca Limpia con borde suave) */
			.assistant-bubble {
				background: #FFFFFF;
				color: #1E293B;
				padding: 1rem 1.1rem;
				border-radius: 1rem;
				border: 1px solid #E2E8F0;
				box-shadow: 0 4px 12px rgba(15, 82, 186, 0.05);
				white-space: pre-wrap;
			}

			/* Metadatos y subtítulos (Gris Medio) */
			.assistant-meta,
			.stCaption {
				color: #64748B;
			}
		</style>
		""",
		unsafe_allow_html=True,
	)


@st.cache_resource
def get_vector_store():
	return build_vector_store()


@st.cache_resource
def get_rag_resources():
	vector_store = get_vector_store()
	return build_rag_chain(vector_store)


def initialize_session_state() -> None:
	if "messages" not in st.session_state:
		st.session_state.messages = []


def render_message(role: str, content: str) -> None:
	with st.chat_message(role):
		bubble_class = "user-bubble" if role == "user" else "assistant-bubble"
		st.markdown(
			f'<div class="{bubble_class}">{escape(content).replace(chr(10), "<br>")}</div>',
			unsafe_allow_html=True,
		)


def run_question(question: str, rag_chain, retriever) -> None:
	start_time = perf_counter()
	retrieved_documents = retriever.invoke(question)
	response = rag_chain.invoke({"input": question})
	latency_seconds = perf_counter() - start_time
	answer = response["answer"]
	sources = format_sources(retrieved_documents)
	append_log(question, answer, sources, latency_seconds)

	st.session_state.messages.append({"role": "assistant", "content": answer})

	render_message("assistant", answer)

	if sources:
		with st.expander("Fuentes recuperadas"):
			for index, source in enumerate(sources, start=1):
				st.markdown(
					f"**Fuente {index}**\n\n"
					f"- Metadata: {source['metadata']}\n\n"
					f"- Fragmento: {source['content']}",
				)

	st.caption(f"Latencia: {latency_seconds:.2f} segundos")


def main() -> None:
	st.set_page_config(page_title="Sanitas Innova AI")
	apply_styles()
	initialize_session_state()

	st.title("Sanitas Innova AI")
	st.write("Consulta la base de conocimiento clínica con respuestas estrictamente basadas en contexto.")

	rag_chain, retriever = get_rag_resources()

	for message in st.session_state.messages:
		render_message(message["role"], message["content"])

	if user_question := st.chat_input("Escribe tu pregunta"):
		st.session_state.messages.append({"role": "user", "content": user_question})
		render_message("user", user_question)
		run_question(user_question, rag_chain, retriever)


if __name__ == "__main__":
	main()

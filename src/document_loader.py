from pathlib import Path

from langchain_text_splitters import MarkdownHeaderTextSplitter


PROJECT_ROOT = Path(__file__).resolve().parent.parent
SOURCE_FILE = PROJECT_ROOT / "data" / "politicas-clinica.md"


def load_markdown_document(file_path: Path) -> str:
	if not file_path.exists():
		raise FileNotFoundError(f"No se encontró el archivo fuente: {file_path}")

	return file_path.read_text(encoding="utf-8")


def split_markdown_by_headers(markdown_text: str):
	headers_to_split_on = [
		("#", "H1"),
		("##", "H2"),
		("###", "H3"),
	]

	splitter = MarkdownHeaderTextSplitter(
		headers_to_split_on=headers_to_split_on,
		strip_headers=False,
	)
	return splitter.split_text(markdown_text)


def print_chunks(chunks) -> None:
	for index, chunk in enumerate(chunks, start=1):
		print(f"\n=== Chunk {index} ===")

		metadata = chunk.metadata or {}
		if metadata:
			print("Headers:")
			for header_name in ("H1", "H2", "H3"):
				if header_name in metadata:
					print(f"  {header_name}: {metadata[header_name]}")
		else:
			print("Headers: (sin metadatos)")

		print("Content:")
		print(chunk.page_content.strip())


def main() -> None:
	markdown_text = load_markdown_document(SOURCE_FILE)
	chunks = split_markdown_by_headers(markdown_text)
	print_chunks(chunks)


if __name__ == "__main__":
	main()

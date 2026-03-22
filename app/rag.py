import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

from conf import conf


embedding = HuggingFaceEmbeddings()

def load_documents():
    documents = []

    for root, _, files in os.walk(conf.DATA_PATH    ):
        for file in files:
            if file.endswith(".txt"):
                loader = TextLoader(os.path.join(root, file))
                documents.extend(loader.load())

    return documents


def create_db():
    print("🔄 Creating new vector DB...")

    documents = load_documents()

    splitter = CharacterTextSplitter(chunk_size=300, chunk_overlap=50)
    docs = splitter.split_documents(documents)

    db = Chroma.from_documents(
        docs,
        embedding,
        persist_directory=conf.DB_PATH
    )

    db.persist()
    return db


def load_db():
    if os.path.exists(conf.DB_PATH):
        print("✅ Loading existing DB...")
        return Chroma(
            persist_directory=conf.DB_PATH,
            embedding_function=embedding
        )
    else:
        return create_db()


db = load_db()

def get_context(query):
    results = db.similarity_search(query, k=3)
    context = "\n".join([r.page_content for r in results])
    return context
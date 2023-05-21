import os

from flask import g
from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader


def build_index(room):
    index_path = f"data/index_{room}.json"

    documents = SimpleDirectoryReader(f"data/{room}").load_data()
    index = GPTSimpleVectorIndex.from_documents(documents)
    index.save_to_disk(index_path)

    return index


def load_index(room):
    index_path = f"data/index_{room}.json"
    if os.path.exists(index_path):
        index = GPTSimpleVectorIndex.load_from_disk(index_path)
    else:
        index = build_index(room)
    return index


def get_index(room):
    if "index" not in g:
        g.index = load_index(room)
    return g.index

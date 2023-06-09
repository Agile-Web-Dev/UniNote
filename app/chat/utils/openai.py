import os

from llama_index import (
    Document,
    GPTVectorStoreIndex,
    StorageContext,
    load_index_from_storage,
)


class OpenAI:
    """
    OpenAI class to handle all ChatGPT functions
    """

    def __init__(self):
        self.indices = {}

    def add_document(self, room, context):
        """
        adding context to chatGPT index based on room
        """
        index_path = f"data/index/{room}"

        index = self.get_index(room)
        doc = Document(context)
        index.insert(doc)

        self.indices["room"] = index
        index.storage_context.persist(persist_dir=index_path)

    def build_index(self, room):
        """
        build index for chatGPT based on the room
        """
        index_path = f"data/index/{room}"
        initial_context = "Initial Context"
        doc = Document(initial_context)

        index = GPTVectorStoreIndex([])
        index.insert(doc)
        index.storage_context.persist(persist_dir=index_path)

        return index

    def load_index(self, room):
        """
        loading the chatGPT index based on the room
        """
        print("read")
        index_path = f"data/index/{room}"
        if os.path.exists(index_path + "/docstore.json"):
            storage_context = StorageContext.from_defaults(persist_dir=index_path)
            index = load_index_from_storage(storage_context)
            return index

        index = self.build_index(room)
        return index

    def get_index(self, room):
        """
        fetch the index based on the room
        """
        if room not in self.indices:
            self.indices["room"] = self.load_index(room)
        return self.indices["room"]


openai = OpenAI()

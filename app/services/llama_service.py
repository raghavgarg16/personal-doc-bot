""" LlamaIndex Service File... """

# Python Packages
import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.settings import Settings
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding

# Constants
from base import constants





# Define Variable
query_engine = None

def init_llama():
    """
    Initialize LlamaIndex once at application startup
    """

    global query_engine

    # Configure OpenAI
    Settings.llm = OpenAI(api_key = constants.OPENAI_API_KEY)
    Settings.embed_model = OpenAIEmbedding(api_key = constants.OPENAI_API_KEY)

    # Load documents
    documents = SimpleDirectoryReader("data").load_data()

    # Create index
    index = VectorStoreIndex.from_documents(documents)

    query_engine = index.as_query_engine()


def get_query_engine():
    return query_engine

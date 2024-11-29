from langchain_openai import ChatOpenAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain import hub
from langchain_pinecone import PineconeVectorStore
from langchain_pinecone import PineconeEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PINECONE_ENVIRONMENT = os.getenv("PINECONE_ENVIRONMENT")

def get_retrieval_chain(docsearch):
    retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat")
    retriever=docsearch.as_retriever()

    llm = ChatOpenAI(
        openai_api_key=OPENAI_API_KEY,
        model_name='gpt-4o-mini',
        temperature=0.0
    )

    combine_docs_chain = create_stuff_documents_chain(
        llm, retrieval_qa_chat_prompt
    )
    retrieval_chain = create_retrieval_chain(retriever, combine_docs_chain)
    return retrieval_chain

def create_embedding_obj():
    model_name = 'multilingual-e5-large'
    embeddings = PineconeEmbeddings(
        model=model_name,
        pinecone_api_key=PINECONE_API_KEY
    )
    return embeddings

def getDocSearch(embeddings):
    namespace = "myvector"
    docsearch = PineconeVectorStore.from_existing_index(
        index_name="blog-chatbot-2",
        text_key="text",
        embedding=embeddings,
        namespace=namespace
    )
    return docsearch


def chatbot(query):
    try :
        #initialize_pinecone()
        print('query', query)
        embedding_obj = create_embedding_obj()
        #print('got embedding',embedding_obj)
        pinecone_vector_store = getDocSearch(embedding_obj)
        #print('got vector store',pinecone_vector_store)
        retrieval_chain = get_retrieval_chain(pinecone_vector_store)
        #print('got chain',retrieval_chain)
        answer = retrieval_chain.invoke({"input": query})
        #print(answer)
        return answer
    except Exception as e:
        print(f"An error occurred: {e}")


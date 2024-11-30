from fastapi import FastAPI
from pydantic import BaseModel
from chatbot import chatbot
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (for development)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

class Request(BaseModel):
    query: str

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI!"}

@app.post("/chat")
async def get_answer(req: Request):
    query = req.query
    print('query:', query)
    res = chatbot(query)
    answer = res['answer']
    context = []
    if (answer) :
        context = get_context(res['context'])
    print('query:' + query + '. ' + 'response:' + answer)
    return {
        "query": query,
        "answer": answer,
        "context": context
    }


def get_context(context):
    unique_context = set()
    for c in context:
        unique_context.add(c.metadata['document'])
    return unique_context
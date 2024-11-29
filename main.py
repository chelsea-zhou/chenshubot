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
    print(req)
    query = req.query
    answer = chatbot(query)
    context = get_context(answer['context'])
    return {
        "query": query,
        "answer": answer['answer'],
        "context": context
    }


def get_context(context):
    unique_context = set()
    for c in context:
        unique_context.add(c.metadata['document'] + '.txt')
    return unique_context
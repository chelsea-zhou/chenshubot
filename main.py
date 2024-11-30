from fastapi import FastAPI, Request, HTTPException
from chatbot import chatbot
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

app = FastAPI()
limiter = Limiter(key_func=get_remote_address)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (for development)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Add a global exception handler for rate limiting
@app.exception_handler(RateLimitExceeded)
async def rate_limit_exceeded_handler(request: Request, exc: RateLimitExceeded):
    raise HTTPException(status_code=429, detail="Too many requests. Please try again later.")

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI!"}

@app.post("/chat")
@limiter.limit("5/minute")  # Limit to 5 requests per minute per IP
async def get_answer(request: Request):
    req = await request.json()
    query = req['query']
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
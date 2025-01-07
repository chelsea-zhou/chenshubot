# ChenshuBot: Chat with me through my writings

This chatbot allows users to interact with me through my writings. When a user asks a question:
1. The system searches through a vector database containing my writings
2. It finds the most relevant pieces of my content
3. GPT-4 generates a response based on these relevant writings
4. The response is returned along with context from the original sources

## Live

[Demo](https://chenshuz-website.vercel.app/)

## Tech Stack
Frontend: [repo link](https://github.com/chelsea-zhou/chenshuz-website)
- **Next.js**: Frontend framework
- **TailwindCSS**: Styling framework

Backend: current repo
- **FastAPI**: Backend web framework
- **LangChain**: For orchestrating the AI components
- **Pinecone**: Vector database storing my writing embeddings
- **OpenAI GPT-4**: For generating human-like responses
- **E5-large**: Multilingual embedding model for content search
- **Deployment**: Vercel

## Features

- 🤖 Conversational interface to my writings
- 🔍 Semantic search across my content
- 📚 Context-aware responses
- 🌐 API-first design
- ⚡ Fast response times
- 🔒 Rate limiting for API protection

## Technical Setup

1. Clone the repository and install dependencies:
```bash
git clone https://github.com/chenshu-ai/fastapi-project.git
cd fastapi-project
pip install -r requirements.txt
```
2. Set up environment variables in `.env`:
```bash
PINECONE_API_KEY=your_pinecone_api_key
OPENAI_API_KEY=your_openai_api_key
```
3. Run the FastAPI server:
```bash
uvicorn main:app --reload
```


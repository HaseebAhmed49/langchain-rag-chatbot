from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain.chains import RetrievalQA
from langchain_community.chat_models import ChatOpenAI
from langchain.document_loaders import JSONLoader
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from dotenv import load_dotenv
import os
import json

load_dotenv()

app = FastAPI()
OPENAI_API_KEY= os.getenv("OPENAI_API_KEY")

# Load knowledge base from JSON
loader = JSONLoader(file_path="backend/knowledge_base.json", jq_schema=".[]",text_content=False)

documents = loader.load()
print(documents)
# Create embeddings and vector store
embeddings = OpenAIEmbeddings(api_key=OPENAI_API_KEY)
vector_store = FAISS.from_documents(documents, embeddings)

# Initialize RetrievalQA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model="gpt-4" ,api_key=OPENAI_API_KEY, temperature=0.7),
    chain_type="stuff",
    retriever=vector_store.as_retriever()
)

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        # Query the knowledge base
        response = qa_chain.run(request.message)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
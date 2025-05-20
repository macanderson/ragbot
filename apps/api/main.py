from fastapi import FastAPI
from pydantic import BaseModel
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from packages.vectorstore.store import get_vectorstore

app = FastAPI()

class Query(BaseModel):
    question: str

retriever = get_vectorstore().as_retriever()
qa = RetrievalQA.from_chain_type(llm=OpenAI(model_name="gpt-4"), retriever=retriever)

@app.post("/ask")
async def ask_question(query: Query):
    result = qa.run(query.question)
    return {"answer": result}

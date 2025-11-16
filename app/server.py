from fastapi import FastAPI
import uvicorn
from vllm import LLM

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

llm = LLM(model=..., task="generate")  # Name or path of your model
# vLLM wrapper endpoint
@app.get("/vllm/sample")
def sample():
    output = llm.generate("Hello, my name is")
    return output

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
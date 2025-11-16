from fastapi import FastAPI
import uvicorn
from vllm import LLM, SamplingParams

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

llm = LLM(model="moonshotai/Kimi-K2-Thinking", task="generate")  # Name or path of your model
# vLLM wrapper endpoint
@app.get("/vllm/sample")
def sample():
    prompts = ["Hello, my name is"]
    sampling_params = SamplingParams(temperature=0.8, top_p=0.95)

    outputs = llm.generate(prompts, sampling_params)
    return outputs[0].text

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
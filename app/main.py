# main.py (or app/main.py if you prefer)
from fastapi import FastAPI
from pydantic import BaseModel
from app.competitions import run_competition

app = FastAPI()

class CompetitionRequest(BaseModel):
    prompt: str
    variations: list[str]

@app.post("/run-competition")
def run_competition_endpoint(request: CompetitionRequest):
    results = run_competition(request.prompt, request.variations)
    return {"results": results}

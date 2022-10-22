from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union, List

app = FastAPI()

class ReceipeStep(BaseModel):
    id: int
    action: str


class Receipe(BaseModel):
    name: str
    title: str
    description: Union[str, None] = None
    id: int
    ingredeants: List
    steps: List[ReceipeStep]


@app.get("/")
async def root():
    return {"message": "Receipe API"}


@app.post("/receipe")
async def create_receipe(receipe: Receipe):
    return receipe
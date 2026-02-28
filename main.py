import uvicorn
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel , Field
from src.utils.config import env_settings as settings

class Metadata(BaseModel):
    key: str
    value: str

class Item(BaseModel):
    name: str
    description: str = Field( title="The description of the item", max_length=300)
    tax: float
    metadata : Optional[Metadata]

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World" , "debug_mode" : settings.debug}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": " ".join([word.capitalize() for word in q.split()]) if q else None}


@app.post("/items/")
async def create_item(item: Item):
    return item

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000  , reload=settings.debug)
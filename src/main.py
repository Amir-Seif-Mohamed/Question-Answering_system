import APIs
import models
from fastapi import FastAPI, requests
from pydantic import BaseModel

class item(BaseModel):
    context: str
    question: str
    answers: dict |None 
    
app = FastAPI()
QA_model = models.QA_model()
my_api =APIs.API(QA_model)

@app.post("/answer")
async def Req_an_answer(data: item):
    return my_api.Req_an_answer(data)

@app.post("/answers")
def Req_answers(BaseModel:list[item]):
    return my_api.Req_answers(BaseModel)

#to run the app, run the following command in the terminal:
#uvicorn main:app --reload

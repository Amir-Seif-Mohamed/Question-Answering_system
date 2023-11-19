#The file contains all api endpoints.
from fastapi import HTTPException
import models
class API:
    def __init__(self, model:models.QA_model):
        """ API class constructor.
        """
        self.current_model = model
    def Req_an_answer(self, data):
        try:
            answer = self.current_model.get_an_answer(data)
            return answer
        except:
            raise HTTPException(status_code=404, detail="Dataset not found")
        
    def Req_answers(self, data):
        try:
            answers = self.current_model.get_answers(data)
            return answers
        except:
            raise HTTPException(status_code=404, detail="Dataset not found")
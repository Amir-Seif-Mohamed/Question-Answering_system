""" 
Question Answering system using FastAPI and HuggingFace's transformers library.
"""
from transformers import pipeline,AutoTokenizer, AutoModelForQuestionAnswering
from fastapi.responses import FileResponse
class QA_model:
    """ Model class contains all the BERT-based models for generating accurate answers.
    """ 
    def __init__(self,model_name= 'deepset/bert-base-uncased-squad2'):
        """ Model class constructor.
        Args:
            model_name (str): The name of the model to be used, 
            The one used:bert-base-cased-squad2'.
        """
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForQuestionAnswering.from_pretrained(model_name)
        self.nlp = pipeline('question-answering', model=self.model, tokenizer=self.tokenizer)

    def get_an_answer(self, data)-> str:
        """ Receives single JSON data containing the context paragraph and 
            the question and return the answer as API response.
        Args:
            data (json): json data containing the context paragraph and the question. 

        Returns:
            _type_: answer
        """
        self.data = data
        context = self.data.context
        question = self.data.question
        answer = self.nlp({'question': question, 'context': context})
        return answer.get("answer")

    def get_answers(self,data)-> list:
        """Receives a dataset that contains multiple contexts, questions and its original answer.
            The output should be a csv file that contains the question, the
            original answer and the generated answer.
        Args:
            data (Dataset): _description_

        Returns:
            list: generated answers
        """
        questions = []
        original_answers = []
        generated_answers = []

        for i in range(len(data)):
            context = data[i].context
            question = data[i].question
            answer = self.nlp({'question': question, 'context': context})
            questions.append(question)
            original_answers.append(data[i].answers['text'][0]) 
            generated_answers.append(answer["answer"])

        with open('Results.csv', mode="w") as csv_file:
            csv_file.write("Question,Original Answer,Generated Answer\n")
            for i in range(len(questions)):
                csv_file.write(questions[i]+","+original_answers[i]+","+generated_answers[i]+"\n")

        return FileResponse("./Results.csv", media_type="text/csv")
    

from langchain_openai import ChatOpenAI
import os 
from dotenv import load_dotenv

class GroqLLM:
    def __init__(self):
        load_dotenv()


    def get_llm(self):
        print("Getting LLM")
        print(os.getenv("OPENAI_API_KEY"))
        
        try:
            print(os.getenv("OPENAI_API_KEY"))
            os.environ["OPENAI_API_KEY"]=self.openai_api_key=os.getenv("OPENAI_API_KEY")
            llm=ChatOpenAI(api_key=self.openai_api_key,model="gpt-4o-mini")
            return llm
        except Exception as e:
            raise ValueError(f"Error occurred with exception : {e}")
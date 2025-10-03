import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from configs.config import setting
from langchain.chat_models import init_chat_model


# Initialize the chat model with the settings from the config
model = chat_model = init_chat_model(
    model= setting.model,
    api_key=setting.OPENAI_API_KEY
)

# Function to generate a SQL query using the language model
def llm(prompt):
    """
    Function to generate a response from the language model.
    
    :param prompt: The input prompt for the language model.
    :return: The response from the language model.
    """
    try:
        response = model.stream(prompt)
        
    except Exception as e:
        print(f"Error occurred: {e}")
    
    return response



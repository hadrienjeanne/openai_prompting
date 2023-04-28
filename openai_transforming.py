"""
To install the OpenAI Python library:

!pip install openai

The library needs to be configured with your account's secret key, which is available on the website.

You can either set it as the OPENAI_API_KEY environment variable before using the library:

 !export OPENAI_API_KEY='sk-...'

Or, set openai.api_key to its value:

import openai
openai.api_key = "sk-..."
"""

import openai
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key  = os.getenv('OPENAI_API_KEY')
# openai.api_key  = "eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcHAiLCJzdWIiOiI5NjA1MSIsImF1ZCI6IldFQiIsImlhdCI6MTY4MjY4NTI5MywiZXhwIjoxNjgzMjkwMDkzfQ.o3GdXoxQF-rRuo0AcH71UT-OXPTnmuMAl3D17upCiyM"

def get_completion(prompt, model="gpt-3.5-turbo"): # Andrew mentioned that the prompt/ completion paradigm is preferable for this class
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

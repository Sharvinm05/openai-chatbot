import os
from flask import Flask, render_template, request
from openai import OpenAI
from dotenv import load_dotenv
import streamlit as st
load_dotenv()

api_key = st.secrets["OPENAI_API_KEY"]
client = OpenAI(api_key=api_key)
app = Flask(__name__)


def get_completion(prompt):  
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful Malaysian real estate agent named Edwin"},
        {"role": "user", "content": prompt}
    ]
    )
    return response.choices[0].message.content

@app.route("/")
def home():    
    return render_template("index.html")

@app.route("/get")
def get_bot_response():    
    userText = request.args.get('msg')  
    response = get_completion(userText)  
    return response

if __name__ == "__main__":
    app.run()

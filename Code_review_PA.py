import google.generativeai as genai
import streamlit as st

#setting up the API key
f = open("keys/gemini_api_key.txt")
key = f.read()
genai.configure(api_key = key)

#setting up the headers
st.title("👨‍💻Your Code Review Buddy🈂")
st.subheader('Issues with your python code? Review your codebase now!')

#taking user input
user_prompt = st.text_area("Enter your code...")

#if the button is clicked, generate responses
if st.button("Review") == True:
    model = genai.GenerativeModel(model_name='models/gemini-1.5-pro-latest',
                              system_instruction="""You are a friendly AI assistant.
                                                    Given a python code to review, analyze the submitted code and identify bugs, errors or areas of improvement.
                                                    Provide the fixed code snippets.
                                                    Explain the reasoning behind code corrections or suggestions. 
                                                    If the code is not in python politely 
                                                    remind the user that you are a python code review assistant.
                                                   """)
    
    #if the prompt is provided
    if user_prompt:
        response = model.generate_content(user_prompt)
        
        #printing the response on the webpage
        st.write(response.text)

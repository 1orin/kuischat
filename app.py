import streamlit as st
from langchain_community.llms import OpenAI

st.title('KUIS Simple LLM-App 🤖')

openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')
# Add a sidebar input for the system prompt
system_prompt = st.sidebar.text_area('System Prompt', 'Enter a system prompt here...')

def generate_response(input_text, system_prompt):
    # Concatenate system prompt with user input
    full_input = system_prompt + "\n\n" + input_text
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    # Use the concatenated input for generating the response
    st.info(llm(full_input))

with st.form('my_form'):
    text = st.text_area('Enter text:', '')
    submitted = st.form_submit_button('Submit')
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(text, system_prompt)



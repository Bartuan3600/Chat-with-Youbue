import streamlit as st
from backend import comp_press

def frontend():
    st.set_page_config(page_title="Youtbe_GPT", layout="wide")
    st.title("Chat with Your PDF")

    question = st.text_input("Ask Question below", placeholder='Your Question')

    with st.sidebar:
        st.subheader("Enter your API key")
        api_key = st.text_input("Enter API key", placeholder="sk_test_BQokikJOvBiI2HlWgH4olfQ2", type="password")
        #help="How to get an OpenAI API Key: https://www.howtogeek.com/885918/how-to-get-an-openai-api-key/"
        url = st.text_input("Enter URL below: ", placeholder="www.youtube.com/...")

    if url and api_key is not None:
        if question:
            ans = comp_press(api_key=api_key, url=url, question=question)
            st.write(ans)

if __name__ == "__main__":
    frontend()
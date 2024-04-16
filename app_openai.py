import streamlit as st
from openai import OpenAI

# Read OpenAI API key from file
with open('openai_key.txt') as f:
    OPENAI_API_KEY = f.read().strip()

# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

def check_code(code):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": "You are a code checker and coding instructor."},
            {"role": "user", "content": code}
        ]
    )
    return response.choices[0].message.content

def main():
    st.title("Code Inspector")
    st.markdown(
        """
        Welcome to the Code Inspector app! This app checks your code for errors 
        and provide suggestions for improvement. Simply enter your code in the text area below, 
        and click the "Check Code" button to see the corrected version.
        """
    )
    code = st.text_area("Enter your code here:", height=200)
    if st.button("Check Code"):
        if code:
            st.info("Checking code...")
            corrected_code = check_code(code)
            st.success("Code checked successfully!")
            st.subheader("Corrected code:")            
            st.write(corrected_code)
        else:
            st.error("Please enter some code.")

if __name__ == "__main__":
    main()

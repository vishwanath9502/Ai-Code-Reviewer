import streamlit as st
import google.generativeai as genai

# Configure the Generative AI API key
genai.configure(api_key="AIzaSyA5Upb6djtVUb_gRP5vC12jDkPLidQ6JcA")
llm = genai.GenerativeModel("models/gemini-1.5-flash")

# Configure Streamlit app
st.set_page_config(
    page_title="AI Code Reviewer",
    page_icon="🤖",
    layout="wide",
)

image_path = 'Inno_logo_.png'  # Replace with your actual PNG image file path

# Specify the desired width and height
st.image(image_path, width=400)

# Header Section
st.markdown(
    """
    <style>
    .main-title {
        font-size: 2.5rem;
        color: #4CAF50;
        font-weight: bold;
        text-align: center;
    }
    .sub-title {
        font-size: 1.2rem;
        color: #555555;
        text-align: center;
    }
    .footer {
        text-align: center;
        font-size: 0.9rem;
        color: #aaaaaa;
        margin-top: 50px;
    }
    </style>
    <div>
        <p class="main-title">AI Code Reviewer 🤖</p>
        <p class="sub-title">Analyze and optimize your code with AI.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.sidebar.header("AI Code Reviewer🤖")
st.sidebar.markdown(
    """
    - 💻 **Supported Languages:** Python, Java, C, C++,JS,SQL 
    - 🧠 **Identify Bugs:** Let AI find issues in your code.  
    - ✨ **Receive Fixes:** Get suggestions and optimized snippets.  
    """
)

st.sidebar.image("C:\\Users\\gorla\\streamlit\\Code_Review.png",
    width=300,
)

# Language Selection
language = st.selectbox("👆🏼 Select Programming Language", ["Python", "Java", "C", "C++","JS","SQL"])
st.markdown(f"🙇 Write or Paste Your {language} Code Below:")
code_input = st.text_area("🧑🏻‍💻Enter your code📝:", height=200, placeholder="🙇Write or paste your code here...🧑🏻‍💻")

# Function to Process Code
def analyze_code(language: str, code: str) -> str:
    """
    Function to send the code for AI review.
    :param language: The programming language of the code.
    :param code: The code to analyze.
    :return: Response text containing review and fixes.
    """
    try:
        prompt = f"Review the following {language} code, identify potential bugs, suggest fixes, and optimize it:\n\n{code}"
        chat_bot = llm.start_chat(history=[])
        response = chat_bot.send_message(prompt)
        return response.text
    except Exception as e:
        return f"Error during analysis: {e}"

# Submit Button and Results
if st.button("👾Submit Code for Review"):
    if not code_input.strip():
        st.error("Please enter your code before submitting.")
    else:
        with st.spinner("Analyzing your code...☠️"):
            response_text = analyze_code(language, code_input)
            if response_text.startswith("⚠️"):
                st.error(response_text)
            else:
                st.markdown("### Potential Issues & Suggestions:")
                st.write(response_text)

st.markdown(
    """
    <div class="footer">
        <hr>
        <p>Developed using Streamlit and AI-powered review using Google's Gemini AI</p>
    </div>
    """,
    unsafe_allow_html=True,
)

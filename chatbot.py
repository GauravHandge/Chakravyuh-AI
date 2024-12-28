import streamlit as st
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

# API Key
GROQ_API_KEY = "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"

# Function to set a background image with fixed width and height
def add_background(image_url, width="100%", height="100vh"):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: {width} {height};  /* Set width and height */
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Function to play audio automatically in the background
def play_background_audio():
    audio_url = "https://www.101soundboards.com/sounds/716057-robot-ringtone"  # Replace with your audio URL
    st.markdown(
        f"""
        <audio autoplay loop>
            <source src="{audio_url}" type="audio/mp3">
        </audio>
        """,
        unsafe_allow_html=True
    )

def main():
    # Play audio in the background
    play_background_audio()

    # Set the background image with fixed width and height
    background_image_url = "https://i.gifer.com/7gRx.gif"  # Replace with your desired image URL
    add_background(background_image_url, width="80%", height="100vh")  # Adjust width and height as needed

    st.title("My Chakravyuh AI – Master strategist to unravel complex problems.GPT ")

    # Add customization options to the sidebar
    st.sidebar.title("Select an LLM")
    model = st.sidebar.selectbox(
        "Choose a model",
        ["mixtral-8x7b-32768", "llama-3.2-90b-text-preview", "gemma2-9b-it"]
    )
    conversational_memory_length = st.sidebar.slider(
        "Conversational memory length:", 1, 10, value=5
    )

    memory = ConversationBufferWindowMemory(k=conversational_memory_length)

    user_question = st.text_area("Ask a question:")

    # Initialize chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    else:
        for message in st.session_state.chat_history:
            memory.save_context({"input": message["human"]}, {"output": message["AI"]})

    # Initialize Groq Langchain chat object and conversation
    groq_chat = ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name=model
    )

    conversation = ConversationChain(
        llm=groq_chat,
        memory=memory
    )

    if user_question:
        response = conversation(user_question)
        message = {"human": user_question, "AI": response["response"]}
        st.session_state.chat_history.append(message)
        st.write("Chatbot:", response["response"])

if __name__ == "__main__":
    main()

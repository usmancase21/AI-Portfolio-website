import os
from io import BytesIO
import streamlit as st
from PIL import Image
from openai import OpenAI
import requests
import google.generativeai as genai

# Configure the API key

api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# Custom CSS for background image
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://wallpapercave.com/wp/wp3530389.jpg");
background-size: 120%;
}}
</style>
"""

# Inject the CSS
st.markdown(page_bg_img, unsafe_allow_html=True)

col1, col2 = st.columns(2)

# Define the persona information
persona = """
I am Usman, an accomplished Educator, Youtuber, and Entrepreneur with a deep expertise in Computer Vision, Generative AI, and Data Analytics.
Currently, I am a faculty member at NUST (National University of Sciences and Technology) and NLC Mandra, and I head the IoTAT Department at NLC Atin Mandra. 
My teaching and mentorship have impacted over a million developers, hobbyists, and students worldwide.

I hold a Bachelor's degree in Computer Science from NUST Islamabad, Pakistan, where I developed a strong foundation in Computer Vision.
As an expert in Generative AI, I have made significant contributions to both educational and industrial applications.
I specialize in Prompt Engineering, catering to the needs of educators, marketers, and industry professionals.

My technical prowess extends to web frameworks such as React, NextJS, and Javascript,
and I am proficient in multiple programming languages, including C, C#, Java, Python, and Javascript.
I have created advanced AI curriculums for the 3-year DAE program in AI for the Pakistani education system, and
I have been involved in developing board papers for various IT courses in Pakistan.
 Additionally, I have developed frameworks for the federal board and won multiple international online hackathons, including lablab.ai and Ultrahack Online Hackathon.

Apart from my professional achievements, I am a passionate drone hobbyist, helping many individuals learn drone flying and programming from scratch.
I enjoy sports like football and cricket and prioritize my fitness through regular walks and exercises. Traveling is another passion of mine, allowing me to explore new places and cultures.
For collaborations, educational content, or industry projects, feel free to reach out to me via

Phone Number:03345627545
Usman's Email: usman.qau12@gmail.com
Usman's Instagram: https://www.instagram.com/usman_nustian?utm_source=qr&igsh=MWxucTRuZDRkdnVzaQ==
Usman's Linkdin: https://www.linkedin.com/in/muhammad-usman-awan-0a644b74?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app
Usman Github :https://github.com/usmancase21 
"""

# Sidebar with models selection
st.sidebar.title("My Created ChatBots")
model_option = st.sidebar.radio(
    "Select a model:",
    ("Usman Awan Portfolio ","Chat Generation Model", "Image Generation Model", "Text to Audio Model")
)
if model_option == "Usman Awan Portfolio ":

# Create tabs
    tab1, tab2, tab3, tab4, tab5, tab6= st.tabs(["About", "Personal AI Bot", "My Skills", "My Setup", "My Gallery", "Contact"])

# Assign content to each tab
    with tab1:
        st.header('About')
        st.write('Welcome to the About page.')
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Hi :wave:")
            st.title("I am Muhammad Usman Awan")
            st.write("Opportunity data scientist and generative AI engineer | Heaviest of drone making and flying | Passionate data scientist"
                     )
        with col2:
            st.image("images/usman.jpg")

    with tab2:
        st.header("Usman Awan's AI Bot")
        user_question = st.text_input("Ask anything about me")
        if st.button("ASK"):
            prompt = persona + "Here is the question that the user asked: " + user_question
            response = model.generate_content(prompt)
            st.write(response.text)

    with tab3:
        st.header('My Skills')
        st.write('Here are my skills.')
        st.slider("generative AI programmer ", 0, 100, 90)
        st.slider("AI and machine learning engineer ", 0, 100, 85)
        st.slider("Large language model integration and development export ", 0, 100, 95)
        st.slider("Robotics expert ", 0, 100, 80)
        st.slider("Drone manufacturing integration", 0, 100, 85)
        st.slider("Drone programming expert", 0, 100, 95)

    with tab4:
        st.header('My Setup')
        st.write('This is my setup.')
        st.image("images/setup.jpg")

    with tab5:
        st.header('My Gallery')
        st.write('Here are some pictures of me.')
        col1, col2, col3, col4= st.columns(4)
        with col1:
            st.image("images/g1.jpg")
            st.image("images/g2.jpg")
            st.image("images/g3.jpg")

        with col2:
            st.image("images/g4.jpg")
            st.image("images/g13.jpg")
            st.image("images/g6.jpg")

        with col3:
            st.image("images/g7.jpg")
            st.image("images/g8.jpg")
            st.image("images/g9.jpg")

        with col4:
            st.image("images/g10.jpg")
            st.image("images/g11.jpg")
            st.image("images/g12.jpg") 
            st.image("images/g5.jpg")   
        


    with tab6:
        st.header('Contact')
        st.write('Feel free to contact me here.')
        st.subheader("For any inquiries, email at:")
        st.write("usman.qau12@gmail.com")
        st.subheader("Instagram")
        st.write("https://www.instagram.com/usman_nustian?utm_source=qr&igsh=MWxucTRuZDRkdnVzaQ==")
        st.subheader("LinkedIn")
        st.write("https://www.linkedin.com/in/muhammad-usman-awan-0a644b74?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app")
        st.subheader("Phone Number")
        st.write("+92 3345627545")

############################################
# OpenAI API setup
############################################



api_key = st.secrets["OPENAI_API_KEY"]

def setup_openai(api_key: str) -> OpenAI:
    # Ensure api_key is a string
    if not isinstance(api_key, str):
        raise TypeError("API key must be a string")
    
    # Set up OpenAI API key
    os.environ['OPENAI_API_KEY'] = api_key
    client = OpenAI(api_key=api_key)
    return client

client = setup_openai(api_key)

# Image Generation setup
def generate_image_openai(client: OpenAI, prompt: str, model="dall-e-3", size="1024x1024", n=1):
    response = client.images.generate(
        model=model,
        prompt=prompt,
        size=size,
        n=n,
    )
    image_url = response.data[0].url
    image = requests.get(image_url)
    image = Image.open(BytesIO(image.content))
    return image
# Chat Generation setup
def generate_text_openai_streamlit(client, prompt,text_area_placeholder=None,
                                   model="gpt-4o", temperature=0.5,
                                   max_tokens=3000, top_p=1, frequency_penalty=0,
                                   presence_penalty=0, stream=True, html=False):
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
        stream=stream
    )
    complete_response = []
    for chunk in response:
        # Ensure that chunk content is not None before appending
        if chunk.choices[0].delta.content:
            complete_response.append(chunk.choices[0].delta.content)
            result_string = ''.join(complete_response)  # Join without additional spaces
 
            # Auto Scroll
            lines = result_string.count('\n') + 1
            avg_chars_per_line = 80  # Adjust based on expected average line length
            lines += len(result_string) // avg_chars_per_line
            height_per_line = 20  # Adjust as needed
            total_height = lines * height_per_line
 
 
            if text_area_placeholder:
                if html:
                    text_area_placeholder.markdown(result_string, unsafe_allow_html=True)
                else:
                    text_area_placeholder.text_area("Generated Text", value=result_string,height=total_height)
 
    result_string = ''.join(complete_response)
    words = len(result_string.split())  # This is an approximation
    st.text(f"Total Words Generated: {words}")
 
    return result_string
 
############################################
# OpenAI Audio to Text
############################################

def generate_text_from_audio_openai(client, audio_file,
                                    model="whisper-1", response_format="text"):
    response = client.audio.transcriptions.create(
        model=model,
        file=audio_file,
        response_format=response_format
    )
    return response
 
def main():
    pass


# Display selected model information in the sidebar
st.sidebar.markdown("### Selected Model")
if model_option == "Image Generation Model":
    st.sidebar.write("You have selected the Image Generation Model")
    prompt = st.text_input("Enter your image prompt")
    if st.button("Generate Image"):
        with st.spinner('Generating image...'):
            image = generate_image_openai(client, prompt)
            st.image(image)
    # Add more details or functionality for the Chat Generation Model here

elif model_option == "Usman Awan Portfolio ":
    st.sidebar.write("You have selected the Usman Awan Portfolio.")
    # Add more details or functionality for the Usman Awan Portfolio here

elif model_option == "Chat Generation Model":
    st.sidebar.write("You have selected the Chat Generation Model.")
    
    prompt = st.text_input("Enter your chat prompt")
    text_area_placeholder = st.empty()
    if st.button("Generate Response"):
        with st.spinner('Generating response...'):
            response = generate_text_openai_streamlit(client, prompt, text_area_placeholder,html=True
                                                )
            st.write(response)
    # Add more details or functionality for the Image Generation Model here
elif model_option == "Text to Audio Model":
    st.sidebar.write("You have selected the Text to Audio Model.")
    st.title("Audio to Text")
    audio_file = st.file_uploader("Choose an audio file...", type=["mp3", "wav"])
    
    if audio_file:
        if st.button("Transcribe"):
            st.audio(audio_file, format='audio/wav')
            with st.spinner('Transcribing audio...'):
                try:
                    result = generate_text_from_audio_openai(client, audio_file)
                    print(result)  # Print the result to check if it's empty or contains any error
                    st.write(result)
                except Exception as e:
                    st.error(f"An error occurred: {e}")
    # Add more details or functionality for the Text to Audio Model here

if __name__ == "__main__":
    main()
    

import streamlit as st
from transformers import BlipProcessor, BlipForConditionalGeneration
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from PIL import Image
import pytesseract
import datetime
from gtts import gTTS
from googletrans import Translator  # Import googletrans for translation

# MongoDB connection
uri = "mongodb+srv://ritikasrivastava:ritika12@cluster0.m00l9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["image_captioning"]
captions_collection = db["captions"]

# Load BLIP model and processor
@st.cache_resource
def load_model():
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    return processor, model

processor, model = load_model()

# Custom CSS for styling
st.markdown("""
    <style>
        .stApp {
            background-color: #f0f2f6;
            font-family: Arial, sans-serif;
        }
        .header {
            font-size: 2.5em;
            font-weight: bold;
            color: #ffffff;
            background: linear-gradient(to right, #ff7e5f, #feb47b);
            padding: 15px;
            border-radius: 8px;
            text-align: center;
            margin-bottom: 15px;
        }
        .subheader {
            font-size: 1.3em;
            color: #4a4a4a;
            margin-bottom: 10px;
        }
        .caption-box {
            border-radius: 8px;
            background-color: #f4e8ff;
            padding: 15px;
            margin: 20px 0;
            color: #333333;
            font-weight: bold;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
        }
        .info-box {
            font-size: 1.1em;
            color: #5b9bd5;
        }
        .success-box {
            font-size: 1.1em;
            color: #4CAF50;
        }
        .footer {
            text-align: center;
            font-size: 0.9em;
            color: #7a7a7a;
            margin-top: 50px;
        }
        .btn-refresh {
            background-color: #4CAF50;
            color: #ffffff;
            padding: 10px 20px;
            border-radius: 8px;
            font-weight: bold;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .btn-refresh:hover {
            background-color: #45a049;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar for additional functionality
st.sidebar.header("📁 Caption Manager")
if st.sidebar.button("View Saved Captions"):
    captions = captions_collection.find().limit(20)
    if captions:
        for caption in captions:
            st.sidebar.write(f"**Image Name:** {caption['image_name']}")
            st.sidebar.write(f"**Caption:** {caption['caption']}")
            st.sidebar.write("---")
    else:
        st.sidebar.write("No captions saved yet!")

# Sidebar for selecting description style
st.sidebar.header("⚙️ Customize Caption Style")
description_style = st.sidebar.selectbox(
    "Choose Description Style",
    ["Detailed", "Concise", "Simple Language"]
)

st.sidebar.write("Select your preferred style for generating captions.")

# Language selection for translation
target_language = st.sidebar.selectbox("Translate to", ["None", "es", "fr", "de", "it", "pt", "zh-cn"])

# Title and description with enhanced header styling
st.markdown("<div class='header'>🖼️ InnoCaption </div>", unsafe_allow_html=True)
st.markdown("<div class='subheader'>Generate or detect accessible captions with ease.</div>", unsafe_allow_html=True)

# Function to detect existing caption using OCR
def detect_existing_caption(image):
    ocr_text = pytesseract.image_to_string(image).strip()
    return ocr_text if ocr_text else None

# Translate function using googletrans
def translate_caption(caption, lang_code):
    translator = Translator()
    translated = translator.translate(caption, dest=lang_code)
    return translated.text

 # Function to provide voice feedback
def provide_voice_feedback(text):
    tts = gTTS(text=text, lang='en')
    tts.save("feedback.mp3")
    audio_file = open("feedback.mp3", "rb")
    st.audio(audio_file)
   
# Image upload with alignment
uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"], label_visibility="collapsed")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    
    # Display uploaded image
    col1, col2, col3 = st.columns([1, 4, 1])
    with col2:
        st.image(image, caption="Uploaded Image", use_container_width=True)
    
    # Check for existing caption
    existing_caption = detect_existing_caption(image)
    
    # Decide on caption to use based on style
    if existing_caption:
        caption_to_use = existing_caption
        st.markdown(f"<div class='caption-box info-box'>📄 Detected Existing Caption: {caption_to_use}</div>", unsafe_allow_html=True)
        provide_voice_feedback(f"Caption generated: {caption_to_use}")
    else:
        inputs = processor(images=image, return_tensors="pt")
        caption_ids = model.generate(**inputs)
        generated_caption = processor.decode(caption_ids[0], skip_special_tokens=True)

        # Adjust caption based on selected style
        if description_style == "Detailed":
            caption_to_use = generated_caption  # Keep as is for detailed
        elif description_style == "Concise":
            caption_to_use = "A concise version: " + generated_caption.split(",")[0]  # Shorten to first part
        elif description_style == "Simple Language":
            caption_to_use = "Here is a simpler description: " + " ".join(generated_caption.split()[:10])  # Simplify

        st.markdown(f"<div class='caption-box success-box'>✅ {description_style} Caption: {caption_to_use}</div>", unsafe_allow_html=True)
        provide_voice_feedback(f"Caption generated: {caption_to_use}")

 # Translate the caption if selected
    if target_language != "None":
        translated_caption = translate_caption(caption_to_use, target_language)
        st.markdown(f"<div class='caption-box success-box'>🌍 Translated Caption ({target_language}): {translated_caption}</div>", unsafe_allow_html=True)
        provide_voice_feedback(f"Caption translated to {target_language}: {translated_caption}")

    # Save to MongoDB with initial data
    caption_data = {
        "image_name": uploaded_file.name,
        "caption": caption_to_use,
        "timestamp": datetime.datetime.now(datetime.timezone.utc),
    }
    captions_collection.insert_one(caption_data)
    st.success("Caption and image details stored in MongoDB successfully!")

    # Add a feedback section with voice input option
st.markdown("<div class='subheader'>📢 User Feedback & Suggestions</div>", unsafe_allow_html=True)

# Text Box for Feedback
feedback = st.text_area("Provide your feedback or suggestions here:", height=150)
if st.button("Submit Feedback"):
    if feedback:
        # Save the feedback to MongoDB or any other storage for analysis
        feedback_data = {
            "feedback": feedback,
            "timestamp": datetime.datetime.now(datetime.timezone.utc),
        }
        # Here you could save it to a MongoDB collection or a file
        # feedback_collection.insert_one(feedback_data)
        st.success("Thank you for your feedback! We will improve based on your suggestions.")
    else:
        st.warning("Please enter some feedback before submitting.")

 # Accessible Documentation Section
st.markdown("""
    <div class='accessible-doc'>
        🎧 <b>Audio-based Documentation:</b> This tool allows you to upload an image, generate a caption, and store it for future reference. You can also translate the caption into various languages and have it read aloud for easier accessibility. Simply upload an image, choose the style of caption you prefer, and select any additional options such as translation or voice feedback. 
    </div>
""", unsafe_allow_html=True)

# Footer with hackathon credits and styling
st.markdown("<div class='footer'>Built with 💻 and ☕ for the Hack This Fall 2024 Virtual Hackathon. Making images more accessible, one caption at a time!</div>", unsafe_allow_html=True)

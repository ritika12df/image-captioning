## InnoCaption: Image Captioning and Accessibility Tool

# Overview
InnoCaption is a web-based tool designed to generate and detect captions for images, making visual content more accessible. The application leverages powerful image captioning models, Optical Character Recognition (OCR), and Google Translate for multi-language support. Additionally, the tool can read captions aloud using Google Text-to-Speech (gTTS) to ensure accessibility for users with visual impairments.

## Features

# 1. Image Upload

Upload images in JPG, JPEG, or PNG format.

Supports visual and textual content from images.

# 2. Caption Generation

Utilizes the BLIP (Bootstrapping Image Pretraining) model to generate captions for uploaded images.

You can choose between three different caption styles:

Detailed

Concise

Simple Language

# 3. Caption Detection

If the image contains an existing caption, the tool automatically detects it using OCR (Optical Character Recognition) via pytesseract.

# 4. Translation

Translates captions into multiple languages including Spanish, French, German, Italian, Portuguese, and more, using Google Translate.

# 5. Voice Feedback

Generates voice feedback of the captions using Google Text-to-Speech (gTTS).

Allows users to listen to the generated captions and translations.

# 6. MongoDB Integration

Stores captions along with metadata (image name, timestamp) in a MongoDB database.

Provides an option to view stored captions via the sidebar.

# 7. User Feedback

Users can submit feedback or suggestions directly in the app.

Feedback is stored in the backend for future improvements.

# 8. Accessible Documentation

Audio-based documentation explains the use of the tool and its features, enhancing the accessibility for users with visual impairments.

# 9. Interactive Sidebar

View and manage saved captions.

Customize caption styles.

Select target language for translation.

## Technologies Used

Streamlit: A Python framework for creating interactive web applications.

BLIP: A pre-trained model used for image caption generation.

pytesseract: Python library used for optical character recognition (OCR).

gTTS (Google Text-to-Speech): Used for generating voice feedback.

Google Translate: For translating captions into different languages.

MongoDB: Cloud-based database for storing captions and feedback.

PIL (Python Imaging Library): Used for image processing.

## Installation

`- Clone the repository:

```bash
git clone https://github.com/ritika12df/image-captioning
cd image-captioning
```

Install required Python packages:

```bash
pip install -r requirements.txt
```
Run the Streamlit app:

```bash
streamlit run app.py
```
## Usage

- Upload Image: Use the "Upload Image" button to upload your desired image in JPG, JPEG, or PNG format.

- Generate Caption: The tool will automatically generate a caption for the uploaded image. Choose from different caption styles (Detailed, Concise, Simple Language) for customization.

- Voice Feedback: You can listen to the generated caption using the voice feedback option. If the caption is translated, the translated caption is also read aloud.

- Translate Caption: Select the language you want the caption to be translated into (if applicable).

- Save to MongoDB: The image name, caption, and timestamp are saved to a MongoDB database for later access.

- Provide Feedback: Share your feedback or suggestions in the provided feedback section.

## MongoDB Configuration

InnoCaption uses MongoDB to store image captions and user feedback. Ensure that you have a MongoDB cluster set up. You can sign up for a free MongoDB Atlas account if you don't have one.

MongoDB URI: The application uses a URI to connect to MongoDB. Replace the uri in the script with your own MongoDB connection string.

```bash
uri = "mongodb+srv://your-mongo-credentials@cluster-url.mongodb.net/?retryWrites=true&w=majority"
```
# Database and Collections:

The captions are stored in the captions collection of the image_captioning database.

You can add additional collections for feedback or other purposes as needed.

## Contributing

We welcome contributions to improve the functionality of InnoCaption. If you'd like to contribute, feel free to fork the repository and submit a pull request.

## License

This project is open-source and available under the MIT License. See the LICENSE file for more information.

## Acknowledgments

BLIP: For image captioning.

pytesseract: For OCR functionality.

gTTS: For text-to-speech conversion.

Google Translate: For multilingual support.

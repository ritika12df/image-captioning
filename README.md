## InnoCaption
A Streamlit-based tool that makes online images more accessible by automatically generating captions. It also detects existing captions using Optical Character Recognition (OCR), making it perfect for users with visual impairments. The tool stores the captions along with image data in a MongoDB database for easy retrieval.

## Table of Contents
Project Overview
Tech Stack
Features
Installation
Usage
Folder Structure
Contributing
License
Credits


## Project Overview

The Accessible Image Captioning Tool allows users to upload images, generate captions, and detect existing text via OCR to make images more accessible. The captions are customizable based on user preferences such as detailed, concise, or simplified language. The tool stores all captions and image details in a MongoDB database for easy reference and future use.

This project is intended to provide a way for people with visual impairments to understand images on the web by generating or detecting captions that describe the content of the images.

## Tech Stack

Frontend: Streamlit (for building the web app)
Model: BLIP (Bootstrapping Image Pre-training) for image captioning
OCR: Tesseract for Optical Character Recognition (OCR) to detect existing text in images
Database: MongoDB (for storing captions and image details)
Backend: Python (for handling image caption generation and OCR processing)

## Features

Image Upload: Upload images in JPG, JPEG, or PNG formats.
Caption Generation: Automatically generate captions for images using the BLIP model.
OCR Support: Detect existing captions or text in images using OCR and use them if available.
Customizable Captions: Choose between detailed, concise, or simplified captions based on your needs.
MongoDB Storage: Captions and image metadata (such as image name and timestamp) are saved to MongoDB for future access.
User Interface: Interactive and easy-to-use interface built using Streamlit.

## Installation
# Prerequisites
Before you begin, ensure that you have the following installed on your system:

Python 3.8 or above

MongoDB (you can use MongoDB Atlas if you prefer cloud storage)
Step 1: Clone the Repository
''
git clone https://github.com/yourusername/accessible-image-captioning.git''
cd accessible-image-captioning
Step 2: Set up a Virtual Environment (optional but recommended)
bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Step 3: Install the Dependencies
Install the necessary Python libraries by running:

bash
Copy code
pip install -r requirements.txt
Step 4: Set Up MongoDB
If you're using MongoDB Atlas, create an account and set up a cluster.
If you're using local MongoDB, make sure MongoDB is installed and running.
Update the uri in the script to reflect your MongoDB connection string.
Step 5: Run the Streamlit App
Once everything is set up, you can start the app with:

bash
Copy code
streamlit run app.py
This will open the application in your default web browser.

## Usage
Upload an Image: Drag and drop or select an image in JPG, JPEG, or PNG format.
Choose Caption Style: Select one of the following caption styles from the sidebar:
Detailed: A full, descriptive caption of the image.
Concise: A shortened version of the caption.
Simple Language: A simplified description of the image.
Generate Caption: The tool will generate a caption for the image. If there is any existing text in the image, the OCR functionality will detect it and use it as the caption.
View Saved Captions: The captions will be stored in MongoDB, and you can view the most recent ones in the sidebar.
Folder Structure
plaintext
Copy code
accessible-image-captioning/
│
├── app.py                # Main Streamlit app file
├── requirements.txt      # Required Python libraries
├── assets/               # (Optional) Folder for storing image assets
├── README.md             # This file
└── utils.py              # Helper functions for OCR and MongoDB operations
Contributing
We welcome contributions to improve this tool! If you'd like to help, follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature-name).
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature-name).
Open a pull request.
License
This project is licensed under the MIT License - see the LICENSE file for more details.

Credits
BLIP (Bootstrapping Image Pre-training): For the image captioning model. BLIP GitHub
Streamlit: For building the interactive web interface. Streamlit
Tesseract: For Optical Character Recognition (OCR). Tesseract OCR GitHub
MongoDB: For storing captions and image metadata. MongoDB

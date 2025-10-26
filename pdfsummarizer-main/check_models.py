import google.generativeai as genai
import os
from dotenv import load_dotenv
import logging

# Set logging to see detailed errors if they happen
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

# Load the .env file just like our app
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    log.error("Error: GOOGLE_API_KEY not found in .env file.")
    log.error("Please ensure your .env file is in the same directory and has the correct variable name.")
else:
    log.info("API key found. Configuring client...")
    try:
        genai.configure(api_key=api_key)

        log.info("Fetching available models from Google AI...\n")

        print("--- Available Models for 'generateContent' ---")

        # This will list all models
        for model in genai.list_models():
            # We only care about models that can be used for text generation
            if 'generateContent' in model.supported_generation_methods:
                print(f"Model Name: {model.name}")

        print("\n-------------------------------------------------")
        log.info("Finished. Please use one of the 'Model Name' values listed above in your summarizer.py file.")

    except Exception as e:
        log.error(f"An error occurred while trying to list models: {e}")
        log.error(
            "This often happens if the API key is incorrect or has not been enabled for the Generative AI API in your Google Cloud project.")

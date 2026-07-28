from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load variables from the .env file
load_dotenv()

# Get the API key
api_key = os.getenv("AIzaSyDMqAhNmRv3hszkr2XhwPp9h7_7gidNxzs")

# Configure Gemini
genai.configure(api_key=api_key)

# Create the model
model = genai.GenerativeModel("gemini-2.5-flash")
# Ask Gemini something
response = model.generate_content("Say hello in one sentence.")

print(response.text)
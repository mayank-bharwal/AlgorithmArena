'''import openai
from PIL import Image, ImageDraw, ImageFont
from instabot import Bot
import time
import os

# OpenAI API key
openai.api_key = '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'

def generate_coding_question(prompt, temperature=0.7, max_tokens=100):
    try:
        response = openai.Completion.create(
            engine="text-davinci-004",
            prompt=prompt,
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error generating question: {e}")
        return None

def create_social_media_image(question, filename="coding_question.png"):
    # Image dimensions and colors
    width, height = 800, 400
    background_color = (255, 255, 255)  # White background
    text_color = (0, 0, 0)  # Black text

    # Create an image with a specific background color
    img = Image.new('RGB', (width, height), color=background_color)
    d = ImageDraw.Draw(img)

    # Load a custom font
    try:
        font = ImageFont.truetype("Lemon-Regular.ttf", 20)
    except IOError:
        font = ImageFont.load_default()
        print("Custom font not found. Using default font.")

    # Add text to the image
    d.text((20, 50), question, fill=text_color, font=font)

    #Optionally add your logo or other elements
    logo = Image.open("logo.png")
    img.paste(logo, (650, 300), logo)

    # Save the image
    img.save(filename)


# Login to Instagram
#bot = Bot()
#bot.login(username="algorithmarena", password="mayank29")

while True:
    question = generate_coding_question("Create a unique and interesting coding question in python for a computer science student at an easy to medium difficulty level:")
    if question:
        image_filename = "coding_question.png"
        create_social_media_image(question, image_filename)
        #bot.upload_photo(image_filename, caption=question)
        #if bot.api.last_response.status_code != 200:
            #print("Error uploading photo.")

    # Wait for 24 hours
    time.sleep(86400)  # 86400 seconds in a day'''

import openai
from PIL import Image, ImageDraw, ImageFont
from instabot import Bot
import os
import textwrap

# Load OpenAI API key from an environment variable
client = openai()

def generate_coding_question(prompt, temperature=0.7, max_tokens=100):
    try:
        response = client.chat.completions.create(
            engine="text-davinci-004",
            prompt=prompt,
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error generating question: {e}")
        return None

def create_social_media_image(question, filename="coding_question.png"):
    # Image dimensions and colors
    width, height = 800, 400
    background_color = (255, 69, 0)  # Reddish orange background
    text_color = (0, 0, 0)  # Black text

    # Create an image with a specific background color
    img = Image.new('RGB', (width, height), color=background_color)
    d = ImageDraw.Draw(img)

    # Load a custom font
    try:
        font = ImageFont.truetype("Lemon-Regular.ttf", 20)
    except IOError:
        font = ImageFont.load_default()
        print("Custom font not found. Using default font.")

    # Wrap text
    wrapped_text = textwrap.fill(question, width=70)

    # Add text to the image
    d.text((20, 50), wrapped_text, fill=text_color, font=font)

    # Optionally add your logo or other elements
    try:
        logo = Image.open("logo.png")
        img.paste(logo, (650, 300), logo)
    except IOError:
        print("Logo file not found.")

    # Save the image
    img.save(filename)

def post_to_instagram(filename):
    # Placeholder for Instabot code to post the image
    # bot = Bot()
    # bot.login(username='your_username', password='your_password')
    # bot.upload_photo(filename, caption='Here is a coding question!')
    pass

# Example usage
question = generate_coding_question("Create a unique and interesting coding question in python for a computer science student at an easy to medium difficulty level:")
if question:
    create_social_media_image(question)
    # post_to_instagram("coding_question.png")

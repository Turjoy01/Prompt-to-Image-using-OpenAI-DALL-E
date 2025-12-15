# main.py

import os
import requests
from io import BytesIO
from PIL import Image
from openai import OpenAI   # pip install openai

# ================== CONFIG ==================
API_KEY = os.getenv("OPENAI_API_KEY", "your-api-key-here")

client = OpenAI(api_key=API_KEY)


def get_image():
    prompt = input("Which image you want to generate? ")

    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        n=1,
        size="1024x1024",       
    )

    image_url = response.data[0].url
    return image_url


def main():
    img_url = get_image()
    print("Image URL:", img_url)

    # Download the image
    res = requests.get(img_url)

    # Save as PNG
    file_name = "image.png"
    with open(file_name, "wb") as f:
        f.write(res.content)

    # Open and display
    img = Image.open(file_name)
    img.show()


if __name__ == "__main__":
    main()
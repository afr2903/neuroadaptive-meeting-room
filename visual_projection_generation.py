import requests
import os
import time
from PIL import Image
from io import BytesIO
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class ImageGenerator:
    def generate_image(self, prompt):
        response = client.images.generate(
            model="dall-e-2",
            prompt=prompt,
            n=1,
            quality="standard",
            size="1024x1024",
        )
        image_url = response.data[0].url
        print(f"Generated image URL: {image_url}")
        time.sleep(1)
        self.display_image(image_url)

    def display_image(self, url):
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        img.show()

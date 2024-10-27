import threading
import cv2
from PIL import Image
import io
from dotenv import load_dotenv
import os
import tkinter as tk
import google.generativeai as genai
import google.ai.generativelanguage as glm
from visual_projection_generation import ImageGenerator
from binaural_beats import generate_binaural_beat

load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
model = genai.GenerativeModel('gemini-1.5-flash')
image_generator = ImageGenerator()

class ContentDescriber:
    def __init__(self, root, user_input, video_handler):
        self.root = root
        self.user_input = user_input
        self.video_handler = video_handler
        self.message_var = tk.StringVar()

    def describe_content(self):
        current_frame = self.video_handler.get_current_frame()
        if current_frame is not None:
            pil_image = Image.fromarray(cv2.cvtColor(current_frame, cv2.COLOR_BGR2RGB))
            img_byte_arr = io.BytesIO()
            pil_image.save(img_byte_arr, format='JPEG')
            blob = glm.Blob(
                mime_type='image/jpeg',
                data=img_byte_arr.getvalue()
            )
            #user_request = self.user_input.get()
            user_request = """Infer the overrall internal state and collective 
            conciousness of the room, by analyzing the facial expressions of 
            each individual present, and any behavioral cues obtainable from 
            the image. From this information, generate a detailed description 
            of a biophilic image to be used by an image generator, the image is 
            going to be actively displayed to the individuals with the goal of 
            drving the collective conciousness of the room towards a desired 
            state of focus for work meeetings. It should be a landspace 
            (natural or city) without any humans nor text. As a response, only 
            provide one parahraph describing the image to be generated, not any 
            additional text."""

            response = model.generate_content([user_request, blob], stream=False)
            print(f"Descripton: {response.text}")
            image_generator.generate_image(response.text)
            # for chunk in response:
                #self.root.after(0, self.update_message, chunk.text)
            return response
        else:
            self.root.after(0, self.update_message, "No frame available")

    def threaded_describe_content(self):
        describe_thread = threading.Thread(target=self.describe_content)
        describe_thread.start()
        audio_thread = threading.Thread(target=generate_binaural_beat)
        audio_thread.start()

    def update_message(self, new_text):
        current_text = self.message_var.get()
        updated_text = current_text + new_text + "\n"
        self.message_var.set(updated_text)
# Symbiosis Project
Designing an adaptive room for captivating the collective consciousness from internal states.
## Longevity, AI, and Cognitive Research Hackathon at MIT Media lab by *ekkolapto* and *Augmentation lab*

For **demo** purposes as a workflow showcasing, multimodal language models (MMLMs) were implemented via API requests.

Features shown:
- Video capturing with `opencv`
- Image analysis with `gemini-1.5-flash`, delivers a description for the image generator.
- Image generation with `dall-e-2`
- Image display with `PIL`
- Binaural beats generation with `sounddevice`

Recorded demos (no audio capturing):

[Screencast from 2024-10-27 14-56-43.webm](https://github.com/user-attachments/assets/7e00019c-5d3c-4b0a-9698-042eeb2880e1)

[Screencast from 2024-10-27 14-52-53.webm](https://github.com/user-attachments/assets/f8ae9bff-39d8-48d6-b2ed-08418b53f028)


### Running instructions
*Test system*: Laptop with GTX 1650, on Ubuntu 24.04.1 with Python 3.12

- Install Tkinter from apt: `sudo apt-get install python3-tk`
- Install Portaudio from apt: `sudo apt-get install portaudio19-dev`
- Clone the repository
- Create a virtual environment: `python -m venv env`
- Activate virtual env: `source env\bin\activate`
- Install libraries: `pip install -r requirements.txt`
- Create `.env` file, with API keys (`OPENAI_API_KEY`,`GOOGLE_API_KEY`)
- Run: `python3 hack-demo.py`

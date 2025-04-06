import base64
import os
from google.genai import types
import google.generativeai as genai


def generate():
    client = genai.Client(
        api_key=os.environ.get("AIzaSyCiZqCvJrm7he0rSRnZxtbOCTboNMNX0II"),
    )

    model = "gemini-1.5-flash"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""Hola, ¿cómo estás?"""),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        response_mime_type="text/plain",
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")

if __name__ == "__main__":
    generate()

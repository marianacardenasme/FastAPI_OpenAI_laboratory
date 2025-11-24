import os
from openai import OpenAI

# Crear cliente usando la variable de entorno
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_description(input_text: str) -> str:
    """Generate a rich product description using OpenAI"""

    prompt = f"""
    You are a Product Description Generator.

    Write a multi-paragraph product description (friendly tone, engaging, professional).
    Include formatting where appropriate and some emojis if relevant.

    Product info:
    {input_text}
    """

    # Nueva API moderna
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text


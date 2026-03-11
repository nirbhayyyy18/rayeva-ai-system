import os
import json
import re
from dotenv import load_dotenv
from groq import Groq

from backend.prompts.category_prompt import build_prompt
from backend.utils.logger import log_ai

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_category(name, description):

    prompt = build_prompt(name, description)

    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[{"role": "user", "content": prompt}]
    )

    text = response.choices[0].message.content

    log_ai(prompt, text)

    text = text.replace("```json", "").replace("```", "").strip()

    try:

        json_match = re.search(r"\{.*\}", text, re.DOTALL)

        result = json.loads(json_match.group())

    except:

        result = {
            "error": "Invalid AI response",
            "raw_response": text
        }

    return result
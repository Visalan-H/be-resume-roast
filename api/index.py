from flask import Flask, request, jsonify
import fitz
from dotenv import load_dotenv
from flask_cors import CORS
from google import genai
import os

load_dotenv()

app=Flask(__name__)

api_key=os.getenv("GEMINI_API_KEY")
FE_ENDPOINT=os.getenv("FE_ENDPOINT")
client=genai.Client(api_key=api_key)
CORS(app, origins=[FE_ENDPOINT])


@app.route('/')
def home():
    return "Hello"

@app.route('/upload_resume', methods=['POST'])
def roastPdf():
    if 'resume' not in request.files:
        return jsonify(error="no file"),400

    file=request.files['resume']

    if not file.filename.endswith('.pdf'):
        return jsonify(error="Only PDF files allowed"), 400

    pdf_bytes=file.read()

    pdf_document=fitz.open(stream=pdf_bytes,filetype="pdf")

    full_text=""
    for pageIndex in range(pdf_document.page_count):
        page=pdf_document.load_page(pageIndex)
        full_text+=page.get_text()

    if not full_text.strip():
        return jsonify(error="No text found in PDF"), 400


    prompt = f"""
Roast this resume in a harsh and sarcastic way but constructively.

Requirements:
- Keep it concise (3 paragraphs max for the roast)
- Start with an overall roast (2 paragraph)
- Follow with 3-4 specific constructive criticisms (bullet points format)
- Don't let it be too short or too long
- Be direct and punchy, not verbose 
- Focus on the most glaring issues
- Use simple, everyday words the average high-schooler can understand!!
- Use **bold** bullet point titles
- Use _italic_ for emphasis and subtle points, don't use single asterisks
- Avoid jargon or complex terms
- Don't use too much /n or /n/n

Resume text:
{full_text}
"""


    response=client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt
    )

    return jsonify(roast=response.text),200


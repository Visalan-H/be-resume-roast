# Resume Roaster Backend 🔥

Flask-based backend API for the Resume Roaster application, powered by Google Gemini AI for resume analysis.

## Features

- **PDF Text Extraction**: Extracts text from PDF resumes using PyMuPDF
- **AI-Powered Analysis**: Uses Google Gemini 2.5 Flash Lite for resume roasting
- **Constructive Feedback**: Generates sarcastic yet helpful criticism
- **Text Formatting**: Supports rich text formatting in responses
- **CORS Support**: Configured for cross-origin requests from frontend
- **File Validation**: Ensures only valid PDF files are processed

## Tech Stack

- **Flask** - Lightweight Python web framework
- **Google Gemini AI** - Advanced language model for analysis
- **PyMuPDF (fitz)** - PDF text extraction library

## Project Structure

```
backend/
├── api/
│   └── app.py         # Main Flask application
├── requirements.txt   # Python dependencies
├── vercel.json        # Vercel deployment configuration
├── .env               # Environment variables (apikey and frontend-endpoint)
└── README.md          # me
```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Google Gemini API key

### Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Create environment file:**
   Create a `.env` file in the backend root directory:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   FE_ENDPOINT=http://localhost:5173
   ```

3. **Get Google Gemini API Key:**
   - Visit [Google AI Studio](https://aistudio.google.com/)
   - Create a new API key
   - Add it to your `.env` file

4. **Run the application:**
   ```bash
   python api/app.py
   ```

The server will start on `http://localhost:5000`


## File Validation

The API enforces the following restrictions:
- **File Type:** Only PDF files (`.pdf` extension)
- **Content:** PDF must contain extractable text
- **Size:** Handled by frontend (4MB max)

## AI Prompt Configuration

The Gemini AI is configured with specific instructions:

### Roast Requirements
- **Length:** 3 paragraphs maximum
- **Structure:** 2 paragraphs general roast + 3-4 bullet points
- **Tone:** Harsh but constructive
- **Language:** Simple, high-school level vocabulary
- **Focus:** Most glaring resume issues

```

import os
import io
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Using the fast model from your list
model = genai.GenerativeModel('gemini-3.5-flash')

# Initialize FastAPI App
app = FastAPI()

# Allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/generate-ui")
async def generate_ui(image: UploadFile = File(...)):
    try:
        # Read the image bytes
        image_bytes = await image.read()
        
        # Convert bytes to PIL Image
        img = Image.open(io.BytesIO(image_bytes))

        # SPEED OPTIMIZATION: Resize image so AI processes it much faster
        img.thumbnail((1024, 1024))

        # Strict Prompt for the AI
        prompt = """
        You are an elite Frontend Developer. Look at this hand-drawn wireframe/sketch and generate a complete, working HTML file using Tailwind CSS (via CDN).
        Rules:
        1. Return a single HTML file containing all structural tags, classes, and dummy content.
        2. Make it beautiful, modern, and fully responsive.
        3. Use standard Tailwind classes. Add generic placeholder images from Unsplash (e.g., https://source.unsplash.com/random/800x600) if an image box is drawn.
        4. CRITICAL: Output ONLY the raw HTML code. Do NOT wrap it in ```html ... ``` markdown block. No explanations, no pleasantries. Return only valid HTML.
        """

        # Call Gemini Vision API
        response = model.generate_content([prompt, img])
        
        # Clean up output just in case AI still adds markdown
        html_code = response.text
        html_code = html_code.replace("```html", "").replace("```", "").strip()
        
        return {"success": True, "code": html_code}

    except Exception as e:
        return {"success": False, "error": str(e)}
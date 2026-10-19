import os
import io
import base64
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# FIXED: Changed from nonexistent 3.5 to the actual fast model
model = genai.GenerativeModel('gemini-1.5-flash')

# Initialize FastAPI App
app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 1. Create a schema to receive JSON from frontend
class ImageRequest(BaseModel):
    image: str

@app.post("/generate-ui")
async def generate_ui(request: ImageRequest):
    try:
        # 2. Decode Base64 string back into image bytes
        # Frontend sends "data:image/jpeg;base64,iVBORw0KG..." so we split by comma
        base64_data = request.image.split(",")[1] if "," in request.image else request.image
        image_bytes = base64.b64decode(base64_data)
        
        # 3. Convert to PIL Image
        img = Image.open(io.BytesIO(image_bytes))

        # SPEED OPTIMIZATION
        img.thumbnail((1024, 1024))

        prompt = """
        You are an elite Frontend Developer. Look at this hand-drawn wireframe/sketch and generate a complete, working HTML file using Tailwind CSS (via CDN).
        Rules:
        1. Return a single HTML file containing all structural tags, classes, and dummy content.
        2. Make it beautiful, modern, and fully responsive.
        3. Use standard Tailwind classes. Add generic placeholder images from Unsplash (e.g., https://source.unsplash.com/random/800x600) if an image box is drawn.
        4. CRITICAL: Output ONLY the raw HTML code. Do NOT wrap it in ```html ... ``` markdown block. No explanations, no pleasantries. Return only valid HTML.
        """

        response = model.generate_content([prompt, img])
        
        html_code = response.text
        html_code = html_code.replace("```html", "").replace("```", "").strip()
        
        return {"success": True, "code": html_code}

    except Exception as e:
        return {"success": False, "error": str(e)}
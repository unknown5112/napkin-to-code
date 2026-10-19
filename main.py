import os
import base64
import google.generativeai as genai
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Render environment variables se saari keys uthayega
KEYS_ENV = os.getenv("GEMINI_API_KEYS", "")
API_KEYS = [k.strip() for k in KEYS_ENV.split(",") if k.strip()]

class UIRequest(BaseModel):
    image: str

@app.post("/generate-ui")
async def generate_ui(request: UIRequest):
    if not API_KEYS:
        raise HTTPException(status_code=500, detail="API keys backend mein configure nahi hain.")

    # Frontend se aayi base64 image ko clean karna
    img_data = request.image
    if "," in img_data:
        img_data = img_data.split(",")[1]

    # AI ke liye prompt
    prompt = """
    You are an expert frontend developer. Convert this wireframe sketch into functional, responsive HTML and Tailwind CSS code. 
    Return ONLY the valid HTML code starting with <!DOCTYPE html>. Do NOT include any markdown blocks like ```html or explanations.
    """

    # Ek-ek karke keys try karna
    for index, key in enumerate(API_KEYS):
        try:
            print(f"Trying API Key {index + 1}...")
            genai.configure(api_key=key)
            
            model = genai.GenerativeModel('gemini-3.5-flash')
            
            # AI ko image aur prompt bhejna
            response = model.generate_content([
                prompt, 
                {"mime_type": "image/jpeg", "data": img_data}
            ])
            
            # Agar AI markdown bhej de (```html ... ```), toh usko saaf karna
            final_code = response.text.strip()
            if final_code.startswith("```html"):
                final_code = final_code.replace("```html", "", 1)
            if final_code.endswith("```"):
                final_code = final_code.rsplit("```", 1)[0].strip()

            return {"success": True, "code": final_code}

        except Exception as e:
            error_msg = str(e).lower()
            # Agar quota limit ka error hai, toh agli key try karega
            if "429" in error_msg or "quota" in error_msg or "exhausted" in error_msg:
                print(f"Key {index + 1} ki limit khatam. Next key par switch kar raha hu...")
                continue
            else:
                # Agar prompt ya image mein problem hai toh direct error throw karega
                raise HTTPException(status_code=500, detail=str(e))
    
    # Jab saari keys exhaust ho jayein
    raise HTTPException(status_code=429, detail="Saari API keys ki limit khatam ho chuki hai. Kal try karein!")
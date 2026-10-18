# 🪄 Napkin-to-Code

![Build Status](https://img.shields.io/badge/Status-Live-success)
![Python](https://img.shields.io/badge/Python-FastAPI-blue)
![AI](https://img.shields.io/badge/AI-Google%20Gemini%203.5%20Flash-orange)
![Frontend](https://img.shields.io/badge/Frontend-Tailwind%20CSS-teal)

**Napkin-to-Code** is an AI-powered developer tool that transforms hand-drawn wireframes and paper sketches into fully functional, responsive, and production-ready HTML/Tailwind CSS code in seconds.

🔗 **[Live Demo]** *(https://unknown5112.github.io/napkin-to-code/)*

---

## 🚀 Features

- **📸 Dual Input System:** Upload a digital sketch from your gallery or capture a paper wireframe directly using your device's camera.
- **⚡ Blazing Fast AI:** Powered by the latest **Google Gemini 3.5 Flash** vision model, optimized with backend image compression for lightning-fast code generation.
- **💻 Interactive Developer UI:** Features a seamless tabbed interface:
  - **Live Preview:** Instantly view the rendered website in an isolated sandbox.
  - **Raw Code:** Access the generated HTML/Tailwind code with a 1-click copy feature.
- **🛡️ Bulletproof Execution:** Built-in anti-reload scripting prevents nested iframe inception bugs during preview interactions.

---

## 🛠️ Tech Stack

### Frontend (Client)
- **HTML5 & Vanilla JavaScript** for lightweight DOM manipulation.
- **Tailwind CSS (via CDN)** for modern, responsive styling.
- Hosted on **GitHub Pages**.

### Backend (API)
- **Python & FastAPI** for a robust and high-speed server.
- **Google Generative AI SDK** (Gemini 3.5 Flash) for multimodal vision-to-code capabilities.
- **Pillow (PIL)** for on-the-fly image compression and preprocessing.
- Hosted on **Render** (Decoupled Architecture).

---

## ⚙️ How It Works

1. **Upload / Capture:** The user provides a sketch of the desired UI layout.
2. **Preprocessing:** The backend intercepts the image, compresses it to optimize API payload size, and constructs a strict prompt for the AI.
3. **Generation:** Gemini 3.5 Flash analyzes the visual boundaries, text, and layout, writing raw HTML and standard Tailwind classes.
4. **Rendering:** The frontend receives the response, strips any markdown formatting, and safely injects the code into the Live Preview iframe.

---

## 👨‍💻 Developed By

**Vishesh Choudhary** <br>
*B.Tech First Year (CSE - Artificial Intelligence & Machine Learning)* <br>
Passionate about building AI tools and exploring the intersection of web development and machine learning.

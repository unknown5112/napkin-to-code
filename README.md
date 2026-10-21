# 🪄 Napkin-to-Code 

> **Turn messy back-of-the-napkin UI sketches into production-ready frontend code instantly using Multimodal Vision AI.**

[![Frontend Deployed on Vercel](https://img.shields.io/badge/Frontend-Vercel-black?style=for-the-badge&logo=vercel)](https://vercel.com)
[![Backend Hosted on Render](https://img.shields.io/badge/Backend-Render-46E3B7?style=for-the-badge&logo=render)](https://render.com)
[![FastAPI](https://img.shields.io/badge/API-FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com)
[![Tailwind CSS](https://img.shields.io/badge/Styling-TailwindCSS-38B2AC?style=for-the-badge&logo=tailwind-css)](https://tailwindcss.com)

---
*Live Demo:* https://napkin-to-code.vercel.app/
## 🚀 About The Project

As developers, converting a rough paper wireframe or a whiteboard UI sketch into clean, responsive HTML/CSS code is a repetitive bottleneck. **Napkin-to-Code** solves this by bridging the gap between raw human imagination and executable code. 

Simply snap a picture of your notebook drawing, upload it, and our serverless Vision AI pipeline analyzes the layout hierarchy, inputs, buttons, and design elements to generate clean **HTML and Tailwind CSS** code with a live real-time preview.

---

## 🏗️ System Architecture & Tech Stack

This project is engineered using a modern cloud-native architecture with zero local overhead:

* **Frontend:** Vanilla JavaScript & Tailwind CSS, deployed globally via **Vercel**.
* **Backend:** Python & FastAPI, hosted on **Render** for reliable server execution.
* **AI Engine:** Google Gemini Multimodal Vision API with fine-tuned system prompting for strict UI-to-code structure translation.
* **Environment:** Developed entirely in the cloud using **GitHub Codespaces**.

---

## ⚡ How It Works (Data Flow)

1. **Capture & Upload:** The user uploads a hand-drawn interface sketch via the Vercel-hosted frontend interface.
2. **Payload Transmission:** The image is sent securely via a POST request to the FastAPI backend hosted on Render.
3. **Vision Analysis:** The backend parses the image using Multimodal AI, mapping components (buttons, cards, headers, forms).
4. **Code Generation & Response:** Clean, production-ready Tailwind markup is streamed back to the client and rendered instantly.

---

## 🎯 Future Roadmap
- [ ] Support multi-page component generation.
- [ ] Export directly to React / Vue framework components.
- [ ] User authentication & history tracking via Supabase.

---

## 👤 Author
**Vishesh Choudhary**
* 1st-Year B.Tech CSE (AI & ML) Student
* [Linkedin Profile](https://www.linkedin.com/in/vishesh-choudhary-737437441?utm_source=share_via&utm_content=profile&utm_medium=member_android)

# 🚀 MiniLink: FastAPI URL Shortener

A lightweight, high-performance URL shortener built with **FastAPI**. This project was developed as a deep-dive into backend engineering, handling data persistence, and RESTful API design.

## ✨ Features
* **Fast Redirection:** Uses HTTP 307 redirects for efficient routing.
* **JSON Persistence:** Automatically saves links to a local database so they survive server restarts.
* **Auto-Generated Keys:** Uses a randomized string generator for unique short IDs.
* **Interactive Docs:** Built-in Swagger UI documentation.

## 🛠️ Tech Stack
* **Language:** Python 3.10+
* **Framework:** FastAPI
* **Validation:** Pydantic
* **Server:** Uvicorn

## 🚀 Getting Started

1. **Clone the repo:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/fastapi-url-shortener.git](https://github.com/YOUR_USERNAME/fastapi-url-shortener.git)
   cd fastapi-url-shortener

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt

3. **Running the Server:**
    ```bash
    uvicorn main:app --reload
4. **Try it out:**
 
    Open http://127.0.0.1:8000/docs to use the interactive API explorer!
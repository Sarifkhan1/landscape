# 🌄 Living Landscapes – AI Image Generation from Text

# python3 -m venv venv

# source venv/bin/activate on windows venv\Scripts\activate

# pip freeze > requirements.txt

# python3 app.py or python app.py


**Living Landscapes** is a Flask-based web application that uses the **Stable Diffusion** model to generate AI-powered images based on natural language prompts. Users simply describe a scene, and the app generates a unique landscape image that visually represents the prompt.


## 🚀 Features

- Generate stunning images from simple text descriptions
- Built using the `stable-diffusion-v1-5` model from Hugging Face
- Optimized for both **CPU and GPU** environments (CUDA if available)
- Clean and simple web interface
- Images saved dynamically with unique filenames


## 📷 Demo

You can view the full demo video and image samples in this shared folder:  
🔗 https://drive.google.com/file/d/1X8QCraK_m1yS7XPm_ReRFNxwbMElbcEp/view?usp=sharing


## 🛠️ Technologies Used

- Python 3.x
- Flask (web framework)
- Hugging Face 🤗 `diffusers` library
- PyTorch (for model inference)
- HTML + CSS (frontend)


## 📁 Project Structure

```

Living-Landscapes/
├── static/
│   └── generated/       # Folder for storing AI-generated images
├── templates/
│   └── index.html       # Frontend layout using Jinja2 templating
├── app.py               # Main Flask app file
└── requirements.txt     # List of dependencies

````

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Sarifkhan1/landscape.git
cd landscape
````

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app locally

```bash
python app.py
```

Then open your browser and visit:
👉 `http://127.0.0.1:5000/`


## 📦 Requirements

* Python 3.7+
* PyTorch (`torch`)
* diffusers
* Flask
* accelerate
* torchvision (if needed)
* A CUDA-compatible GPU (optional but improves performance)


## 🧠 Model Used

[`runwayml/stable-diffusion-v1-5`](https://huggingface.co/runwayml/stable-diffusion-v1-5)
  Loaded via Hugging Face `diffusers` pipeline with automatic device detection (`cuda` or `cpu`).

## 📌 Notes

All images are saved in the `static/generated/` folder with unique filenames.
The app is currently designed for **local use**. Deployment on a cloud platform like Heroku or Render would require GPU support and additional configuration.
If you are running on CPU, generation might be slower.

## 📜 License

This project is for educational and non-commercial use.


## 🙌 Creator

Made with 💻 and ☕ by [Sarif Khan](https://github.com/Sarifkhan1)

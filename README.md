# Contrast Enhancement of Medical X-Ray Images 🦴

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://xrayimageprocessing.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)](https://opencv.org/)

**B.Sc. IT Field Project (2026-2027)**  
**Author:** Pondharani Devendra  
**College:** S.I.W.S. N.R. Swamy College of Commerce & Economics and Smt. Thirumalai College of Science

## 📌 Project Overview
This project presents a web-based diagnostic tool designed to improve the interpretability of medical X-ray radiographs. Medical images frequently suffer from low contrast and poor visibility. To solve this, the application applies strict spatial-domain mathematical transformations to enhance visual clarity, stretch dynamic range, and sharpen anatomical boundaries.

**Crucially, this system relies entirely on deterministic mathematical filtering rather than generative AI.** This ensures the absolute integrity of the original medical data, preventing the risk of hallucinated artifacts in clinical settings.

## ⚙️ Core Processing Pipeline
The application processes radiographs through a sequential 4-step pipeline:
1. **Histogram Equalization:** Reassigns brightness values to utilize the full dynamic range of the image.
2. **Spatial Filtering (High-Pass):** Applies discrete 2D matrix convolutions to highlight sharp frequency transitions and remove blur.
3. **Density Heatmaps:** Generates a pseudo-color representation of bone density for easier visual assessment.
4. **Laplacian Edge Detection:** Isolates strong bone cracks and borders by evaluating the second derivative of the image pixels, providing a mathematical variance score.

## 🚀 Features
* **Dual-View Analytics:** Upload a healthy baseline and a test radiograph side-by-side for direct comparison.
* **Interactive UI:** Navigate through the different stages of the image processing pipeline using a clean, dark-themed tabbed interface.
* **Variance Scoring:** Automatically calculates the structural percentage difference between the reference and diagnostic images based on edge density.

## 💻 Local Installation & Setup

To run this project locally on your machine:

**1. Clone the repository:**
```bash
git clone https://github.com/Dharani-dev22/Contrast-Enhancement-.git
cd Contrast-Enhancement-
```

**2. Install the required dependencies:**
```bash
pip install -r requirements.txt
```

**3. Run the Streamlit application:**
```bash
streamlit run filtering.py
```

## 🌐 Live Deployment
This application is fully compatible with **Streamlit Community Cloud**. 
To deploy:
1. Connect this GitHub repository to Streamlit Cloud.
2. Set the Main file path to `filtering.py`.
3. Click Deploy.

## 🛠️ Technology Stack
* **Language:** Python
* **Frontend/UI:** Streamlit (with custom CSS configurations)
* **Image Processing:** OpenCV (`opencv-python-headless`), NumPy, Pillow

---
*Developed under the guidance of Ms. Rani Mario, Department of Information Technology.*

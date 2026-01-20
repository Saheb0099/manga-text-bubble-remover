# Manga Bubble Remover 💬✂️

An automated AI tool to remove **speech bubbles, narration boxes, and floating text** from manga and webtoon pages using a **two-stage AI pipeline**.

---

## 🚀 Features

- **Two-Stage AI Cleaning**
  - Stage 1 removes speech bubbles and narration boxes
  - Stage 2 removes remaining floating text and sound effects

- **GPU Accelerated**
  - Apple Silicon (MPS)
  - NVIDIA GPUs (CUDA)

- **Batch Processing**
  - Process entire manga volumes or hundreds of chapters automatically

- **Fail-Safe Execution**
  - Pipeline stops immediately if any stage fails

---

## 📥 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Saheb0099/manga-text-bubble-remover.git
cd manga-text-bubble-remover
```

---

### 2️⃣ Install Dependencies

It is recommended to use a virtual environment.

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Download AI Models (Required)

Due to GitHub size limits, models must be downloaded separately.

**Download link:**  
https://drive.google.com/file/d/1-TvWff3aQW5uedCZr5SiZrLn6XiRIxcp/view

**Steps:**
1. Download `data.zip`
2. Extract it into the project root
3. Verify the folder structure:

```plaintext
manga-text-bubble-remover/
├── data/
│   └── models/
│       ├── adetailerForTextSpeech_v20/
│       └── yolov8m_seg-speech-bubble/
├── main.py
├── rm_speech_bubbles.py
├── rm_text.py
└── ...
```

---

## 🛠️ Usage

### 1️⃣ Prepare Input Files

Create an `input_manga` directory and place chapter folders inside it:

```plaintext
input_manga/
├── Chapter 101/
│   ├── 01.jpg
│   └── 02.jpg
└── Chapter 102/
    └── ...
```

---

### 2️⃣ Run the Pipeline

```bash
python main.py
```

---

### 3️⃣ Output

- `temp_stage1/` — Intermediate results (bubbles removed, text remains)
- `output_manga/` — ✅ Final cleaned images

---

## ⚙️ Pipeline Overview

| Stage | Script | Model | Description |
|------|-------|------|-------------|
| **1** | `rm_speech_bubbles.py` | Shapes Model | Aggressively removes speech bubbles and narration boxes using a low threshold (0.05). |
| **2** | `rm_text.py` | Text Model | Removes remaining floating English text and sound effects using a stricter threshold (0.2). |

---

## 🔧 Configuration

Adjust AI sensitivity in `main.py`:

```python
# Stage 1 - Speech Bubbles
STAGE_1_THRESHOLD = 0.05  # Lower = more aggressive

# Stage 2 - Text
STAGE_2_THRESHOLD = 0.2   # Higher = stricter text detection
```

---

## 🙏 Credits & Acknowledgements

This project is built upon:

- **speech_bubble_remove_and_copy**  
  https://github.com/s9roll7/speech_bubble_remove_and_copy  
  By **s9roll7** — core bubble detection and inpainting logic

---

## 📝 License

This project is licensed under the **MIT License**.

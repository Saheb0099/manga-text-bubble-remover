
# Manga Bubble Remover 💬✂️

An automated AI tool to remove speech bubbles, narration boxes, and floating text from manga and webtoon pages.

This tool uses a **Two-Stage Pipeline** to ensure high-quality cleaning:

1. **Stage 1 (Heavy Lifter):** Removes solid speech bubbles and square narration boxes.
2. **Stage 2 (Detailer):** Hunts down and removes leftover floating text and sound effects.

## 🚀 Features

* **Two-Stage Cleaning:** Separates bubble removal from text removal for maximum precision.
* **GPU Accelerated:** Optimized for Mac Silicon (MPS) and NVIDIA (CUDA) for fast processing.
* **Batch Processing:** Can process hundreds of chapters automatically.
* **Fail-Safe:** Automatically stops if a stage fails to prevent data corruption.

## 📥 Installation

### 1. Clone the repository
```bash
git clone [https://github.com/Saheb0099/manga-text-bubble-remover.git](https://github.com/Saheb0099/manga-text-bubble-remover.git)
cd manga-text-bubble-remover

```

### 2. Set up the Environment (Recommended)

It is highly recommended to use a virtual environment (`venv`) to avoid conflicts.

**For Mac / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate

```

**For Windows:**

```bash
py -3.10 -m venv venv
venv\Scripts\activate

```

### 3. Install PyTorch

You must install the correct version of PyTorch for your hardware (NVIDIA CUDA or Mac MPS) **before** installing other dependencies.

* **Visit the official guide:** [https://pytorch.org/get-started/locally/](https://pytorch.org/get-started/locally/)
* **Or use one of these common commands:**
* **For Mac (M1/M2/M3 Chips):**
```bash
pip install torch torchvision torchaudio

```


* **For Windows (NVIDIA GPU - CUDA 12.1):**
```bash
pip install torch torchvision torchaudio --index-url [https://download.pytorch.org/whl/cu121](https://download.pytorch.org/whl/cu121)

```


* **For CPU Only (Slow):**
```bash
pip install torch torchvision torchaudio

```





### 4. Install Dependencies

Once PyTorch is installed, install the rest of the required libraries:

```bash
pip install -r requirements.txt

```

### 5. ⬇️ Download the AI Models (REQUIRED)

The model files are too large for GitHub, so they must be downloaded separately.

> **[Download the `data.zip` file here](https://drive.google.com/file/d/1-TvWff3aQW5uedCZr5SiZrLn6XiRIxcp/view?usp=sharing)**

* Download the zip file.
* Extract it inside the project folder.
* Your folder structure must look **exactly** like this:
```text
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



## 🛠️ Usage

### 1. Prepare your files

Create a folder named `input_manga` and place your chapter folders inside it:

```text
input_manga/
├── Chapter 101/
│   ├── 01.jpg
│   └── 02.jpg
└── Chapter 102/
    └── ...

```

### 2. Run the tool

Run the master script to start the pipeline:

```bash
python main.py

```

### 3. Get results

The tool will create two folders:

* `temp_stage1/`: Intermediate files (Bubbles removed, text remains).
* `output_manga/`: **Final Results** (Clean images).

## ⚙️ How It Works (The Pipeline)

This tool runs two distinct scripts in sequence:

| Stage | Script | Model Used | Goal |
| --- | --- | --- | --- |
| **1** | `rm_speech_bubbles.py` | **Model 0** (Shapes) | Aggressively removes white shapes, speech bubbles, and square narration boxes. Uses a low detection threshold (0.05) to catch boxes hidden in speed lines. |
| **2** | `rm_text.py` | **Model 1** (Text) | Scans the cleaned images from Stage 1 and removes any remaining floating English text or sound effects using a standard threshold (0.2). |

## 🔧 Configuration

You can adjust the sensitivity of the AI by editing the settings at the top of `main.py`:

```python
# STAGE 1 (Bubbles)
STAGE_1_THRESHOLD = 0.05  # Lower = More aggressive (removes more boxes)

# STAGE 2 (Text)
STAGE_2_THRESHOLD = 0.2   # Higher = stricter (only removes obvious text)

```

## 🙏 Credits & Acknowledgements

This project is built upon the amazing work from:

* **[speech_bubble_remove_and_copy](https://github.com/s9roll7/speech_bubble_remove_and_copy)** by **s9roll7** - Used for the core bubble detection and inpainting logic.

## 📝 License

[MIT License](https://www.google.com/search?q=LICENSE)

```


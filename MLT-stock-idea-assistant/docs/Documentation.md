# ![MLT Logo](https://github.com/user-attachments/assets/f322d9cc-1adf-45d4-a38d-4764f62cf7bd) MLT Stock Image Automation Assistant

## Documentation & Usage Guide

**MLT Stock Image Assistant** is a Windows GUI tool designed to streamline the entire process of AI-based stock image generation, tagging, and publishing to stock sites such as Dreamstime. Built for creators and coders, it combines **Ollama**, **ComfyUI**, and **Python automation** under one user-friendly interface.

--- 

## 🔗 Quick Links
- [🏠 Home](../README.md)
- [📚 Documentation](Documentation.md)
- [🛠 Installation Guide](INSTALLATION_GUIDE.md)
- [👀 Sample Outcome](../sample/sample.md)

---

## 🚀 Usage Sequence & Button Guide

![App Screenshot](https://github.com/user-attachments/assets/d4e3e899-8e4c-452b-8500-ac7715d274be)

---

## 🧠 Feature Highlights

- **Prompt Generation with Ollama LLM (e.g., Mistral)**
  - Automatically creates 10 high-quality prompts using a local language model
  - Clean format with `Title`, `Description`, and `Keywords` (new lines for each)

- **Flattened Prompt Conversion**
  - Converts prompts into single-line ComfyUI-compatible format for batch processing

- **One-click ComfyUI Launch**
  - Launches ComfyUI and waits until the API is ready

- **Automated Image Generation**
  - Queues jobs into ComfyUI using SDXL workflow
  - Randomizes model seed
  - Uses: `sd_xl_base_1.0.safetensors`, `sd_xl_refiner_1.0.safetensors`, `dpmpp_2m_sde_gpu`, `karras`, `RealESRGAN_x4plus.pth`

- **Image Completion Wait Logic**
  - Waits for expected number of JPGs to be generated before proceeding

- **Metadata Embedding + CSV Creation**
  - Injects Title, Description, Keywords into JPG IPTC metadata
  - Generates Adobe Stock-compatible CSV

- **Output Management**
  - Sorts JPG and PNG files into timestamped folders (`YYYYMMDDHHMM`)
  - Ensures no overwrite of previous batches

- **FTP Upload (optional)**
  - Uploads latest image batch via FTP to a stock site
  - LATEST = most recent `timestamped folder`

---

## 📘 How to Use + Tips

### 1. Generate Prompt
- Enter theme/idea into the **"Prompt Theme"** box
- Built-in negative prompts avoid malformed hands, limbs, or NSFW content

### 2. Open Prompt
- You may paste prompts from other tools
- Format must be in 3 lines format without bullet points:
  - Title:
  - Description:
  - Keywords:
- Paste the prompt twice (PRO) for more image variety
- This is the source for embedding metadata into JPGs

### 3. Flatten Prompt
- Converts prompts to single-line format for ComfyUI
- **No prompt limit in PRO version**

### 4. Generate Image
- Token errors (`>77`) in ComfyUI are expected and safe to ignore
- If a JPG metadata mapping fails, the next ones will still work

### 5. Open JPG Folder
- Output folders use timestamp format `YYYYMMDDHHMM`
- JPGs are separated and upscaled with `RealESRGAN_x4plus.pth` to ensure size ≥ 3MB for 1344 x 768 & 768 x 1344.
- **Important:** Manually delete any low-quality images before uploading
- CSV file is generated with Title/Keywords ready for Adobe Stock—even if some images are deleted

### 6. Upload via FTP
- Set FTP URL, username, and password in the app
- Only JPGs in the **latest timestamped folder** will be uploaded
- After upload, visit the site to confirm tags/descriptions, then submit

### 7. Tips
- If generation is slow, check if **Ollama** is using GPU—terminate via Task Manager
- For big batches, **restart your PC** before starting
- If restarting midway, **exit and relaunch the app** to reset queue tracking

### 8. Known Issues
- If the **last image (e.g., #100)** has broken metadata, it might’ve skipped a line
- **Solutions:**
- 🛠 **Manual:** Use an EXIF viewer (e.g., **XnView MP**) to check for the skipped image
- ⚠️ **Avoid:** Generate smaller batches (e.g., 50 instead of 100)
- ⚠️ DecompressionBombWarning
```
DecompressionBombWarning: Image size (103219200 pixels) exceeds limit of 89478485 pixels, could be decompression bomb DOS attack.
```
🔍 What It Means:
- Your image is very large: 103,219,200 pixels (e.g., 12,000 × 8,600).
- Pillow sets a default limit of 89,478,485 pixels to prevent denial-of-service (DOS) attacks from opening maliciously large files that consume too much memory.




---


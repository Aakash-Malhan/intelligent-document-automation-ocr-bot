# intelligent-document-automation-ocr-bot
Lightweight OCR + PDF pipeline (pypdfium2 + Tesseract + pdfplumber) with a Gradio UI. Extracts Invoice #, Date, Total/Amount Due, and basic tables. Includes sample PDFs.

A lightweight OCR pipeline + Gradio UI that extracts **key fields** and **tables** from PDFs or images:

<img width="1500" height="890" alt="Screenshot 2025-10-18 161738" src="https://github.com/user-attachments/assets/a9132208-bdf3-480b-9795-ecd13c306dd6" />
<img width="1900" height="849" alt="Screenshot 2025-10-18 161803" src="https://github.com/user-attachments/assets/1448faf4-803b-47b5-a01c-59b0766b306f" />


- Uses `pdfplumber` for native PDF text & tables.
- Falls back to OCR on scanned docs (OpenCV + Tesseract).
- PDF rasterization via `pypdfium2` (no Poppler dependency).
- Simple regex rules to pull: **Invoice #**, **Date**, **Total/Amount Due**.
- Pydantic models for clean JSON output.
- Optional built-in **sample PDFs** in `samples/` and a **Load sample** dropdown.

---

## Demo : https://huggingface.co/spaces/aakash-malhan/ocr-bot

If you deploy to Hugging Face Spaces, add a `packages.txt` file with:

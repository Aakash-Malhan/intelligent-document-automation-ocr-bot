import os, json, traceback, glob
import gradio as gr
from src.pipeline import process_document

SAMPLES_DIR = "samples"  # optional folder with example PDFs

def run(file_path: str):
    """Run extraction for a user-uploaded file path."""
    if not file_path:
        return "Upload a PDF or image."
    try:
        with open(file_path, "rb") as f:
            b = f.read()
        filename = os.path.basename(file_path)
        out = process_document(b, filename)
        return json.dumps(out, indent=2)
    except Exception:
        return "ERROR:\n" + traceback.format_exc()

def list_samples():
    """Return list of sample PDFs in the samples/ dir (sorted)."""
    if not os.path.isdir(SAMPLES_DIR):
        return []
    files = sorted(os.path.basename(p) for p in glob.glob(os.path.join(SAMPLES_DIR, "*.pdf")))
    return files

def run_sample(sample_name: str):
    """Run extraction on a built-in sample from samples/."""
    if not sample_name:
        return "Pick a sample."
    path = os.path.join(SAMPLES_DIR, sample_name)
    if not os.path.exists(path):
        return f"Sample not found: {path}"
    return run(path)

with gr.Blocks(title="OCR Bot - Intelligent Document Automation") as demo:
    gr.Markdown("# 📄 OCR Bot\nUpload a PDF or image (invoice/receipt), or try a sample.")
    with gr.Row():
        with gr.Column(scale=2):
            inp = gr.File(
                label="Upload PDF or Image",
                file_types=[".pdf", ".png", ".jpg", ".jpeg"],
                type="filepath",  # important: returns a filepath (not a NamedString)
            )
            btn = gr.Button("Extract", variant="primary")
        with gr.Column(scale=1):
            samples = gr.Dropdown(
                choices=list_samples(),
                label="Try a built-in sample",
                interactive=True,
                info="Files come from the samples/ folder in the repo.",
            )
            sample_btn = gr.Button("Run sample")

    out = gr.Code(label="Structured JSON / Errors", language="json")

    btn.click(run, inputs=inp, outputs=out)
    sample_btn.click(run_sample, inputs=samples, outputs=out)

if __name__ == "__main__":
    demo.queue().launch()

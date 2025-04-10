import streamlit as st
import fitz  # PyMuPDF
import os
from tempfile import NamedTemporaryFile

def add_coordinates_to_pdf(uploaded_pdf):
    input_file = NamedTemporaryFile(delete=False, suffix=".pdf")
    input_file.write(uploaded_pdf.read())
    input_file.close()

    doc = fitz.open(input_file.name)
    for page in doc:
        width, height = page.rect.width, page.rect.height

        for x in range(0, int(width), 20):
            page.draw_line((x, 0), (x, height), color=(0.8, 0.8, 0.8))
            page.insert_text((x+1, 5), str(x), fontsize=6, color=(0.3, 0.3, 0.3))

        for y in range(0, int(height), 20):
            page.draw_line((0, y), (width, y), color=(0.8, 0.8, 0.8))
            page.insert_text((2, y+2), str(y), fontsize=6, color=(0.3, 0.3, 0.3))

    output_path = input_file.name.replace(".pdf", "_grid.pdf")
    doc.save(output_path)
    return output_path

st.title("🧭 PDF Coordinate Grid Generator")
st.write("Upload a PDF template and download the version with coordinate lines for design reference.")

uploaded_pdf = st.file_uploader("Upload your PDF", type="pdf")

if uploaded_pdf is not None:
    if st.button("Generate PDF with Grid"):
        output_path = add_coordinates_to_pdf(uploaded_pdf)
        with open(output_path, "rb") as f:
            st.download_button("📥 Download Grid PDF", f, file_name="grid_template.pdf")

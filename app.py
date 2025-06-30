import streamlit as st
import tempfile
import os
from utils import process_pdf, process_docx
from PIL import Image

st.set_page_config(page_title="Docubrand", layout="centered")
st.title("📄 Docubrand - Brand Your Documents Easily")

st.markdown("Add header and/or footer images to your PDF or Word documents. Download the result as PDF or DOCX.")

# Ensure folders exist
os.makedirs("branding/headers", exist_ok=True)
os.makedirs("branding/footers", exist_ok=True)

def list_images(folder):
    return [f for f in os.listdir(folder) if f.lower().endswith((".png", ".jpg", ".jpeg"))]

def save_uploaded_image(file, folder):
    path = os.path.join(folder, file.name)
    with open(path, "wb") as f:
        f.write(file.read())
    return path

# Upload file
uploaded_file = st.file_uploader("📤 Upload your PDF or DOCX file", type=["pdf", "docx"])

# Header Image
st.subheader("🖼️ Header Image (Logo)")
header_images = list_images("branding/headers")
selected_header = st.selectbox("Choose a previously uploaded header (optional):", ["None"] + header_images)
new_logo_file = st.file_uploader("Or upload a new header image", type=["png", "jpg", "jpeg"])
logo_path = None
if new_logo_file:
    logo_path = save_uploaded_image(new_logo_file, "branding/headers")
elif selected_header != "None":
    logo_path = os.path.join("branding/headers", selected_header)
    st.image(logo_path, width=150, caption="Selected Header")

# Footer Image
st.subheader("🏢 Footer Image (Address/Footer)")
footer_images = list_images("branding/footers")
selected_footer = st.selectbox("Choose a previously uploaded footer (optional):", ["None"] + footer_images)
new_footer_file = st.file_uploader("Or upload a new footer image", type=["png", "jpg", "jpeg"])
footer_path = None
if new_footer_file:
    footer_path = save_uploaded_image(new_footer_file, "branding/footers")
elif selected_footer != "None":
    footer_path = os.path.join("branding/footers", selected_footer)
    st.image(footer_path, width=150, caption="Selected Footer")

# File Type
file_type = uploaded_file.name.split(".")[-1].upper() if uploaded_file else None
split_option = st.checkbox("📑 Split PDF into individual pages (PDF only)", value=False) if file_type == "PDF" else False
output_format = st.radio("Choose output format", ["PDF", "DOCX"])

# iLovePDF Modal/Helper
# ⛔ PDF uploaded but user selects DOCX – warn and show helpful modal
if uploaded_file and file_type == "pdf" and output_format == "DOCX":
    st.warning("⚠️ You've uploaded a PDF but selected 'DOCX' as output. Convert the PDF to Word to proceed.")

    with st.container():
        st.markdown(
            """
            <style>
            .modal-box {
                background-color: #f9f9f9;
                border: 2px solid #e0e0e0;
                padding: 1.5rem;
                border-radius: 12px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
                margin-top: 1rem;
            }
            .modal-header {
                font-size: 20px;
                font-weight: 600;
                margin-bottom: 10px;
                color: #1a1a1a;
            }
            .modal-button {
                background-color: #008CBA;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 6px;
                cursor: pointer;
                font-size: 16px;
            }
            .modal-button:hover {
                background-color: #0072a5;
            }
            </style>

            <div class="modal-box">
                <div class="modal-header">🔄 Convert PDF to Word (DOCX)</div>
                <p>To proceed with adding branding to a Word document, you need to convert your PDF to a DOCX file.</p>
                <ul>
                    <li>Click the button below to visit iLovePDF.</li>
                    <li>Convert and download your DOCX file.</li>
                    <li>Re-upload it here and continue the process.</li>
                </ul>
                <br>
                <button class="modal-button" onclick="window.open('https://www.ilovepdf.com/pdf_to_word', '_blank')">🌐 Go to iLovePDF</button>
            </div>
            """,
            unsafe_allow_html=True
        )


# Process File
if st.button("🚀 Process File"):
    if uploaded_file:
        with tempfile.NamedTemporaryFile(delete=False, suffix=f".{uploaded_file.name.split('.')[-1]}") as temp_input:
            temp_input.write(uploaded_file.read())
            input_path = temp_input.name

        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_output:
            output_path = temp_output.name

        if file_type == "PDF":
            process_pdf(input_path, logo_path, footer_path, output_path, split_pages=split_option)
            with open(output_path, "rb") as f:
                if output_format == "PDF":
                    st.success("✅ Done! Download your processed PDF:")
                    st.download_button("📥 Download PDF", data=f, file_name="processed_output.pdf")
                else:
                    st.warning("⚠️ PDF to DOCX conversion is not supported locally. Use iLovePDF above.")
        else:
            docx_path, pdf_path = process_docx(input_path, logo_path, footer_path, output_path, split_pages=split_option)
            if output_format == "PDF":
                with open(pdf_path, "rb") as f:
                    st.success("✅ Done! Download your processed PDF:")
                    st.download_button("📥 Download PDF", data=f, file_name="processed_output.pdf")
            else:
                with open(docx_path, "rb") as f:
                    st.success("✅ Done! Download your processed DOCX:")
                    st.download_button("📥 Download DOCX", data=f, file_name="processed_output.docx")

        if file_type == "PDF" and split_option:
            st.markdown("📄 Individual Split Pages:")
            split_dir = "split_pages"
            for filename in sorted(os.listdir(split_dir)):
                page_path = os.path.join(split_dir, filename)
                with open(page_path, "rb") as p:
                    st.download_button(f"⬇️ {filename}", data=p, file_name=filename)
    else:
        st.error("❗ Please upload a file to proceed.")

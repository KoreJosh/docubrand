# Docubrand

# 📄 Docubrand – Brand Your Documents with Ease

**Docubrand** is a lightweight Streamlit-based app that allows users to add branded headers and footers (e.g., logos and addresses) to PDF or DOCX documents, with the option to download them in PDF or DOCX format. Whether you’re creating professional reports, invoices, or school projects, Docubrand helps you maintain a consistent and branded look.

---

## 🚀 Features

| Feature                         | Description                                                                 |
|----------------------------------|-----------------------------------------------------------------------------|
| 📤 **Upload Support**            | Accepts **PDF** and **DOCX** files for branding                            |
| 🖼️ **Header & Footer Branding**  | Add a **logo at the top** (header) and an **address/footer image**         |
| 🗂️ **Image Reuse**               | Previously uploaded branding images are **stored and selectable**          |
| 📄 **Output Format Choice**      | Choose between **PDF** and **DOCX** as output format                       |
| ✂️ **Split PDF Option**          | Split PDFs into **individual branded pages**                               |
| 🔄 **PDF ➡️ DOCX Shortcut**       | Integrated link to **iLovePDF** for PDF-to-Word conversion                 |
| 🧠 **Flexible Branding**         | Add either header, footer, or both based on need                          |
| ✅ **Preview & Download**        | Instantly download the processed, branded file                            |
| 🧠 **Stateful Uploads**          | Retains uploaded headers/footers for reuse across sessions                |

---

## 🧭 How It Works

1. **Upload your file** (PDF or DOCX)
2. **Upload/select** a header and/or footer image
3. **Choose output format** (PDF or DOCX)
4. **Click Process** to apply branding
5. **Download** the final document

✅ Optional: Split PDFs into individually branded pages

---

## 🔄 PDF to Word Conversion

If you upload a PDF but want to apply branding as a Word document, we provide a quick shortcut:

> 📎 Click the "Open iLovePDF PDF to Word Converter" button to convert before branding.

[🔗 iLovePDF PDF to Word](https://www.ilovepdf.com/pdf_to_word)

---

## 🛠️ Tech Stack

- **Frontend:** [Streamlit](https://streamlit.io)
- **Image Processing:** Pillow (PIL)
- **Document Handling:** python-docx, PyPDF2, reportlab
- **File Management:** tempfile, os

---

## 📁 Folder Structure

Docubrand/
├── app.py
├── utils.py
├── branding/
│ ├── headers/
│ └── footers/
├── split_pages/
└── README.md

📌 Notes
🧠 Header and footer uploads are stored in the branding/ folder and remain accessible for reuse.

🧾 For now, PDF to DOCX conversion must be done via iLovePDF before uploading.



from flask import Flask, render_template, request, redirect, url_for, flash
from PyPDF2 import PdfReader

app = Flask(__name__)
app.config['SECRET_KEY'] = 'add-secret-key-here'


file = ""

def get_pdf_text(pdf_file):
    reader = PdfReader(pdf_file)
    number_of_pages = len(reader.pages)
    print(number_of_pages)
    all_text = ""
    for page_no in range(0, number_of_pages):
        page = reader.pages[page_no]
        text = page.extract_text()
        all_text += text
    return all_text


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
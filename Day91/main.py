from flask import Flask, render_template, request, redirect, url_for, flash, redirect, url_for,\
    session, send_file
from PyPDF2 import PdfReader
from gtts import gTTS
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'add-secret-key-here'
app.config['UPLOAD_FOLDER'] = 'uploads'

file = ""

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def get_file():
    if request.method == 'POST':
        # Save the file to the upload folder
        file = request.files['filename']
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        # Store the file path in the session
        session['file_path'] = file_path
        flash("File uploaded successfully")
        return redirect(url_for('get_pdf_text'))
    
    return render_template("index.html")



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


def convert_and_save_audio(file):
    pdf_text = get_pdf_text(file)
    print(pdf_text)
    text_to_speech = gTTS(pdf_text)
    text_to_speech.save(f'{pdf_text}.mp3')

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
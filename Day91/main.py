from flask import Flask, render_template, request, redirect, url_for, flash, redirect, url_for,\
    session, send_file
from PyPDF2 import PdfReader
from gtts import gTTS
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'add-secret-key-here'
app.config['UPLOAD_FOLDER'] = 'uploads'


# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def home():
    audio_file_path = request.args.get('filename', '')
    if request.method == 'POST':
        file = request.files['filename']
        if file:
            # Ensure the upload folder exists before saving the file
            os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            session['file_path'] = file_path
            text_to_convert = extract_text_from_pdf(file_path)
            session['text_to_convert'] = text_to_convert
            flash("File uploaded and text extracted successfully")
            return render_template("index.html",
                                   text_to_convert=text_to_convert,
                                   audio_file_path=audio_file_path)  # CHANGED
    return render_template("index.html",
                           text_to_convert=session.get('text_to_convert', ''),
                           audio_file_path=audio_file_path)



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


@app.route("/audio/<filename>")
def get_audio(filename):
    return send_file(
       filename,
       mimetype="audio/mpeg",
       as_attachment=False
    )


if __name__ == '__main__':
    app.run(debug=True)
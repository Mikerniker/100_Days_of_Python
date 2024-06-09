from flask import Flask, render_template, request, redirect, url_for
from PIL import Image
import pandas as pd
import os

app = Flask(__name__)

# Ensure the upload directory exists
UPLOAD_FOLDER = './static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'add-secret-key-here'


def get_RGB(image_path, colors):
    img = Image.open(image_path)
    convert_palette = img.convert("P", palette=Image.Palette.WEB)
    palette = convert_palette.getpalette()  #get rgb
    palette = [palette[3*n:3*n+3] for n in range(256)]
    color_count = [(n, palette[m]) for n, m in convert_palette.getcolors()]

    # Convert to a dataframe and get 10 most common
    rgb_df = pd.DataFrame(color_count, columns=['count', "RGB"]).sort_values(by="count", ascending=False).iloc[0:colors]
   
    # Convert df to RGB
    RGB = pd.DataFrame(rgb_df['RGB'].to_list(), columns=['r', 'g', 'b'])
    RGB['Total'] = RGB.r + RGB.g + RGB.b
    RGB = RGB.sort_values(by=["Total"]).drop(['Total'], axis=1).reset_index().drop("index", axis=1)
   
    return RGB


def rgb_to_hex(red, green, blue):
   return f"#{red:02x}{green:02x}{blue:02x}"


def get_hex_list(image_path, colors):
    RGB = get_RGB(image_path, colors)
    RGB['hex'] = RGB.apply(lambda r: rgb_to_hex(*r), axis=1)
    color = RGB.hex.to_list()
    return color


@app.route("/", methods=["GET"])
def home():
    img = "./static/assets/images/foodplatter.jpg"
    colors = 10
    image_colors = get_hex_list(img, colors)
    return render_template("index.html", user_image=img, colors=image_colors)


@app.route("/upload", methods=["POST"])
def display_colors():
    if request.method == "POST":
        file = request.files['filename']
        color_num = int(request.form['color_number'])
        try:
            if file:
                filename = file.filename
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                img_path = f"./static/uploads/{filename}"
                image_colors = get_hex_list(filepath, color_num)
                print(f"Uploaded file: {filename}, Number of colors: {color_num}")
                return render_template("index.html", user_image=img_path, colors=image_colors)
        except Exception as e:
            print(f"Error: {e}")
            return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
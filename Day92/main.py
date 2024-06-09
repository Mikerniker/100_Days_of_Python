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

def get_RGB():
    img = Image.open(r"./static/assets/images/foodplatter.jpg")
    convert_palette = img.convert("P", palette=Image.Palette.WEB)
    palette = convert_palette.getpalette()   #get rgb
    palette = [palette[3*n:3*n+3] for n in range(256)]
    color_count = [(n, palette[m]) for n, m in convert_palette.getcolors()]

    # Convert to a dataframe and get 10 most common
    rgb_df = pd.DataFrame(color_count, columns=['count', "RGB"]).sort_values(by="count", ascending=False).iloc[0:10]
    print(rgb_df)

    # Convert df to RGB
    RGB = pd.DataFrame(rgb_df['RGB'].to_list(), columns=['r', 'g', 'b'])
    RGB['Total'] = RGB.r + RGB.g + RGB.b
    RGB = RGB.sort_values(by=["Total"]).drop(['Total'], axis=1).reset_index().drop("index", axis=1)
    print(f"RGB: {RGB}")
    return RGB


def rgb_to_hex(red, green, blue):
   return "#%02x%02x%02x" %(red, green, blue)



@app.route("/", methods=["GET", "POST"])
def home():
    # image_colors = get_rgb_final()
    return render_template("index.html", colors=image_colors)


if __name__ == '__main__':
    app.run(debug=True)
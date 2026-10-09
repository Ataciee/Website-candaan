# save this as app.py
from flask import Flask

app = Flask(__name__)

@app.route("/halaman")
def tentang():
    web_title = "Khusus Rangga"
    return f"<p>INI HALAMAN {web_title}</p><br/><a href='/tentang'>masuk ke tentang halaman yagesya</a>"

@app.route("/tentang")
def halaman():
    return "<p>RANGGA KARBITTT</p><br/><a href='/halaman'>balik ke halaman</a>"

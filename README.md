# Website-candaan
RANGGA KARBITTTT

@app.route("/")
def tentang():
    web_title = "Khusus Rangga"
    return f"<p>INI HALAMAN {web_title}</p><br/><a href='/tentang'>masuk ke tentang halaman yagesya</a>"

@app.route("/tentang")
def halaman():
    return "<p>RANGGA KARBITTT</p><br/><a href='/'>balik ke halaman</a>"

ODETTE PUNYA GUEEEEEE

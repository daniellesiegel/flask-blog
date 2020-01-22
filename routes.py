from app import app

#home page
@app.route("/")
def home():
    return "<h1>I made a website!!!!!</h1>"

@app.route("/imsocoolbecauseimadeawebsite")
def about():
    return "<h1>About Me: I Made a Website</h1> <br> Hello everyone I made this website I am very cool"
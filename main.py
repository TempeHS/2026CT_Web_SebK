from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/index.html')
@app.route('/')
def index():
    card_data = (
        ("Golden Cookie Combos", "How to use golden cookies together", "combos.html", "static/images/cardimg1.png"),
        ("Best Krumblor Abilites", "How to train your cookie dragon", "krumblor.html", "static/images/cardimg2.png"),
        ("Minigame Guide", "How to maximise your minigame game", "minigames.html", "static/images/cardimg3.png"),
        ("Early Game Guide", "How to start cookie clicker", "earlygame.html", "static/images/early.jpg"),
        ("Mid Game Guide", "How to keep it going", "midgame.html", "static/images/mid.png"),
        ("Late Game Guide", "How to make the number even bigger", "lategame.html", "static/images/late.webp"),
    )

    return render_template("index.html", cards=card_data), 200

@app.route('/contact.html')
def contact():
    return render_template("contact.html"), 200

@app.route('/glossary.html')
def glossary():
    return render_template("glossary.html"), 200

@app.route('/earlygame.html')
def earlygame():
    return render_template("earlygame.html"), 200

@app.route('/midgame.html')
def midgame():
    return render_template("midgame.html"), 200

@app.route('/lategame.html')
def lategame():
    return render_template("lategame.html"), 200

@app.route('/minigames.html')
def minigames():
    return render_template("minigames.html"), 200

@app.route('/krumblor.html')
def krumblor():
    return render_template("krumblor.html"), 200

@app.route('/combos.html')
def combos():
    return render_template("combos.html"), 200

if __name__ == '__main__':
    app.run(debug=True)
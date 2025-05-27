from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/index.html')
@app.route('/')
def index():
    card_data = (
        ("Golden Cookie Combos", "How to use golden cookies together", "webpage", "static/images/cardimg1.png"),
        ("Best Krumblor Abilites", "How to train your cookie dragon", "webpage", "static/images/cardimg2.png"),
        ("Minigame Guide", "How to maximise your minigame game", "webpage", "static/images/cardimg3.png"),
        ("Minigame Guide2", "How to maximise your minigame game", "webpage", "static/images/cardimg3.png"),
        ("Minigame Guide3", "How to maximise your minigame game", "webpage", "static/images/cardimg3.png"),
        ("Minigame Guide4", "How to maximise your minigame game", "webpage", "static/images/cardimg3.png"),
    )

    return render_template("index.html", cards=card_data), 200

if __name__ == '__main__':
    app.run(debug=True)
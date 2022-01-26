from flask import Flask, request, render_template
# from flask_debugtoolbar import DebugToolbarExtension
from stories import stories

app = Flask("__name__")
# app.config['SECRET_KEY']="123"
# debug = DebugToolbarExtension(app)

@app.route("/")
def home():
    return render_template("home.html", stories=stories)

@app.route("/story_form")
def story_template():
    id = request.args.get("select-template")
    for story in stories:
        if story.id == id:
            p = story.prompts
            t = story.title
    return render_template("story_form.html", storyId=id, title=t, prompts = p)

@app.route("/story")
def show_story():
    id = request.args.get("storyId")
    for story in stories:
        if story.id == id:
            s = story
    answers = request.args
    text = s.generate(answers)
    
    return render_template("story.html", content=text)
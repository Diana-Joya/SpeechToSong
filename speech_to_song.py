from flask import Flask, redirect, url_for, render_template, request, session
from IntegrateAPIs import genius_request, spotify_request, authenticate_genius, authenticate_spotify
from speech_to_text import speech_to_text
from get_voice_command import get_voice_command

app = Flask(__name__, template_folder='templates')
app.secret_key = "S2Stestkey"
genius_token, base_url = authenticate_genius()
sp_token = authenticate_spotify()


@app.route("/", methods=["POST", "GET"])
def home():
    error = 'Sorry, I couldn\'t understand that! Please try again.'
    if request.method == "POST":
        if "record" in request.form:
            filename = get_voice_command()
            voice_command = speech_to_text(filename)
            if voice_command == 'error':
                print('error')
                return render_template("index.html", error=error)
            else:
                session["query"] = voice_command
                return render_template("index.html", voice_command=voice_command, error=None)

        elif "search" in request.form:
            return redirect(url_for("results"))

        elif "try-again" in request.form:
            return redirect(url_for("home"))
    else:
        return render_template("index.html")


@app.route("/results-page", methods=["POST", "GET"])
def results():
    if request.method == "POST":
        if "try-again" in request.form:
            return redirect(url_for("home"))
    if "query" in session:
        q = session["query"]
        artist, song = genius_request(query=q, access_token=genius_token, base_url=base_url)
        track = spotify_request(artist=artist, song_title=song, token=sp_token)
        print(artist, song, track)
        return render_template("results.html", artist=artist, song=song, track=track)
    else:
        return redirect(url_for("home"))


@app.route("/clear-session")
def clear():
    session.pop("query", None)
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request, jsonify, make_response
import requests
import json
import sys
from werkzeug.exceptions import NotFound

app = Flask(__name__)

PORT = 3200
HOST = '0.0.0.0'

moviesImdb = requests.get('https://imdb-api.com/API/Top250Movies/k_oz7jxxdv').json()["items"]
movies = []
for movie in moviesImdb:
    movies.append({
      "title": movie["title"],
      "rating": float(movie["imDbRating"]),
      "director": movie["crew"],
      "id": movie["id"]
    })

# root message
@app.route("/", methods=['GET'])
def home():
    return make_response("<h1 style='color:blue'>Welcome to the Movie service!</h1>",200)

@app.route("/template", methods=['GET'])
def template():
    return make_response(render_template("index.html", body_text='This is my HTML template for Movie service'),200)

@app.route("/json", methods=['GET'])
def get_json():
    res = make_response(jsonify(movies), 200)
    return res

@app.route("/movies/<movieid>", methods=['GET'])
def get_movie_byid(movieid):
    for movie in movies:
        if str(movie["id"]) == str(movieid):
            res = make_response(jsonify(movie),200)
            return res
    return make_response(jsonify({"error":"Movie ID not found"}),400)

@app.route("/moviesbytitle", methods=['GET'])
def get_movie_bytitle():
    json = ""
    if request.args:
        req = request.args
        for movie in movies:
            if str(movie["title"]) == str(req["title"]):
                json = movie

    if not json:
        res = make_response(jsonify({"error":"movie title not found"}),400)
    else:
        res = make_response(jsonify(json),200)
    return res

@app.route("/movies/<movieid>", methods=['POST'])
def create_movie(movieid):
    req = request.get_json()

    for movie in movies:
        if str(movie["id"]) == str(movieid):
            return make_response(jsonify({"error":"movie ID already exists"}),409)

    req["id"] = movieid
    movies.append(req)
    res = make_response(jsonify({"message":"movie added"}),200)
    return res

@app.route("/movies/<movieid>", methods=['PUT'])
def update_movie_rating(movieid):
    if request.args and int(request.args["rate"]):
        for movie in movies:
            if str(movie["id"]) == str(movieid):
                movie["rating"] = int(request.args["rate"])
                res = make_response(jsonify(movie),200)
                return res
        return make_response(jsonify({"error":"movie ID not found"}),400)

    return make_response(jsonify({"error":"QueryParam rate is requiered"}),400)

@app.route("/movies/<movieid>", methods=['DELETE'])
def del_movie(movieid):
    for movie in movies:
        if str(movie["id"]) == str(movieid):
            movies.remove(movie)
            return make_response(jsonify(movie),200)

    res = make_response(jsonify({"error":"movie ID not found"}),400)
    return res

@app.route("/moviesbydirector", methods=['GET'])
def get_movies_bydirector():
    json = []
    if request.args:
        req = request.args
        for movie in movies:
            if str(movie["director"]) == str(req["director"]):
                json.append(movie)

    if len(json) == 0:
        res = make_response(jsonify({"error":"movies for director not found"}),400)
    else:
        res = make_response(jsonify(json),200)
    return res

if __name__ == "__main__":
    #p = sys.argv[1]
    print("Server running in port %s"%(PORT))
    app.run(host=HOST, port=PORT)

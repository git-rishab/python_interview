from flask import Flask,jsonify

app = Flask(__name__)

posts = {}

@app.route('/')
def welcome():
    return "Welcome to backend application"

@app.route('/add/<username>/<caption>', methods=['POST'])
def add(username, caption):
    id = len(posts)+1
    while id in posts:
        id += 1
    posts[username] = {}
    posts[username]["id"] = id
    posts[username]["caption"] = caption
    return "Post created succeddfully", 201

@app.route('/view', methods=["GET"])
def view():
    return jsonify(posts), 200

@app.route('/delete/<id>', methods=["DELETE"])
def delete_post(id):
    for el in posts:
        if posts[el["id"]] == int(id) :
            del posts[el]
    
    return "Post deleted successfully", 200


if __name__ == '__main__' :
    app.run()
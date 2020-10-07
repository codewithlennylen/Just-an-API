from flask import Flask, render_template, request
from flask_restful import Resource, Api
from datetime import date

app = Flask(__name__)
api = Api(app)


def get_my_age():
    today = date.today()
    my_age = int(str(today)[0:4]) - 2002
    return my_age


class BasicCalls(Resource):
    def get(self):
        return{
            "name": "Lenny Ng'ang'a",
            "age": get_my_age(),
            "language": "Python"
        }

    def post(self):
        some_json = request.get_json()
        return {"post-request": some_json}, 201


api.add_resource(BasicCalls, '/api')


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask
from src.user_api import user_api
from flasgger import Swagger

app = Flask(__name__)
app.register_blueprint(user_api)
Swagger(app)


if __name__ == "__main__":
    app.run(port=8000, debug=True)  
from flask import jsonify, request

from app import app

from .extensions import db
from .models import User


@app.route("/api/hello", methods=["GET"])
def hello_api():
    return {"message": "Hey man"}


@app.route("/api/users", methods=["POST"])
def create_user():
    data = request.get_json()
    new_user = User(username=data["username"], email=data["email"])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"id": new_user.id, "username": new_user.username, "email": new_user.email}), 201

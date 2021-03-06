from flask import Blueprint, jsonify, request
from api.middleware import login_required, read_token

from api.models.db import db
from api.models.cat import Cat

cats = Blueprint('cats', 'cats')

@cats.route('/', methods=["POST"])
@login_required
def create():
  data = request.get_json()
  profile = read_token(request)
  data["profile_id"] = profile["id"]
  cat = Cat(**data)
  db.session.add(cat)
  db.session.commit()
  return jsonify(cat.serialize()), 201
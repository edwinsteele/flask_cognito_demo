from flask import request, jsonify, Blueprint, current_app as app, render_template
from flask_jwt_extended import jwt_required

blueprint = Blueprint("pages", __name__, url_prefix="/pages",
                      template_folder="templates")


@blueprint.route("/hello", methods=["GET"])
def hello():
    return render_template("hello.html", name="edwin")


@blueprint.route("/protected", methods=["GET"])
@jwt_required
def hello_auth():
    return render_template("hello.html", name="protected person")

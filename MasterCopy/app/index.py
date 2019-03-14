#Test landing page (might have to delete when committing to master -- Hana and Orrin may
#have this one under control)

from flask import Blueprint, render_template

bp = Blueprint("index",__name__)

@bp.route("/", methods=["GET"])
def index():
    return render_template("index.html")
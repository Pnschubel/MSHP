# This is a sample landing page view! You can create lots of other python files
# like this, each with its own associated view. I'd suggest not throwing them
# into one .py file - that allows people to work on views separately, and
# keeps it much more organized.

from flask import Blueprint, render_template

# This is how you'll "sign" all your blueprints. We first create the string name
# that other Flask files will be able to use to reference this page, "index." Then
# we pass in __name__ as the import_name parameter so other programs know that
# they're importing this specific blueprint when they call "import index" or something.
# More here: http://flask.pocoo.org/docs/1.0/api/#flask.Blueprint
bp = Blueprint("index", __name__)


# I'm sure you know what this does. This associates a particular URL ending with
# this blueprint. In this case, since "/" is the default URL you go to when you
# visit the website, you'll be taken to the index page.
@bp.route("/", methods=["GET"])
def index():
    return render_template("index.html")

# NOTE NOTE NOTE NOTE:
# Whenever you create a new blueprint, you HAVE to register it in __init__.py as shown.
# Otherwise you'll just get a 404 when you request the URL.

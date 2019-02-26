import sqlite3, click, os
from flask import current_app, g
from flask.cli import with_appcontext


# Weirdest and most nondescript module name EVER:
# g is the "global" (if that's what it stands for) cache in which all the
# information that might be accessed by a request is stored. If we need
# to access the database multiple times, g will be called on instead of
# a new connection being created.

# Given a cursor and an SQL row, return a dictionary.
def make_dicts(cursor, row):

    # This is pretty messy, but here's what it does:
    # Cursor.description returns a 7-element tuple for each column where
    # the last 6 items of each tuple are None. dict() is evaluated using
    # its last argument first - for idx, value in enumerate(row), which
    # converts the row into key-value pairs (column_name: column_value).

    # As it iterates over the row, it adds entries into the dictionary
    # based on the name of the property in the cursor object. idx is
    # a variable referenced in the for loop - it's integer index
    # of the tuple corresponding to the column. We use 0 as the index
    # to get the actual name of the column - recall that the other 6
    # entries are None.
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))


def get_db():
    # We ensure that no database has been stored in g yet.
    if "db" not in g:
        g.db = sqlite3.connect(

            # Remember when we defined a database in __init__.py? It's recalled here,
            # and we use the path stored in the DATABASE key to retrieve the location,
            # which, if everything executed correctly, should be the instance path
            # of the application.

            # What's good about this approach is that we don't store the location of
            # our database directly in our program. That would be bad practice.
            current_app.config["DATABASE"],

            # This ensures that we actually convert all of our entries back to
            # Python-operable objects. Typically, if we stored a number (like 10)
            # in the database, it would be stored as "number(10)." PARSE_DECLTYPES
            # converts that into an actual number instead of an SQL type.
            detect_types=sqlite3.PARSE_DECLTYPES
        )

        # We define what function is responsible for our row factory here. That is, if we retrieve
        # a row given a cursor, we should get a dictionary out with the columns as key-value pairs.
        g.db.row_factory = make_dicts

    return g.db


def query_db(query, args=(), one=False):

    # This will do two things:
    # 	1. Call get_db() in order to create a connection to the DB
    # 	2. Execute the query with given arguments.
    # This is basically just a fancy wrapper for your regular
    # get_db().execute() function.
    cur = get_db().execute(query, args)

    # Returns "all remaining" results from the query. You'd typically
    # have to move through them one by one using the cursor, but fetchall
    # just loads everything into a list and returns it. I don't know why
    # it's called rv, that's just bad naming. I'd suggest renaming it to
    # something else.
    entries = cur.fetchall()

    # Closes the database connection.
    cur.close()

    # If "one" is true, this will just return the first element in the list.
    # This is a way to guarantee that only one result gets returned, since
    # queries aren't guaranteed to only return one. Otherwise, if "one" is
    # false, it'll just return the entire list.
    return (entries[0] if entries else None) if one else entries


def close_db(e=None):

    # Check if "db" exists in g. If it does, pop it off. Otherwise, just
    # return None.
    db = g.pop("db", None)

    if db is not None:
        db.close()


def init_db():

    # Gets the database connection.
    db = get_db()

    # Iterates over the schema.sql file and executes each line as SQL.
    with current_app.open_resource("schema.sql") as f:
        db.executescript(f.read().decode("utf8"))


def init_app(app):

    # This is a convenient function to add contexts to a couple other functions.
    # When this gets called in __init__, close_db gets the teardown_appcontext
    # decorator associated with it, and "initdb" becomes a usable command to
    # invoke init_db_command().

    # I think you can replace this by actually decorating close_db with
    # @app.teardown_appcontext, but this is nicer in my opinion. You can
    # take care of all your contextual stuff in one function.
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


# Associate initdb with this function using the inbuilt click library.
@click.command("initdb")
@with_appcontext
def init_db_command():
    init_db()
    click.echo("Initialized the database.")
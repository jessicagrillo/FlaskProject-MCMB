import os

from flask import Flask, render_template


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # # a simple page that says hello
    # @app.route('/hello')
    # def hello():
    #     return 'Hello, World!'

    # INDIVIDUALS Table Data
    headings = ("Name", "Location", "Needs", "Preferences")
    data = (
        ("Jordan Hilton", "South Dakota", "Transportation", "Female Driver"),
        ("Madelyn Brennan", "Oklahoma", "Housing, Transportation", "Female Hostess"),
        ("Daniella Owens", "Missouri", "Housing", "N/A"),
        ("Payton Burns", "Idaho", "Housing, Transportation", "N/A"),
        ("Molly Jones", "Texas", "Housing, Transportation", ""),
        ("Cameron Smith", "Missouri", "Housing", "?"),
        ("Chloe Arnold", "Louisiana", "Housing", "?"),
        ("Izzy Alvarez", "Texas", "Transportation", "?"),
        ("...", "...", "...", "..."),
    )

    # VOLUNTEERS Table Data
    headings2 = ("Name", "Location", "Resources", "Preferences")
    data2 = (
        ("Theresa Gomez", "New York", "Housing, Transportation", "?"),
        ("Brianna Johnson", "Massachusetts", "Housing, Transportation", "?"),
        ("Stephanie Miller", "California", "Housing, Transportation", "?"),
        ("Maria Davis", "Oregon", "Housing, Transportation", "?"),
        ("Kaitlin Williams", "New Mexico", "Housing", "?"),
        ("Sharon Anderson", "Washington", "Transportation", "?"),
        ("Laurie Hansen", "New Jersey", "Transportation", "?"),
        ("Janet Goldstein", "Maryland", "Housing", "?"),
        ("...", "...", "...", "..."),
    )

    @app.route('/individuals')
    def table_ind():
        return render_template("individuals.html", headings=headings, data=data)

    @app.route('/volunteers')
    def table_vol():
        return render_template("volunteers.html", headings2=headings2, data2=data2)

    @app.route('/home')
    def home():
        return render_template('home.html')

    # @app.route('/individuals')
    # def table1():
    #     return 'Hello, individuals!'

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    return app

from app import create_app

app = create_app()


if __name__ == "__main__":
    app.run(debug=True)


'''quellen
youtube authentifizierung                 https://www.youtube.com/watch?v=8PccXtf5tT0&list=PLMLdiraLeES2mry621I7mGr96w68z83vm&index=3
app aus factory importieren               https://flask.palletsprojects.com/en/3.0.x/patterns/appfactories/
if __name__ == "__main__"                 https://docs.python.org/3/library/__main__.html
app.run() server starten                  https://flask.palletsprojects.com/en/3.0.x/api/#flask.Flask.run
debug modus                               https://flask.palletsprojects.com/en/3.0.x/config/#DEBUG
'''
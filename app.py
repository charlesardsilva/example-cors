from flask import Flask
try:
    from flask.ext.cors import cross_origin
except ImportError:
    import os
    parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.sys.path.insert(0, parentdir)

    from flask.ext.cors import cross_origin


app = Flask(__name__)


@app.route("/", methods=['GET'])
@cross_origin()
def helloWorld():
    return '''<h1>Root Page!</h1>'''

@app.route("/yourConfiguration", methods=['GET'])
@cross_origin(origins="http://xxx:8000")
def your_configuration():
    return '''<h1>Deny Page!</h1>'''

if __name__ == "__main__":
    app.run(debug=True)

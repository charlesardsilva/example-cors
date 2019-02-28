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
    return '''<h1>Index Page!</h1>'''

@app.route("/content", methods=['GET'])
@cross_origin(origins="http://localhost:8000")
def get_content():
    print 'Get Content'
    return '''<h1>My Content</h1>'''

@app.route("/contentPreflighted", methods=['GET'])
@cross_origin(origins="http://localhost:8000", allow_headers= "X-Test-Header")
def get_content_preflighted():
    print 'Get Content Preflighted'
    return '''<h1>My Content Preflighted</h1>'''


if __name__ == "__main__":
    app.run(debug=True)

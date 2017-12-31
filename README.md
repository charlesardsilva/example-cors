test-cors
===================


Simple project for test and understand how CORS works.

----------


Installation
-------------
Install library CORS dependency:

    pip install -U flask-cors


How execute
-------------

1 - First, you need to run the app server.

    python app.py

It will execute in: http://localhost:5000

2 - Second, you need to run the app client.

    python -m SimpleHTTPServer 8000

It will execute in: http://localhost:8000


How it works
-------------
There are two buttons:

Get Content - Root page => Get Data from http://localhost:5000/

Get Content - Configuration => Get Data from http://localhost:5000/yourConfiguration
If your want do tests, change the configuration CORS (method your_configuration) in app.py and use this button.



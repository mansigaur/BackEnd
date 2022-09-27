
from flask import Flask, abort, jsonify
from flask_restful import Api
from resources.validate import ValidateAuthorAndUrl

app = Flask(__name__)
api = Api(app)

@app.errorhandler(Exception)
def handle_exception(err):
    """Return JSON instead of HTML for MyCustomError errors."""
    
    response = {}
    error_code = 400

    if hasattr(err, 'description'):
        response["error"] = err.description, 
    
    if len(err.args) > 0:
        response["message"] = err.args[0]

    if app.debug and hasattr(err, "data"):
        response['data'] = err.data['messages']
    
    if hasattr(err, 'code'):
        error_code = err.code

    return jsonify(response), error_code

def _access_control(response):
    """
    Response headers to manage the cors
    """
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Max-Age'] = 86400
    return response

api.add_resource(ValidateAuthorAndUrl, '/validate')
app.after_request(_access_control)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
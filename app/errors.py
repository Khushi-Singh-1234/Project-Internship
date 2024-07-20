
from flask import Blueprint,jsonify #import Blueprint and jsonify from flask module

errors= Blueprint('errors',__name__) # create a Blueprint instance for handling errors


@errors.app_errorhandler(404)
def not_found_error(error):
    return jsonify({"error":"Resource not found"}),404


@errors.app_errorhandler(400)
def bad_request_error(error):
    return jsonify({"error":"Bad request"}),400

@errors.app_errorhandler(500)
def internal_error(error):
    return jsonify({"error":"Internal server error"}),500
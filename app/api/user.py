from app.api import bp
from flask import Blueprint, request, jsonify

@bp.route('/users/profile',methods =['GET'])
def getUserProfile() :
    pass


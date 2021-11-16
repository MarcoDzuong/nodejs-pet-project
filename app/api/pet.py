from app.api import bp
from flask import Blueprint, request, jsonify

@bp.route('/boss',methods =['POST'])
def addBoss() :
    pass 

@bp.route('/boss',methods =['GET'])
def getListPet() :
    pass 

@bp.route('/boss/detail',methods =['GET'])
def getPetInfoDetail() :
    
    pass 




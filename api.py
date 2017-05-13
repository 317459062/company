#encoding:utf-8
from flask import Flask,request,jsonify,session
from flask_restful import Api,reqparse, abort, Resource
from api_xuexin import app_xuexin
from api_insurance import app_insurance
app=Flask(__name__)
app.register_blueprint(app_xuexin)
app.register_blueprint(app_insurance)
@app.errorhandler(404)
def page_not_found(error):
    return jsonify({"res":404})
if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)



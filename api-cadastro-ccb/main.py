from crypt import methods
from doctest import testfile
from operator import methodcaller
from unicodedata import name

from flask import Flask, request

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/student',methods=['POST'])
def create_student():
    payload = request.get_json()
    if payload:
        if 'name' in payload:
            name = payload ['name']
        if 'dob' in payload:
            dob = payload['dob']
        if 'common_church' in payload:
            common_church  = payload['common_church']
        if 'instrument' in payload['instrument']:
            instrument = payload['instrument']
        if 'tone' in payload['tone']:
            tone = payload['tone']
        return 'Data ok'
    return 'Missing data for registration',400
    
@app.route('/list_students',methods=['GET'])
def list_student():
    list_users = ['Lucas']
    payload = request.get_json()

    if payload:
        if 'id' in payload:
            id = payload['id']
        if 'name' in payload:
            name = payload['name']
    if True:
        return 'Result'

@app.route('/search_student',methods=['GET'])
def search():
    payload = request.get_json()

    if payload:
        id = payload['id']
    
    if True:
        return 'Data of student'
    return 'Id not found'



@app.route('/update_student',methods=['GET'])
def update_student():
    payload = request.get_json()

    if payload:
        if 'id' in payload:
            id = payload['id']
    
    if True:
        return 'Student data has been updated'
    return 'Id not found'


@app.route('/delet_student',methods=['GET'])
def delet_student():
    payload = request.get_json()

    if payload:
        if 'id' in payload:
            id = payload['id']
    
    if True:
        return 'Student data has deleated'
    return 'Id not found'

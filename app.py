#! /bin/python3
# base lib
import html
import secrets, random, os
import json
# foreign lib
from flask import Flask, render_template, request, Response, jsonify
from flask_api import  status
from flask_sqlalchemy import SQLAlchemy
# custom lib
from misc import *

# key generate for start also can read config file to do so.
secret_base = secrets.token_urlsafe(32)
session_rc4_key = secret_base  # future feature

# print the session communication key for debug
# print(session_rc4_key)

# init app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:////' + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)  # ORM sqlite db

# db model User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    image = db.Column(db.String(100))

# flask command to create db
@app.cli.command()
def initdb():
    db.create_all()

# / path for api help docs
# no input
# no return
@app.route('/')
def hello_world():  # put application's code here
    return render_template('apiHelp.html',urls=urldata)

# /question path get question
# no input
# return json
# {
#   'image': 'image url',
#   'name': ['name1',...] # default is name{1,4}
# }
@app.route('/question',methods=['GET'])
def getQuestions():
    # gen name lists by id lists
    people_max = User.query.count()
    if people_max <= 4:
        leak_info = {
            "image": "leak info",
            "name": [None,None,None,None]
        }
        return jsonify(leak_info), status.HTTP_500_INTERNAL_SERVER_ERROR

    lists = [i for i in range(1,people_max+1)]
    chosen_people_id = random.sample(lists,4)

    # set the true answer
    answer_user = User.query.get(chosen_people_id[0])
    answer_user_info = [chosen_people_id[0],answer_user.name,answer_user.image]
    # print("infolist",answer_user_info)
    check = {
        'id': answer_user.id,
        'true_user_hash': hash(str(answer_user_info)) # just for sure data no changed (even the hacker get keys)
    }
    # print("check raw",check)
    token = encrypt(json.dumps(check),session_rc4_key)
    # print("token",token)

    # generate user name lists
    fake_user = [ User.query.get(chosen_people_id[i]) for i in range(1,4) ]
    name_list = []
    name_list.append( html.escape(answer_user.name) )
    for every_fack_user in fake_user:
        name_list.append( html.escape(every_fack_user.name) )

    # make response
    res = {
        'image': html.escape(answer_user.image) ,
        'name': name_list
    }
    resp = Response(json.dumps(res) ,mimetype='application/json')
    # set true answer as token in cookie
    resp.set_cookie(key="token",value=token)

    return resp

# /answer path post answer
# input post param & cookie
#   answer=<username user answered>
#   cookie: token=<token from get question
# return json
# {
#   "iscorrect":Ture/False
# }
@app.route('/answer',methods=['POST'])
def checkAnswer():
    # get the answer
    answer = request.form.get('answer')
    # get the token(contain true answer)
    token = request.cookies.get('token')
    # make response
    res = {"iscorrect":False}
    try:
        # decode the true answer
        true_answer_json = json.loads(decrypt(token,session_rc4_key))
        true_answer_user = User.query.get(true_answer_json['id'])
        true_answer_user_info = [true_answer_user.id ,true_answer_user.name,true_answer_user.image]

        # verify answer
        answer_true = true_answer_user.name == answer
        answer_no_change = hash(str(true_answer_user_info)) == true_answer_json['true_user_hash']
        if ( answer_true and answer_no_change ):
            res = {"iscorrect":True}

    except :
        pass
    finally:
        return jsonify(res)

# /userdata path post userdata
# input post param
#   user=username
#   image_url=user image
# return json
# {
#   "upload": "success"/"fail"
# }
@app.route('/userdata',methods=['POST'])
def upload():
    username = request.form.get('user')
    image_url = request.form.get('image_url')
    try:
        if username == None or image_url ==None :
            raise RuntimeError
        new_user = User(name=username,image=image_url)
        db.session.add(new_user)
        db.session.commit()
        print("commit")
        res = {"upload":"success"}
    except:
        res = {"upload":"fail"}
    finally:
        return jsonify(res)

# bad api access for clean the database
# /reinitdb path for restart database
# no input
# return json
# {
#   "state": "success"/"fail"
# }
@app.cli.command()
def reinitdb():
    res = {"state":"fail"}
    try:
        db.drop_all()
        db.create_all()
        res = {"state":"success"}
    except:
        pass
    finally:
        return print(res)


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080)

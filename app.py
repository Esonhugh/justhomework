import secrets, random, os
from misc import *
from flask import Flask, render_template, request, Response, jsonify
import json

secret_base = secrets.token_urlsafe(32)
session_rc4_key = secret_base  # future feature

print(session_rc4_key)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:////' + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)  # ORM sqlite db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    image = db.Column(db.String(100))


@app.cli.command()
def initdb():
    db.create_all()

@app.route('/')
def hello_world():  # put application's code here
    return render_template('apiHelp.html',urls=urldata)

@app.route('/question',methods=['GET'])
def getQuestions():
    people_max = User.query.count()
    lists = [i for i in range(1,people_max+1)]
    chosen_people_id = random.sample(lists,4)
    answer_user = User.query.get(chosen_people_id[0])
    answer_user_info = [chosen_people_id[0],answer_user.name,answer_user.image]

    print("infolist",answer_user_info)
    check = {
        'id': answer_user.id,
        'true_user_hash': hash(str(answer_user_info)) # just for sure data no changed (even the hacker get keys)
    }

    print("check raw",check)
    token = encrypt(json.dumps(check),session_rc4_key)
    print("token",token)

    fake_user = [ User.query.get(chosen_people_id[i]) for i in range(1,4) ]

    name_list = []
    name_list.append(answer_user.name)
    for every_fack_user in fake_user:
        name_list.append(every_fack_user.name)

    res = {
        'image' : answer_user.image ,
        'name' : name_list
    }

    print(res)
    json.dumps(res)
    resp = Response(json.dumps(res), mimetype='application/json')
    resp.set_cookie(key="token",value=token)
    return resp


@app.route('/checkAnswer',methods=['POST'])
def checkAnswer():
    answer = request.form.get('answer')
    res = {"iscorrect":False}
    token = request.cookies.get('token')
    try:
        real_answer = json.loads(decrypt(token,session_rc4_key))
        answered_user = User.query.get(real_answer['id'])
        answered_user_info = [answered_user.id ,answered_user.name,answered_user.image] 




        answer_true = answered_user.name == answer
        answer_no_change = hash(str(answered_user_info)) == real_answer['true_user_hash']
        if ( answer_true and answer_no_change ):
            res = {"iscorrect":True}
    except :
        pass
    finally:
        return jsonify(res)


@app.route('/uploadData',methods=['POST'])
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
        res = {"upload":"true"}
    except:
        res = {"upload":"fail"}
    finally:
        return jsonify(res)

@app.route('/reinitdb')
def reinitdb():
    try:
        db.drop_all()
        db.create_all()
        return "success"
    except:
        return "fail"


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080)

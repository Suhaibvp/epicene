import os
from flask import *
from werkzeug.utils import secure_filename

from src.dbconnect import *

app=Flask(__name__)

@app.route('/login',methods=['post'])
def login():

    username=request.form['uname']
    password=request.form['pass']
    qry="select*from `log` where username=%s and `password`=%s"
    val=(username,password)
    s=selectone(qry,val)
    print(s)

    if s is None:
        return jsonify({'task':'invalid'})
    else:
        id=s[0]
        return jsonify({'task':'valid',"id" : id })

@app.route('/reg',methods=['post'])
def reg():
    print(request.files)
    print(request.form)

    uname=request.form['uname']
    uplace=request.form['uplace']
    upost=request.form['upost']
    upin=request.form['upin']
    uphno = request.form['phone']
    uemail = request.form['uemail']
    photo = request.files['files']
    fn = secure_filename(photo.filename)
    photo.save(os.path.join("static/trans", fn))
    username=request.form['username']
    password=request.form['password']
    qry="insert into log values(null,%s,%s,'user ')"
    val = (username, password)
    id=iud(qry, val)
    qry="INSERT INTO`user`VALUES(null,%s,%s,%s,%s,%s,%s,%s,%s)"
    val1=(str(id),uname,uplace,upost,upin,uphno,uemail,photo)
    iud(qry,val1)
    return jsonify({'task': 'success'})

@app.route('/addevent',methods=['post'])
def addevent():
    print(request.form)
    id=request.form['lid']
    eventname=request.form['event']
    descri=request.form['description']
    venue=request.form['venue']
    date=request.form['date']
    time=request.form['time']
    qry="INSERT INTO `events` VALUES(null,%s,%s,%s,%s,%s,%s)"
    val=(str(id),eventname,descri,venue,date,time)
    iud(qry,val)
    return jsonify({'task':'success'})

@app.route('/editevent',methods=['post'])
def editevent():
    print(request.form)
    id=request.form['id']
    eventname=request.form['event']
    descri=request.form['description']
    venue=request.form['venue']
    date=request.form['date']
    time=request.form['time']
    qry="update `events` set et_event_name=%s,et_description=%s,et_venue=%s,et_date=%s,et_time=%s where et_id=%s"
    val=(eventname,descri,venue,date,time,str(id))
    iud(qry,val)
    return jsonify({'task':'success'})



# @app.route('/viewevent',methods=['post'])
# def viewevent():
#     qry="SELECT * FROM `events`"
#     res=androidselectallnew(qry)
#     return jsonify(res)


@app.route('/deleevent',methods=['post'])
def deleevent():
    id=request.form['etid']

    qry="DELETE FROM`events` WHERE`et_id`=%s "
    val=(str(id))
    iud(qry,val)
    return jsonify({'task': 'success'})


# @app.route('/viewjob',methods=['post'])
# def viewjob():
#     qry="SELECT * FROM `jobs`"
#     res=androidselectallnew(qry)
#     return jsonify(res)





# @app.route('/viewhealth',methods=['post'])
# def viewhealth():
#     qry="SELECT * FROM `health_tips`"
#     res=androidselectallnew(qry)
#     return jsonify(res)


@app.route('/viewcouncel',methods=['post'])
def viewcouncel():
    qry="SELECT * FROM `councelling_pgm`"
    res=androidselectallnew(qry)
    return jsonify(res)


@app.route('/viewlegals',methods=['post'])
def viewlegals():
    qry="SELECT * FROM `legal_assistant`"
    res=androidselectallnew(qry)
    return jsonify(res)


@app.route('/dlt',methods=['post'])
def dlt():
    id=request.form['id']
    qry="delete from events where et_id=%s"
    val=id
    res=iud(qry,id)
    return jsonify({'task':'success'})


@app.route('/vieweduc',methods=['post'])
def vieweduc():
    qry="SELECT * FROM `education`"
    res=androidselectallnew(qry)
    return jsonify(res)


@app.route('/viewhrights',methods=['post'])
def viewhrights():
    qry="SELECT * FROM `human_rights`"
    res=androidselectallnew(qry)
    return jsonify(res)

@app.route('/viewlocal',methods=['post'])
def viewlocal():
    qry = "SELECT * FROM `local_coordinator`"
    res = androidselectallnew(qry)
    return jsonify(res)

@app.route('/apmtrqst',methods=['post'])
def apmtrqst():
    uid=request.form['u_id']
    lid = request.form['la_id']
    qry="INSERT INTO `appointments` VALUES(NULL,%s,%s,CURDATE(),CURTIME(),'pending')"
    val=(uid,lid)
    iud(qry,val)
    return jsonify({'task':'success'})

@app.route('/changepassword',methods=['GET','POST'])
def changepassword():
    id=request.form['lid']
    crntpwd=request.form['currentpwd']

    newpwd=request.form['newpwd']
    qry="update log set password=%s where l_id=%s and password=%s"
    val=(newpwd,id,crntpwd)
    iud(qry,val)
    return jsonify({"task": "success"})


@app.route('/viewfriends',methods=['GET','post'])
def viewfriends():
    id = request.form['uid']
    qry="SELECT `u_name`,`u_photo`,l_id FROM`user` where l_id!=%s"
    val=(id)
    res=androidselectall(qry,val)
    return jsonify(res)

@app.route('/viewevent',methods=['GET','post'])
def viewevent():
    qry = "SELECT * FROM`events`"
    res = androidselectallnew(qry)
    print(res)
    return jsonify (res)

@app.route('/viewjob',methods=['GET','post'])
def viewjob():
    id = request.form['j_type']
    qry ="SELECT * from jobs WHERE `j_type`=%s"
    res = androidselectall(qry, id)
    return jsonify(res)

@app.route('/viewdoc',methods=['GET','post'])
def viewdoc():

    id = request.form['specialization']
    qry = "SELECT * FROM `medical` where m_specialization=%s"
    res = androidselectall(qry, id)
    return jsonify(res)

@app.route('/viewhealth',methods=['GET','post'])
def viewhealth():
    id = request.form['h_type']
    qry = "SELECT * FROM `health_tips` WHERE `h_type`=%s"
    res = androidselectall(qry, id)
    return jsonify(res)

@app.route('/viewcoun',methods=['GET','post'])
def viewcoun():

    qry = "SELECT * FROM `councelling_pgm`"
    res = androidselectallnew(qry)
    return jsonify(res)


@app.route('/viewcounmore',methods=['GET','post'])
def viewcounmore():
    id=request.form['id']

    qry = "SELECT * FROM `councelling_pgm` where cp_id=%s"
    res = androidselectall(qry, id)
    return jsonify(res)


@app.route('/viewlegal',methods=['GET','post'])
def viewlegal():

    qry = "SELECT * FROM `legal_assistant`"
    res = androidselectallnew(qry)
    return jsonify(res)

@app.route('/viewmeet',methods=['GET','post'])
def viewmeet():

    qry ="SELECT * FROM `meeting`"
    res = androidselectallnew(qry)
    print(res)
    return jsonify(res)

@app.route('/viewedu',methods=['GET','post'])
def viewedu():

    qry ="SELECT * FROM `education`"
    res = androidselectallnew(qry)
    return jsonify(res)


@app.route('/viewedumore',methods=['GET','post'])
def viewedumore():
    id=request.form['id']

    qry ="SELECT * FROM `education` where e_id=%s"
    res = androidselectall(qry, id)
    return jsonify(res)

@app.route('/apmtlegal',methods=['GET','post'])
def apmtlegal():

    qry = "SELECT  * FROM `legal_assistant`"
    res = androidselectallnew(qry)
    return jsonify(res)







@app.route('/viewapmt',methods=['GET','post'])
def viewapmt():
    id = request.form['id']

    qry = "SELECT `appointments`.*,`legal_assistant`.`la_name` FROM `legal_assistant` JOIN `appointments` ON `legal_assistant`.`la_id`=`appointments`.`la_id` WHERE `appointments`.`a_status`='Accepted' and `appointments`.`u_id`=%s"
    res = androidselectall(qry, id)
    return jsonify(res)

@app.route('/viewhuman',methods=['GET','post'])
def viewhuman():


    qry = "SELECT * FROM `human_rights` "
    res = androidselectallnew(qry)
    return jsonify(res)


@app.route('/in_message2',methods=['post'])
def in_message():
    print(request.form)
    fromid = request.form['fid']
    print("fromid",fromid)

    toid = request.form['toid']
    print("toid",toid)

    message=request.form['msg']
    print("msg",message)
    qry = "INSERT INTO `chat` VALUES(NULL,%s,%s,CURDATE(),%s)"
    value = (fromid, toid, message)
    print("pppppppppppppppppp")
    print(value)
    iud(qry, value)
    return jsonify(status='send')

@app.route('/view_message2',methods=['post'])
def view_message2():
    print("wwwwwwwwwwwwwwww")
    print(request.form)
    fromid=request.form['fid']
    print(fromid)
    toid=request.form['toid']
    print(toid)
    lmid = request.form['lastmsgid']
    print("msgggggggggggggggggggggg"+lmid)
    sen_res = []
    # qry="SELECT * FROM chat WHERE (fromid=%s AND toid=%s) OR (fromid=%s AND toid=%s) ORDER BY DATE ASC"
    qry="SELECT `c_fromid`,`c_text`,`c_date`,`c_id` FROM `chat` WHERE `c_id`>%s AND ((`c_toid`=%s AND  `c_fromid`=%s) OR (`c_toid`=%s AND `c_fromid`=%s)  )  ORDER BY c_id ASC"

    val=(str(lmid),str(toid),str(fromid),str(fromid),str(toid))
    print("fffffffffffff",val)
    res = androidselectall(qry,val)
    print("resullllllllllll")
    print(res)
    if res is not None:
        return jsonify(status='ok', res1=res)
    else:
        return jsonify(status='not found')


if __name__ =="__main__":
    app.run(host="0.0.0.0",port=5000)    
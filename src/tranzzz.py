import os
from flask import *
from werkzeug.utils import secure_filename

app=Flask(__name__)


import functools
def login_required(func):
    @functools.wraps(func)
    def secure_function():
        if "lid" not in session:
            return redirect ("/")
        return func()
    return secure_function



from src.dbconnect import *
app.secret_key="qqq"
@app.route('/')
def main():
    return render_template('login.html')
@app.route('/addedu',methods=['post'])
def addedu():
    return render_template('admin/addeducation.html')
@app.route('/addlegal',methods=['post'])
def addlegal():
    return render_template('admin/addlegalassistance.html')
@app.route('/addmed',methods=['post'])
def addmed():
    return render_template('admin/addmedicalofficer.html')
@app.route('/adminhome')
def adminhome():
    return render_template('admin/adminhome.html')
@app.route('/loccord')
def loccoord():
    qry = "SELECT `local_coordinator`.* FROM `local_coordinator` JOIN `log` ON `log`.`l_id`=`local_coordinator`.`l_id` WHERE `log`.type='pending'"
    res = selectall(qry)
    return render_template('admin/APPROVE LOCAL COORDINATOR.html',val=res)
@app.route('/acceptloccord')
def acceptloccord():
    id=request.args.get('id')
    qry="UPDATE `log` SET `type`='local coordinator'  WHERE `l_id`=%s"
    val=(str(id))
    iud(qry,val)


    return '''<script>alert("accepted");window.location="/loccord"</script>'''

@app.route('/rejectloccord')
def rejectloccord():
    id=request.args.get('id')
    qry="UPDATE `log` SET `type`='rejected'  WHERE `l_id`=%s"
    val=(str(id))
    iud(qry,val)
    return '''<script>alert("rejected");window.location="/loccord"</script>'''




@app.route('/approvetrans')
def approvetrans():
    qry = "SELECT *FROM user"
    res = selectall(qry)
    return render_template('admin/approvetransducer.html',val=res)
@app.route('/password')
def password():
    return render_template('admin/changepassword.html')

@app.route('/password2',methods=['post'])
def password2():
    curpswrd=request.form['textfield']
    newpswrd=request.form['textfield2']
    confpswrd=request.form['textfield3']
    qry = "select * from log where password=%s and l_id=%s"
    val = (curpswrd, session['lid'])
    res = selectone(qry, val)
    if res is not None:
        if curpswrd == newpswrd:
            return '''<script>alert("password is same as current password");window.location="/"</script>'''
        elif newpswrd == confpswrd:
            qry = "UPDATE `log` SET `password`=%s WHERE l_id=%s"
            val = (newpswrd, session['lid'])
            iud(qry, val)

            return '''<script>alert("password  changed successfully");window.location="/adminhome"</script>'''
        else:
            return '''<script>alert("invalid password");window.location="/password"</script>'''
    else:
        return '''<script>alert("current password doesnot exist");window.location="/password"</script>'''


@app.route('/job',methods=['post','get'])
def job():
    qry = "SELECT *FROM jobs"
    res = selectall(qry)
    return render_template('admin/managejob.html', val=res)


@app.route('/addjob',methods=['post','get'])
def addjob():

    return render_template('admin/add_job.html')
@app.route('/managelegal')
def managelegal():
    qry = "SELECT *FROM legal_assistant"
    res = selectall(qry)
    return render_template('admin/managelegalassist.html',val=res)

@app.route('/delmanlegal')
def delmanlegal():
    id=request.args.get('id')
    qry ="DELETE FROM `legal_assistant` WHERE l_id=%s"
    val = (str(id))
    iud(qry, val)
    return '''<script>alert("successfully deleted");window.location="managelegal"</script>'''

@app.route('/editleg',methods=['get'])
def editleg():
    id = request.args.get('id')
    print(id)

    session['ppid'] = id
    qry = "SELECT * FROM `legal_assistant` WHERE `l_id`=%s"

    res = selectone(qry,str(id))

    print(res)
    return render_template('admin/editlegalassistance.html',val=res)

@app.route('/editleg2',methods=['post'])
def editleg2():
    try:
        id=session['ppid']
        name=request.form['textfield']
        file=request.form['file']
        fn=secure_filename(file.filename)
        file.save(os.path.join("static/document",fn))
        gender=request.form['radiobutton']
        place=request.form['textfield2']
        post=request.form['textfield3']
        pin=request.form['textfield4']
        ph_no=request.form['textfield5']
        email=request.form['textfield6']
        qry="UPDATE `legal_assistant` SET `la_name`=%s,`la_gender`=%s,`la_place`=%s,`la_post`=%s,`la_pin`=%s,`la_contactno`=%s,`la_email`=%s,`document`=%s WHERE `l_id`=%s"

        val=(name,gender,place,post,pin,ph_no,email,fn,str(id))
        iud(qry,val)
        return'''<script>alert("updated successfully");window.location="managelegal"</script>'''
    except Exception as e:
        id = session['ppid']
        name = request.form['textfield']

        gender = request.form['radiobutton']
        place = request.form['textfield2']
        post = request.form['textfield3']
        pin = request.form['textfield4']
        ph_no = request.form['textfield5']
        email = request.form['textfield6']
        qry = "UPDATE `legal_assistant` SET `la_name`=%s,`la_gender`=%s,`la_place`=%s,`la_post`=%s,`la_pin`=%s,`la_contactno`=%s,`la_email`=%s WHERE `l_id`=%s"

        val = (name, gender, place, post, pin, ph_no, email, str(id))
        iud(qry, val)
        return '''<script>alert("updated successfully");window.location="managelegal"</script>'''








@app.route('/managemedical')
def managemedica():
    qry = "SELECT *FROM medical"
    res = selectall(qry)
    return render_template('admin/managemedicalofficer.html',val=res)


@app.route('/deletemedi')
def deletemedi():
    id=request.args.get('id')

    qry="DELETE FROM `medical` WHERE l_id=%s"
    val=(str(id))
    iud(qry,val)
    return '''<script>alert("successfully deleted");window.location="managemedical"</script>'''

@app.route('/editmed',methods=['get'])
def editmed():
    id = request.args.get('id')
    session['ppid'] = id
    qry = "SELECT * FROM `medical` WHERE l_id=%s"

    res = selectone(qry,str(id))
    return render_template('admin/editmedicalofficer.html',val=res)


@app.route('/editmed2',methods=['post'])
def editmed2():
    id=session['ppid']
    name=request.form['textfield']
    gender=request.form['radiobutton']
    secialisation=request.form['select']
    place=request.form['textfield2']
    post=request.form['textfield3']
    pin=request.form['textfield4']
    ph_no=request.form['textfield5']
    email=request.form['textfield6']
    qry="UPDATE `medical` SET `m_name`=%s,`m_gender`=%s,`m_specialization`=%s,`m_place`=%s,`m_post`=%s,`m_pin`=%s,`m_contactno`=%s,`m_email`=%s WHERE `l_id`=%s"
    val=(name,gender,secialisation,place,post,pin,ph_no,email,str(id))
    iud(qry,val)
    return'''<script>alert("updated successfully");window.location="/managemedical"</script>'''


@app.route('/mnageedu')
def mnageedu():
    qry = "SELECT *FROM education"
    res = selectall(qry)
    return render_template('admin/mnageeducation.html',val=res)\



@app.route('/editedu2',methods=['post'])
def editedu2():
    try:
        id=session['ppid']
        name=request.form['textfield']
        file=request.form['file']
        fn=secure_filename(file.filename)
        file.save(os.path.join("static/document",fn))

        place=request.form['textfield2']
        post=request.form['textfield3']
        pin=request.form['textfield4']
        ph_no=request.form['textfield5']
        email=request.form['textfield6']
        qry="UPDATE `education` SET `e_name`=%s,`e_place`=%s,`e_post`=%s,`e_pin`=%s,`e_phno`=%s,`e_email`=%s,`e_documents`=%s WHERE `l_id`=%s WHERE `l_id`=%s"

        val=(name,place,post,pin,ph_no,email,fn,str(id))
        iud(qry,val)
        return'''<script>alert("updated successfully");window.location="manageedu"</script>'''
    except Exception as e:
        id = session['ppid']
        name = request.form['textfield']

        place = request.form['textfield2']
        post = request.form['textfield3']
        pin = request.form['textfield4']
        ph_no = request.form['textfield5']
        email = request.form['textfield6']
        qry = "UPDATE `education` SET `e_name`=%s,`e_place`=%s,`e_post`=%s,`e_pin`=%s,`e_phno`=%s,`e_email`=%s WHERE `e_id`=%s"

        val = (name, place, post, pin, ph_no, email, str(id))
        iud(qry, val)
        return '''<script>alert("updated successfully");window.location="mnageedu"</script>'''

































@app.route('/editedu')
def editedu():
    id=request.args.get('id')

    qry="select * from education where e_id=%s"
    val=(str(id))
    res=selectone(qry,val)

    return render_template('admin/editeducation.html',val=res)
@app.route('/delmanedu1')
def delmanedu1():
    id=request.args.get('id')
    qry ="DELETE FROM `education` WHERE e_id=%s"
    val = (str(id))
    iud(qry, val)
    return '''<script>alert("successfully deleted");window.location="mnageedu"</script>'''


@app.route('/deljob1')
def deljob1():
    id=request.args.get('id')
    print(str(id))
    qry ="DELETE FROM `jobs` WHERE j_id=%s"
    val = (str(id))
    iud(qry, val)
    return '''<script>alert("successfully deleted");window.location="job"</script>'''



@app.route('/editjob1')
def editjob1():
    id=request.args.get('id')
    session['jid']=id



    qry="select * from jobs where j_id=%s"
    val=(str(id))
    res=selectone(qry,val)

    return render_template('admin/editjob1.html',val=res)



@app.route('/updatejob1',methods=['post'])
def updatejob1():
    id=session['jid']
    type=request.form['textfield']

    post=request.form['textfield2']
    place=request.form['textfield3']
    pin=request.form['textfield4']
    ph_no=request.form['textfield5']
    email=request.form['textfield6']
    qry="UPDATE `jobs` SET `j_type`=%s,`j_place`=%s,`j_post`=%s,`j_pin`=%s,`j_phno`=%s,`j_email`=%s WHERE j_id=%s"
    val=(type,place,post,pin,ph_no,email,str(id))
    iud(qry,val)
    return'''<script>alert("updated successfully");window.location="/job"</script>'''





@app.route('/logout')
@login_required
def logout():
    session.clear()
    return render_template('login.html')

@app.route('/logincode',methods=['post'])
def logincode():
    uname=request.form['textfield']
    pssword=request.form['textfield2']
    qry="SELECT *FROM `log` WHERE(`username`=%s AND `password`=%s)"
    val=(uname,pssword)
    res=selectone(qry,val)

    if res is None:

        return'''<script>alert("invalid");window.location="/"</script>'''
    elif res[3]=='admin':
        session['lid']=res[0]
        return '''<script>alert("welcome to epicene");window.location="/adminhome"</script>'''
    elif res[3]=='medical officer':
        session['lid']=res[0]

        return '''<script>alert("welcome to epicene");window.location="/mediofficerhome"</script>'''
    elif res[3]=='local coordinator':
        session['lid']=res[0]
        return '''<script>alert("welcome to epicine local cordinator");window.location="/coordinator"</script>'''
    elif res[3] == 'legal officer':
        session['lid'] = res[0]
        return '''<script>alert("welcome to epicine legal officer");window.location="/leghome"</script>'''





# ADMIN>.................................................

@app.route('/adappoint')
@login_required
def adappoint():
    qry = "SELECT user.u_name,user.u_place,user.u_phno,appointments.a_date ,appointments.a_id FROM appointments JOIN USER ON appointments.u_id=user.l_id WHERE appointments.a_status='pending'"
    res=selectall(qry)
    return render_template('legalassistance/addappointment.html',val=res)

@app.route('/acceptappoi')
def acceptappoi():
    id=request.args.get('id')
    session['appid']=id
    return render_template('legalassistance/appointmenttime.html')


@app.route('/addappoi2',methods=['post'])
def addappoi2():
    time=request.form['textfield']
    qry="UPDATE `appointments` SET `a_time`=%s,a_status='accepted' WHERE `a_id`=%s"
    val=(time,session['appid'])
    iud(qry,val)
    return '''<script>alert("appointment accepted");window.location="/adappoint"</script>'''

@app.route('/rejectappoi')
def rejectappoi():
    id = request.args.get('id')
    qry = "UPDATE `appointments` SET a_status='rejected' WHERE `a_id`=%s"
    val = ('id')
    iud(qry, val)
    return '''<script>alert("appointment rejected");window.location="/adappoint"</script>'''


# @app.route('/viewappo')
# def viewappo():
#     qry=""





@app.route('/addhuman',methods=['post'])
def addhuman():


    return render_template('legalassistance/addhumanrights.html')
@app.route('/insertaddhuman',methods=['post'])
def insertaddhuman():
    try:
        type=request.form['select']
        descrption=request.form['desc']
        qry="insert into `human_rights` VALUES(null,%s,%s,%s)"
        val=(session['lid'],type,descrption)
        iud(qry,val)
        return '''<script>alert("added success");window.location="/manahumanrights"</script>'''
    except Exception as e:
        return '''<script>alert("duplicate entry try again..");window.location="manahumanrights"</script>'''


@app.route('/addmeet',methods=['post'])
def addmeet():
    return render_template('legalassistance/addmeetingnotification.html')
@app.route('/leassist')
def leassist():
    return render_template('legalassistance/legalassisthome.html')
@app.route('/manahumanrights')
@login_required
def manahumanrights():
    qry="select * from human_rights"
    res=selectall(qry)

    return render_template('legalassistance/managehumanrights.html',val=res)
@app.route('/manameetnoti')

@login_required
def manameetnoti():
    qry="SELECT * FROM `meeting`"
    res = selectall(qry)
    return render_template('legalassistance/managemeetingnotification.html',val=res)

@app.route('/editlegmeet2')
def editlegmeet2():
    id = request.args.get('id')
    print(id)

    session['ppid'] = id
    qry = "SELECT * FROM `meeting` WHERE mt_id=%s"

    res = selectone(qry, str(id))

    print(res)
    return render_template('legalassistance/editlegmeet2.html', val=res)

@app.route('/delmeet')
def delmeet():
    id=request.args.get('id')
    qry="DELETE FROM meeting WHERE mt_id=%s"
    val=(str(id))
    iud(qry,val)
    return'''<script>alert("deleted");window.location="/manameetnoti"</script>'''

@app.route('/hdel')
def hdel():
    id=request.args.get('id')
    qry="DELETE FROM `human_rights` WHERE  `hr_id` =%s"
    val=(str(id))
    iud(qry,val)
    return'''<script>alert("deleted");window.location="/manahumanrights"</script>'''







@app.route('/pswd1')
@login_required
def pswd1():
    return render_template('legalassistance/changepassword1.html')


@app.route('/leghome')
def leghome():
    return render_template('legalassistance/legalassisthome.html')


@app.route('/coordinator')
def coordinator():
    return render_template('local coordinator/localcoordinator.html')





@app.route('/manaaware')
def manaaware():
    return render_template('local coordinator/addawarenessprgm.html')


@app.route('/event')
def event():
    qry="SELECT * FROM `events`"
    res=selectall(qry)
    return render_template('local coordinator/veiwevent.html',val=res)
@app.route('/pswd2')
def pswd2():
    return render_template('local coordinatior/changepassword2.html')
@app.route('/addcounpro',methods=['post'])
def addcounpro():
    return render_template('medical officer/addcounselingprogram.html')
@app.route('/addhealth',methods=['post'])
def addhealth():
    return render_template('medical officer/addhealthtip.html')
@app.route('/manacounpro')
@login_required
def manacounpro():
    qry="select * from `councelling_pgm`"
    res=selectall(qry)

    return render_template('medical officer/managecouncellingprogram.html',val=res)





@app.route('/addcounc2',methods=['post'])
def addcounc2():
    try:
         counc=request.form['textfield']
         descri=request.form['textarea']
         place=request.form['textfield2']
         date=request.form['textfield3']
         time=request.form['textfield4']
         contno=request.form['textfield5']
         qry="insert into councelling_pgm VALUES(NULL,%s,%s,%s,%s,%s,%s,%s) "
         val=(str(session['lid']),counc,descri,place,date,time,contno)
         iud(qry,val)
         return'''<script>alert("added successfully");window.location="/manacounpro"</script>'''
    except Exception as e:
        return '''<script>alert("duplicate entry try again..");window.location="manacounpro"</script>'''





@app.route('/delcounc')
def delcounc():
    id=request.args.get('id')
    qry="delete from councelling_pgm where cp_id=%s"
    val=(id)
    iud(qry,val)
    return'''<script>alert("deleted");window.location="/manacounpro"</script>'''

@app.route('/editcounc2')
def editcounc2():
    id=request.args.get('id')
    session['cp_id']=id
    val = (str(id))
    qry="select * from councelling_pgm where cp_id=%s"
    res=selectone(qry,val)
    return render_template('medical officer/editcounc2.html',val=res)

@app.route('/updatecoun1',methods=['post'])
def updatecoun1():
    id=session['cp_id']
    counciling=request.form['textfield']
    description=request.form['textarea']
    Place=request.form['textfield2']
    date=request.form['textfield3']
    Ttime=request.form['textfield4']
    cnt=request.form['textfield5']

    qry="UPDATE `councelling_pgm` SET `cp_pgm`=%s,`cp_description`=%s,cp_place=%s,cp_date=%s,cp_time=%s,cp_contactno=%s WHERE cp_id=%s"
    val=(counciling,description,Place,date,Ttime,cnt,str(id))
    iud(qry,val)
    return'''<script>alert("updated successfully");window.location="/manacounpro"</script>'''


@app.route('/password3',methods=['post'])
def password3():
    curpswrd=request.form['textfield']
    newpswrd=request.form['textfield2']
    confpswrd=request.form['textfield3']
    qry = "select * from log where password=%s and l_id=%s"
    val = (curpswrd, session['lid'])
    res = selectone(qry, val)
    if res is not None:
        if curpswrd == newpswrd:
            return '''<script>alert("password is same as current password");window.location="/"</script>'''
        elif newpswrd == confpswrd:
            qry = "UPDATE `log` SET `password`=%s WHERE l_id=%s"
            val = (newpswrd, session['lid'])
            iud(qry, val)

            return '''<script>alert("password  changed successfully");window.location="/mediofficerhome"</script>'''
        else:
            return '''<script>alert("invalid password");window.location="/pswd3"</script>'''
    else:
        return '''<script>alert("current password doesnot exist");window.location="/pswd3"</script>'''




@app.route('/passwordlegal',methods=['post'])
def passwordlegal():
    curpswrd=request.form['textfield']
    newpswrd=request.form['textfield2']
    confpswrd=request.form['textfield3']
    qry="select * from log where password=%s and l_id=%s"
    val=(curpswrd,session['lid'])
    res=selectone(qry,val)
    if res is  not None:
        if curpswrd==newpswrd:
            return '''<script>alert("password is same as current password");window.location="/"</script>'''
        elif newpswrd==confpswrd:
            qry="UPDATE `log` SET `password`=%s WHERE l_id=%s"
            val=(newpswrd,session['lid'])
            iud(qry,val)

            return '''<script>alert("password  changed successfully");window.location="/leghome"</script>'''
        else:
            return '''<script>alert("invalid password");window.location="/pswd1"</script>'''
    else:
        return '''<script>alert("current password doesnot exist");window.location="/pswd1"</script>'''







@app.route('/manhealthtip')
@login_required
def manhealthtip():
    qry="select * from health_tips"
    res=selectall(qry)
    return render_template('medical officer/managehealthtip.html',val=res)
@app.route('/deltip')
def deltip():
    id=request.args.get('id')
    qry="delete from health_tips where h_id=%s"
    val=(id)
    iud(qry,val)
    return'''<script>alert("deleted");window.location="/manhealthtip"</script>'''



@app.route('/addhealth2',methods=['post'])
def addhealth2():
    try:
        type=request.form['textfield']
        des=request.form['textarea']
        qry="insert into health_tips values(null,%s,%s,%s)"
        val=(str(session['lid']),type,des)
        iud(qry,val)
        return'''<script>alert("added");window.location="/manhealthtip"</script>'''
    except Exception as e:
        return '''<script>alert("duplicate entry try again..");window.location="manhealthtip"</script>'''





@app.route('/mediofficerhome')
@login_required
def mediofficerhome():
    return render_template('medical officer/medicalofficerhome.html')
@app.route('/pswd3')
@login_required
def pswd3():

    return render_template('medical officer/changepassword3.html')
@app.route('/addmed1',methods=['post'])
def addmed1():
    try:
        Name=request.form['textfield']
        Gender=request.form['radiobutton']
        Specialisation=request.form['select']
        place=request.form['textfield2']
        post=request.form['textfield3']
        Pin=request.form['textfield4']
        Contactno=request.form['textfield5']
        Email=request.form['textfield6']
        Username=request.form['textfield7']
        Password=request.form['textfield8']
        qry="insert into log values(null,%s,%s,'medical officer')"
        val=(Username,Password)
        id=iud(qry,val)
        qry1="INSERT INTO `medical` VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val1=(id,Name,Gender,Specialisation,place,post,Pin,Contactno,Email)
        iud(qry1,val1)
        return'''<script>alert("medical");window.location="/managemedical"</script>'''
    except Exception as e:
        return '''<script>alert("duplicate entry try again..");window.location="managemedical"</script>'''






@app.route('/addleg',methods=['post'])
def addleg():
    try:
        Name=request.form['textfield']
        Gender=request.form['radiobutton']
        place=request.form['textfield2']
        post=request.form['textfield3']
        Pin=request.form['textfield4']
        Contactno=request.form['textfield5']
        Email=request.form['textfield6']
        document=request.files['file']
        fname=secure_filename(document.filename)
        path=r"./static/documents"
        document.save(os.path.join(path,fname))
        Username=request.form['textfield8']
        Password=request.form['textfield9']
        qry="insert into log values(null,%s,%s,'legal officer')"
        val=(Username,Password)
        id=iud(qry,val)
        qry1="INSERT INTO legal_assistant VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val1=(id,Name,Gender,place,post,Pin,Contactno,Email,fname)
        iud(qry1,val1)
        return'''<script>alert("added legal_assistan successfully");window.location="managelegal"</script>'''
    except Exception as e:
        return '''<script>alert("duplicate entry try again..");window.location="managelegal"</script>'''


@app.route('/addedu1',methods=['post'])
def addedu1():
    try:
        name=request.form['textfield']
        place=request.form['textfield2']
        post=request.form['textfield3']
        Pin=request.form['textfield4']
        Contactno=request.form['textfield5']
        Email=request.form['textfield6']
        document=request.files['file']
        fname = secure_filename(document.filename)
        path = r"./static/documents"
        document.save(os.path.join(path, fname))

        qry1="INSERT INTO education VALUES(NULL,%s,%s,%s,%s,%s,%s,%s)"
        val1=(name,place,post,Pin,Contactno,Email,fname)
        iud(qry1,val1)
        return '''<script>alert("education");window.location="mnageedu"</script>'''
    except Exception as e:
        return '''<script>alert("duplicate entry try again..");window.location="mnageedu"</script>'''




@app.route('/addjob1',methods=['post'])
def addjob1():
    try:
        name=request.form['textfield']
        place=request.form['textfield2']
        post=request.form['textfield3']
        Pin=request.form['textfield4']
        Contactno=request.form['textfield5']
        Email=request.form['textfield6']

        qry1="INSERT INTO jobs VALUES(NULL,%s,%s,%s,%s,%s,%s)"
        val1=(name,place,post,Pin,Contactno,Email,)
        iud(qry1,val1)
        return'''<script>alert("jobs");window.location="job"</script>'''
    except Exception as e:
        return '''<script>alert("duplicate entry try again..");window.location="job"</script>'''




####################local coordinator code##################

@app.route('/changpss')
@login_required
def changpss():
    return render_template('local coordinator/changepassword2.html')



@app.route('/addaware',methods=['post'])
def addaware():
    return render_template('local coordinator/addawarenessprgm.html')
@app.route('/userreg')
@login_required
def userreg():
    return render_template('local coordinator/userregister.html')

@app.route('/manageawarenes')
@login_required
def manageawarenes():
    qry="SELECT * FROM awarness"
    res=selectall(qry)


    return render_template('local coordinator/manage awareness.html',val=res)










@app.route('/addloc1',methods=['post'])
def addloc11():
    try:
        Name=request.form['textfield2']
        gender=request.form['radiobutton']
        place=request.form['textfield4']
        post=request.form['textfield5']
        Pin=request.form['textfield6']
        Contactno=request.form['textfield11']
        Email=request.form['textfield5']
        area=request.form['textfield8']
        Username=request.form['textfield10']
        Password=request.form['textfield12']
        qry="insert into log values(null,%s,%s,'local coordinator')"
        val=(Username,Password)
        id=iud(qry,val)
        qry1="INSERT INTO `local_coordinator` VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val1=(str(id),Name,gender,place,post,Pin,Contactno,Email,area)
        iud(qry1,val1)
        return'''<script>alert("localcoordinator");window.location="/userreg"</script>'''
    except Exception as e:
        return '''<script>alert("duplicate entry try again..");window.location="manalocal"</script>'''


@app.route('/addloc2',methods=['get','post'])
def addloc2():
    try:
         name=request.form['textfield']
         description=request.form['textarea']
         date=request.form['textfield2']
         time=request.form['textfield3']
         venue=request.form['textfield4']
         qry="insert into `awarness` VALUES(NULL,%s,%s,%s,%s,%s,%s)"
         val=(str(session['lid']),name,description,date,time,venue)
         iud(qry,val)
         return'''<script>alert("events added successfully");window.location="/manageawarenes"</script>'''
    except Exception as e:
        return '''<script>alert("duplicate entry try again..");window.location="manageawarenes"</script>'''


@app.route('/addtrans2',methods=['get','post'])
@login_required
def addtrans2():
    return render_template("local coordinator/add transgen.html")

@app.route('/addtrns',methods=['get','post'])
def addtrns():
     name=request.form['textfield2']

     place=request.form['textfield4']
     post=request.form['textfield5']
     pin=request.form['textfield6']
     phno=request.form['textfield11']
     email=request.form['textfield6']
     photo=request.files['file']
     fn=secure_filename(photo.filename)
     photo.save(os.path.join("static/trans",fn))
     username=request.form['textfield10']
     password=request.form['textfield12']
     qry = "insert into log values(null,%s,%s,'user ')"
     val = (username, password)
     id = iud(qry, val)
     qry1 = "INSERT INTO `user` VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s)"
     val1 = (str(id),name,place,post,pin,phno,email,fn)
     iud(qry1, val1)
     return '''<script>alert("added");window.location="/addtrans2"</script>'''

@app.route('/addaware2',methods=['get','post'])
def addaware2():
     id=session['lid']

     name=request.form['textfield']

     descri=request.form['textarea']
     date=request.form['textfield2']
     time=request.form['textfield3']
     venue=request.form['textfield4']

     qry1 = "INSERT INTO `awarness` VALUES(NULL,%s,%s,%s,%s,%s,%s)"
     val1 = (str(id), name,descri, date,time,venue)
     iud(qry1, val1)
     return '''<script>alert("added");window.location="/manageawarenes"</script>'''




@app.route('/editaware2')
def editaware2():
    id = request.args.get('id')
    print(id)

    session['ppid'] = id
    qry = "SELECT * FROM `awarness` WHERE aw_id=%s"

    res = selectone(qry,str(id))

    print(res)
    return render_template('local coordinator/editawarenessprgm.html',val=res)


@app.route('/updateaware',methods=['post'])
def updateaware():

        id=session['ppid']
        name=request.form['textfield']
        description=request.form['textarea']

        date=request.form['textfield2']
        time=request.form['textfield3']
        venue=request.form['textfield4']


        qry="UPDATE `awarness` SET `aw_pgm_name`=%s,`aw_description`=%s,`aw_date`=%s,`aw_time`=%s,`aw_venue`=%s WHERE `aw_id`=%s"

        val=(name,description,date,time,venue, str(id))
        iud(qry,val)
        return'''<script>alert("updated successfully");window.location="manageawarenes"</script>'''



@app.route('/delevnt')
def delevnt():
    id=request.args.get('id')
    qry="DELETE FROM events WHERE et_id=%s"
    val=(str(id))
    iud(qry,val)
    return'''<script>alert("deleted");window.location="/event"</script>'''



@app.route('/addevent',methods=['post'])
@login_required
def addevent():
    return render_template('local coordinator/addevent.html')




@app.route('/addevent2',methods=['get','post'])
def addevent2():
    try:
         id=session['lid']
         name=request.form['textfield']
         descri=request.form['textarea']
         venue = request.form['textfield2']

         date=request.form['textfield3']
         time=request.form['textfield4']

         qry1 = "INSERT INTO `events` VALUES(NULL,%s,%s,%s,%s,%s,%s)"
         val1 = (str(id), name,descri,venue,date,time)
         iud(qry1, val1)
         return '''<script>alert("added");window.location="event"</script>'''
    except Exception as e:
        return '''<script>alert("duplicate entry try again..");window.location="event"</script>'''



@app.route('/password4',methods=['post'])
def password4():
    curpswrd=request.form['textfield']
    newpswrd=request.form['textfield2']
    confpswrd=request.form['textfield3']
    qry = "select * from log where password=%s and l_id=%s"
    val = (curpswrd, session['lid'])
    res = selectone(qry, val)
    if res is not None:
        if curpswrd == newpswrd:
            return '''<script>alert("password is same as current password");window.location="/"</script>'''
        elif newpswrd == confpswrd:
            qry = "UPDATE `log` SET `password`=%s WHERE l_id=%s"
            val = (newpswrd, session['lid'])
            iud(qry, val)

            return '''<script>alert("password  changed successfully");window.location="/coordinator"</script>'''
        else:
            return '''<script>alert("invalid password");window.location="/changpss"</script>'''
    else:
        return '''<script>alert("current password doesnot exist");window.location="/changpss"</script>'''



### legal assistance..................................###


@app.route('/addmeet1',methods=['post'])
def addmeet1():
    try:
         time=request.form['textfield']
         place=request.form['textfield2']
         description=request.form['textarea']

         qry="insert into `meeting` VALUES(NULL,%s,%s,%s,%s)"
         val=(str(session['lid']), time,place,description)
         iud(qry,val)
         return'''<script>alert("added successfully");window.location="leghome"</script>'''

    except Exception as e:
        return '''<script>alert("duplicate entry try again..");window.location="leghome"</script>'''

@app.route('/update', methods=['post'])
def update():

            time = request.form['textfield']
            place = request.form['textfield2']
            description = request.form['textarea']

            qry = "update `meeting` set mt_meeting_time=%s,mt_place=%s,mt_description=%s where mt_id=%s"
            val = ( time, place, description,str(session['ppid']))
            iud(qry, val)
            return '''<script>alert("added successfully");window.location="leghome"</script>'''




# @app.route('/addmeet2',methods=['get','post'])
# def addmeet2():
#      id=session['lid']
#      name=request.form['textfield']
#      descri=request.form['textarea']
#      place = request.form['textfield2']
#
#      date=request.form['textfield3']
#      time=request.form['textfield4']
#
#      qry1 = "INSERT INTO `events` VALUES(NULL,%s,%s,%s,%s,%s,%s)"
#      val1 = (str(id), name,descri,place,,time)
#      iud(qry1, val1)
#      return '''<script>alert("added");window.location="event"</script>'''










app.run(debug=True)

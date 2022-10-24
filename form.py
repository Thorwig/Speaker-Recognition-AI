import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
from flask import Flask, flash, request, render_template, session
from feat_extract import parse_audio_files
from feat_extract_predict import parse_predict_files
import numpy as np
import classifier
import os, shutil
import mysql.connector
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

with open('Parameters/database_parameters.json', encoding='utf-8') as f:
	data = json.load(f)


@app.route('/', methods =["GET", "POST"])
def root():
    return render_template("form.html")

@app.route('/enroll', methods=['POST'])
def enroll():
#transfrom from mp3 to wav and get name
    print('enroll function called')
    if os.path.exists('extracted_features/features.npy') & os.path.exists('extracted_features/labels.npy'):
        if not os.path.exists('data/'+ request.form.get('firstname') +'_'+request.form.get('lastname')):
            os.mkdir('data/'+request.form.get('firstname') +'_'+request.form.get('lastname'))

        file = request.files['file']

        input_name = 'enrollment_audio.mp3'
        file_name = 'data/'+ request.form.get('firstname') +'_'+request.form.get('lastname')+'/'+ input_name
        file.save(file_name)

        i = len(os.listdir('data/'+request.form.get('firstname') +'_'+request.form.get('lastname')))
        output_name = request.form.get('firstname') +'_'+request.form.get('lastname') + str(i+1) + '.wav'
        filename_output = 'data/'+ request.form.get('firstname') +'_'+request.form.get('lastname')+'/' + output_name

        os.system('ffmpeg -i '+file_name+ ' '+ filename_output)
        os.remove(file_name)
#feature extract
    features, labels = parse_audio_files('data')
    if os.path.exists('extracted_features/features.npy') & os.path.exists('extracted_features/labels.npy'):
        print('test..............................')
        dataF = np.load('extracted_features/features.npy')
        feat = np.append(dataF, features,axis=0)
        np.save('extracted_features/features.npy', feat)

        dataL = np.load('extracted_features/labels.npy')
        lab = np.append(dataL, labels,axis=0)
        np.save('extracted_features/labels.npy', lab)
        
        dir = 'data'
        for files in os.listdir(dir):
            path = os.path.join(dir, files)
            try:
                shutil.rmtree(path)
            except OSError:
                os.remove(path)
#insert name to database
        mydb = mysql.connector.connect(host=data['host'],user=data['user'],password=data['password'],database=data['database'])
        mycursor = mydb.cursor(buffered=True)
        label = np.load('extracted_features/labels.npy')[-1]
        sql = """INSERT INTO user_identify(id_user,first_name,last_name) VALUES(%s,%s,%s)"""
        val = (str(label), request.form.get('firstname'), request.form.get('lastname'))
        mycursor.execute(sql,val)
        mycursor.close()
#classification
        classifier.svm_classifier()
        # nn_classifier.nn_classify()
        return np.array2string(labels)
    else :
        np.save('extracted_features/features.npy', features)
        np.save('extracted_features/labels.npy', labels)
        dir = 'data'
        for files in os.listdir(dir):
            path = os.path.join(dir, files)
            try:
                shutil.rmtree(path)
            except OSError:
                os.remove(path)
#classification
        classifier.svm_classifier()
        # nn_classifier.nn_classify()
        return np.array2string(labels)


@app.route('/identify', methods=['POST'])
def identify():
#transform from mp3 to wav
    file = request.files['file']

    print(request.form.get('audioname'))
    file_name = 'predict/identification_audio.mp3'
    filename_output = 'predict/identification_audio.wav'
    file.save(file_name)
    os.system('ffmpeg -i '+file_name+ ' '+ filename_output)
    os.remove(file_name)
    
#feature extract
    features, filenames = parse_predict_files('predict')
    np.save('extracted_features/predict_features.npy', features)
    np.save('extracted_features/predict_labels.npy', filenames)

    os.remove('predict/identification_audio.wav')

#classification
    label,score = classifier.svm_predict()
    label = label[0]
    #label = nn_classifier.nn_predict()

    score = str(score)

    mydb = mysql.connector.connect(host=data['host'],user=data['user'],password=data['password'],database=data['database'])
    mycursor = mydb.cursor(buffered=True)
    mycursor.execute("""SELECT first_name, last_name FROM user_identify where id_user LIKE'"""+str(label)+"""'""")
    myresult_ = mycursor.fetchall()
    
    
    if len(myresult_)==0:
            myresult_ = [('Not available', 'Not available')]

    resp = {'first_name':myresult_[0][0], 'last_name':myresult_[0][1], 'score':score}
    mycursor.close()

    return resp

@app.route('/getlist', methods=['POST'])
def getlist():
#load list from database to front
    mydb = mysql.connector.connect(host=data['host'],user=data['user'],password=data['password'],database=data['database'])
    mycursor = mydb.cursor(buffered=True)   
    mycursor.execute("""SELECT id_user, first_name, last_name FROM user_identify""")
    myresult = mycursor.fetchall()
    users = []
    for x in myresult :
        users.append({'id':x[0], 'first_name':x[1], 'last_name':x[2]})
    mycursor.close()
#save list in json
    with open('static/templates/users.json', 'w') as f:
        json.dump(users,f,indent=2)
    return users

@app.route('/delete', methods=['POST'])
def delete():
#delete from database
    id_number = str(request.form.get('user_id'))
    mydb = mysql.connector.connect(host=data['host'],user=data['user'],password=data['password'],database=data['database'])
    mycursor = mydb.cursor(buffered=True)
    mycursor.execute("""DELETE FROM user_identify WHERE id_user LIKE'"""+id_number+"""'""")
    mycursor.close()
#Delete from extracted_features/features.npy & extracted_features/labels.npy
    datalabel = list(np.load('extracted_features/labels.npy'))
    datafeat = list(np.load('extracted_features/features.npy'))
    for x in datalabel:
        if x == int(id_number):
            index = datalabel.index(x)
            datalabel.pop(index)
            datafeat.pop(index)
            np.save('extracted_features/labels.npy',np.array(datalabel))
            np.save('extracted_features/features.npy',np.array(datafeat))

    return datalabel


if __name__=='__main__':
    app.run(use_reloader=True)
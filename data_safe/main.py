from re import A
from flask import Flask
from flask import request
from flask_cors import CORS
from dotenv import load_dotenv
import os
import json
import requests
import datetime
import threading
import sqlite3
import time

app = Flask(__name__)
CORS(app)
# open sqlite3 database
# check if database exists
if not os.path.exists('database.db'):
    # create database




    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    


    c.execute('''CREATE TABLE assessments (
	id INTEGER PRIMARY KEY,
	date TEXT,
    progress INT,
    total INT,
    speed INT,
    status INT
    );''')

    c.execute('''CREATE TABLE users (
	id INTEGER PRIMARY KEY,
	name TEXT,
    assessment_id INT,
    password TEXT,
    FOREIGN KEY(assessment_id) REFERENCES assessments(id)
    );''')

    c.execute('''CREATE TABLE words (
	id INTEGER PRIMARY KEY,
	word TEXT
    );''')


    conn.commit()
    conn.close()
    # end of open sqlite3 database

def getUpdatesUntilOver(date):
    status = "3"
    
     
    while status != "5":
        # make POST request to CRACKER_REMOTE_URL
        try:
            r = requests.get("http://adcracker/update")
            if r.status_code != 200:
                raise Exception(r.text)
            # response to json
            response = json.loads(r.text)
            total = response['total']
            progress = response['progress']
            status = response['status']
            temp = response['temp']
            speed = response['speed']
            #print all data
            print("Total: " + str(total))
            print("Progress: " + str(progress))
            print("Status: " + str(status))
            print("Temp: " + str(temp))
            print("Speed: " + str(speed))

            # update database
            conn = sqlite3.connect('database.db')
            c = conn.cursor()
            c.execute("UPDATE assessments SET progress = ?, total = ?, speed = ?, status = ? WHERE date=?", (str(progress), str(total), str(speed), str(status),date))
            conn.commit()
            conn.close()
            # end of update database
            # get status of newest assessment
            
            
        except Exception as e:
            print (e)

        # thread sleep for 2 seconds
        
        time.sleep(3)

        print("                        ")
          

    # make post request to CRACKER_REMOTE_URL
    r = requests.get("http://adcracker/result")
    if r.status_code != 200:
        return {"Error":  r.text}
    # response to json
    response = json.loads(r.text)
    user = response['user']

    # get newest assessment id from database
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT id FROM assessments ORDER BY id DESC LIMIT 1")
    id = c.fetchone()[0]
    conn.commit()
    conn.close()


    for i in user:
        print(i['username'])
        # insert user into database
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        #take first 3 characters of password and replace every other with *
        password = i['password']
        password = password[:3] + "*"*(len(password)-3)


        c.execute("INSERT INTO users VALUES (NULL, ?, ?, ?)", (i['username'], id,password))
        conn.commit()
        conn.close()
        # end of insert user into database





# flask endpoints
# create new assessment
@app.route('/createassessment', methods=['POST'])
def create_assessment():
    # get dc_ip and target from request from raw json
    data = request.get_json()
    dc_ip = data['dc_ip']
    target = data['target']
    
    print (dc_ip, target)
    # send POST request to SYNCER_REMOTE_URL
    
    
    r = requests.post("http://adsyncer/steal", json={'dc_ip': dc_ip, 'target': target})
    
    if r.status_code != 200:
        return {"Error":  r.text}
    # response to json
    response = json.loads(r.text)
    
    data = response['data']
    
    # split data at every new line
    data = data.split('\n')
    # remove empty lines
    data = [x for x in data if x != '']
    


    # send POST request to CRACKER_REMOTE_URL
    
     
    r = requests.post("http://adcracker/crack", json={'dump': data})
    if r.status_code != 200:
        return {"Error":  r.text}
    
    # response to json
    response = json.loads(r.text)
    try:
        data = response['lock']
        if data == "lock":
            return {"lock": "lock"}
    except Exception as e:
        print (e)
    state = response['state']
    

    # create assessment in database
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    # get current date as string
    date = str(datetime.datetime.now())
    c.execute("INSERT INTO assessments VALUES (NULL, ?, ?, ?,?,?)", (date, 0, len(data), 0, 3))
    conn.commit()
    conn.close()
    # end of create assessment in database
    # start thread to get updates until over
    x = threading.Thread(target=getUpdatesUntilOver, args=(date,))
    x.start()

    return {"state":  state}
    
@app.route('/state', methods=['POST'])
def get_new_assessment():
    # get newest assessment from database
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM assessments ORDER BY id DESC LIMIT 1")
    assessment = c.fetchone()
    conn.commit()
    conn.close()
    # end of get newest assessment from database

    return {"state":assessment}

# get newest assessment with all users
@app.route('/result', methods=['POST'])
def get_assessment():
    # get newest assessment from database
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM assessments ORDER BY id DESC LIMIT 1")
    assessment = c.fetchone()
    conn.commit()
    conn.close()
    # end of get newest assessment from database
    # get all users from database
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE assessment_id = ?", (assessment[0],))
    users = c.fetchall()
    conn.commit()
    conn.close()
    # end of get all users from database
    return {"assessment": assessment, "users": users}

@app.route("/addwords", methods=['POST'])
def add_words():
    data = request.get_json()
    field_input = data['field_input']
    
    r = requests.post("http://adcracker/addwords",json={'field_input': field_input})
    if r.status_code != 200:
        raise Exception(r.text)
    
    # loop through every line of field_input
    for i in field_input.split('\n'):
        # ad i into databse word
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("INSERT INTO words VALUES (NULL, ?)", (i,))
        conn.commit()
        conn.close()
        # end of ad i into databse word
    return {"success": "success"}



@app.route("/words", methods=['POST'])
def get_words():
    # get all words from database
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM words")
    words = c.fetchall()
    conn.commit()
    conn.close()
    # end of get all words from database
    return {"words": words}



# get all assessments 
@app.route('/assessments', methods=['POST'])
def get_all_assessments():
    # get all assessments from database with the user count
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM assessments")
    assessments = c.fetchall()
    conn.commit()
    conn.close()
    newList = []
    # Get the count of users for each assessment
    for i in assessments:
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("SELECT COUNT(*) FROM users WHERE assessment_id = ?", (i[0],))
        count = c.fetchone()[0]
        conn.commit()
        conn.close()

        i = i + (count,)
        newList.append(i)
    # end of get all assessments with the user count

    # end of get all assessments from database with the user count
    return {"assessments": newList}
     
@app.route('/getAssessment', methods=['POST'])
def getResulstOfAssessment():
    data = request.get_json()
    assessment_id = data['assessment_id']
    # get all users from database
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE assessment_id = ?", (assessment_id,))
    users = c.fetchall()
    conn.commit()
    conn.close()
    # end of get all users from database
    return {"users": users}
    

# start flask server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
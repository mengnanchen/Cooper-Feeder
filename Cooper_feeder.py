from flask import Flask
import json
import os
from datetime import datetime




app = Flask(__name__)
timelog = []


@app.route('/feedcooper')
def feedcooper():
    i = datetime.now()
    logline = 'cooper is fed at ' + i.strftime('%Y/%m/%d %H:%M')
    timelog.append(logline)
    savetimelog(logline)
    return json.dumps(timelog)

def savetimelog(logline):
    file = open("fedtimelog.txt", "a")
    file.write(logline+'\n')
    file.close()

def readtimelog():
    if os.path.isfile('./fedtimelog.txt') is False:
        file = open("fedtimelog.txt","x")
        file.close()
    file = open("fedtimelog.txt", "r")
    for line in file:
        timelog.append(line)
    file.close()
    return timelog


if __name__ == "__main__":

    listoflines = readtimelog()
    print(listoflines)
    app.run(host='127.0.0.1',port=8080,debug=True)


from flask import Flask
from datetime import datetime, timedelta

from utils import auth_required

try:
    from dotenv import load_dotenv
    load_dotenv()
except:
    print('no .env file, using external enviromental variable')

app = Flask(__name__)

def render_plan():
    file = open('tables.html','r')
    tables = file.read()
    tables = tables.replace('min-oversikt','table table-dark table-hover table-bordered')
    tables = tables.replace('<h2>','<h2 class="display-4 text-center">')
    tables = tables.replace('<p>','<p class="lead">')
    tables = tables.replace('BPA','') #Hvorfor skriver folk BPA inn i rubrikkene? 
    head = '<html><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">'
    head = head+ f'<title>BPA Arbeidsplan</title> <head>'
    html = head+'<body>'+tables+'</body></html>'
    return html

def check_data():
    file = open('tables.html','r')
    data = file.read()
    time_data = data.splitlines()[len(data.splitlines())-1]
    time_data = time_data.replace('<p>Extracted: ','')
    time_data = time_data.replace('</p>','')
    time_data_last_collected = datetime.strptime(time_data,"%Y-%m-%d %H:%M:%S.%f")
    time_since_last_update =  datetime.now()-time_data_last_collected
    print(str(time_since_last_update.total_seconds()/60/60))
    #print(time_data.hour)


@app.route('/')
@auth_required
def index():
    return render_plan()

if __name__ == '__main__':
    check_data()
    app.run(debug=True)
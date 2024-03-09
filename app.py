from flask import Flask, render_template
from datetime import datetime
import os

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
    file.close()
    tables = tables.replace('min-oversikt','table table-dark table-hover table-bordered text-light')
    tables = tables.replace('<h2>','<h2 class="display-4 text-center text-light">')
    tables = tables.replace('<p>','<p class="lead text-light">')
    tables = tables.replace('BPA','') #Hvorfor skriver folk BPA inn i rubrikkene? 
    table_html = '<div class="container"> <div class="mx-auto">' +tables+'</div></div>'
    return table_html

def check_data():
    try:
        file = open('tables.html','r')
        data = file.read()
        file.close()
        time_data = data.splitlines()[len(data.splitlines())-1]
        time_data = time_data.replace('<p>Extracted: ','')
        time_data = time_data.replace('</p>','')
        time_data_last_collected = datetime.strptime(time_data,"%Y-%m-%d %H:%M:%S.%f")
        time_since_last_update =  datetime.now()-time_data_last_collected
        #print(str(time_since_last_update.total_seconds()/60/60))
        # if the data is more than 6 hours old, rescrape data.
        if ( time_since_last_update.total_seconds()/60/60 >= 6 ):
            os.system('python main.py')

    except:
        print('No table data found, scraping again')
        os.system('python main.py')

@app.route('/')
@auth_required
def index():
    return render_template('index.html')

@app.route('/get_plan')
@auth_required
def get_plan():
    check_data()
    return render_plan()

if __name__ == '__main__':
    check_data()
    app.run()#debug=True)
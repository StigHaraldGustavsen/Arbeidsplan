from flask import Flask
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
    tables = tables.replace('min-oversikt','table table-dark table-hover table-bordered')
    tables = tables.replace('<h2>','<h2 class="display-4 text-center">')
    tables = tables.replace('<p>','<p class="lead">')
    tables = tables.replace('BPA','') #Hvorfor skriver folk BPA inn i rubrikkene? 
    head = '<html>\n<head>\n<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">'
    head = head+ f'<title>BPA Arbeidsplan</title> <head>'
    Body = '<body>' + '<div class="container"> <div class="mx-auto">' +tables+'</div></div></body></html>'
    html = head+Body
    return html

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
    check_data()
    return render_plan()

if __name__ == '__main__':
    check_data()
    app.run()#debug=True)
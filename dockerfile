FROM python:3.10

WORKDIR /app
COPY . /app
COPY .env /app/.env

RUN pip install --trusted-host pypi.python.org -r requirements.txt

RUN apt-get update && apt-get install -y unzip && \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt install -y ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb && \
    apt-get clean

COPY main.py /app/main.py

#Scripts to poetentally use, set them to excecutable.
RUN chmod +x /app/createEnviroment.sh
RUN chmod +x /app/main.py
RUN chmod +x /app/run_gunicorn.sh

EXPOSE 5000 

#Development RUN
#CMD ["poetry", "run", "flask", "--app", "webuncert/app", "run", "--port=5000","--host=0.0.0.0"]

#CMD [ "python", "app.py" ]

#Run FLASK application through gunicorn WSGI 
CMD ["./run_gunicorn.sh"]

#CMD ['gunicorn', '-w', '4', '-b', '0.0.0.0:5000', 'app:app']

#If you need to create a new .env file.
#CMD ["sh", "-c", 'echo', '"ULOBA_USERNAME=${ULOBA_USERNAME}"', '>', '.env', '&&', 'echo', '"ULOBA_PASSWORD=${ULOBA_PASSWORD}"', '>', '.env', '&&', 'cron', '-f']
#CMD ["sh", "-c", 'echo', '"ULOBA_USERNAME=${ULOBA_USERNAME}"', '>', '.env', '&&', 'echo', '"ULOBA_PASSWORD=${ULOBA_PASSWORD}"', '>', '.env', '&&', 'cron', '-f']
#CMD ["sh", '-c', './app/creatEnviroment.sh', '&&', 'cron', '-f']
#CMD ["./createEnviroment.sh", "&&", "cron", "-f"]

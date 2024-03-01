# Uloba workschedule sharing web application

BPA's of ulloba struggle with that they can only see their own shifts, and the manager needs to manually share the shift plan. This automats this.


but this web app collects the plan automatically on an irregular cadence. but several times a day if someone needs it. if it is not needed then it does not collect it either.

## Run the application in docker

change the enviromental variables in the -e parameters.
```bash
git clone https://github.com/StigHaraldGustavsen/Arbeidsplan.git
docker build -t arbeidsplan .
docker container run -d \
-p 5000:5000 \
-e ULOBA_USERNAME='username@mail.com' \ 
-e ULOBA_PASSWORD='the uloba password' \ 
-e EVERYONES_USERNAME='BPA' \ 
-e EVERYONES_PASSWORD='BPA_password' \
--restart unless-stopped \ 
arbeidsplan
```

Not it runns on http://localhost:5000, under a WSGI server, so if neede it can be put behind a webserver like Nginx or apache if so needs be. https is not yet enabled. so use http and not https, to get this to work. add https with your own web server.


```bash
git clone https://github.com/StigHaraldGustavsen/Arbeidsplan.git

# The username and password for the webscraping
export ULOBA_USERNAME='username@mail.com'
export ULOBA_PASSWORD='the uloba password'
# Web app spesific to share with the people using the app
export EVERYONES_USERNAME='BPA'
export EVERYONES_PASSWORD='BPA_password'

#Creates the .env file
chmod +x createEnviroment.sh
./createEnviroment.sh
#you can also just manually create a .env file, .env.bak is examle, but rename file to ".env"

docker build -t arbeidsplan .
docker container run --env-file .env --restart unless-stopped -d -p 1000:5000 arbeidsplan
```


## Run the application in local enviroment.

Run production application
```bash
chmod +x run_gunicorn.sh
./run_gunicorn.sh
```

Run develompent
```bash
poetry config virtualenvs.in-project true
poetry install
poetry run python app.py
poetry run python main.py

```

Single Scrape
```bash
poetry config virtualenvs.in-project true
poetry install
poetry run python main.py

```

```bash

```
if local not from docker file:
#### Activate the virtual environment
source /path/to/your/.venv/bin/activate


utils:

```bash
poetry export --without-hashes --format=requirements.txt > requirements.txt
```






# Create the docker file

```bash
docker build -t arbeidsplan_scraper .
docker container run -d -p 1000:5000 arbeidsplan_scraper
docker container run arbeidsplan_scraper
```




### docker utillities
```bash
docker image rm -f scraper
docker build -t scraper .
docker container run scraper
docker run -it -v ./temp:/app scraper


docker run -v scraper_volume:/app -d scraper
docker run --env-file .env -v scraper_volume:/app -d scraper

docker run -v scraper_volume:/app scraper

docker exec -it <container_id> bash
```


# Notes

add boostraps:
 <html>
 <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
 <head>
 </head>
 <body>
 
Tables

 </body>
 </html>


with the dump. replace all 
min-oversikt 
with 
table table-dark table-hover



#### docker volume

No need for volumes here, the tables are stored in the local web app.
```bash
docker volume prune -a
docker volume create my_volume
docker run -v my_volume:/app -d scraper

/var/lib/docker/volumes/my_volume/_data
docker volume inspect my_volume
cd /var/lib/docker/volumes/my_volume/_data
```

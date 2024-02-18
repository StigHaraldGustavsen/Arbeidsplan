

# Create the docker file

```bash
docker build -t arbeidsplan_scraper .
docker container run -d -p 1000:5000 arbeidsplan_scraper
docker container run arbeidsplan_scraper
```


#### docker volume
```bash
docker volume prune -a
docker volume create my_volume
docker run -v my_volume:/app -d scraper

/var/lib/docker/volumes/my_volume/_data
docker volume inspect my_volume
cd /var/lib/docker/volumes/my_volume/_data
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

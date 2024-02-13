

# Create the docker file

```bash
docker build -t arbeidsplan_scraper .
docker container run -d -p 1000:5000 arbeidsplan_scraper
docker container run arbeidsplan_scraper
```

### docker utillities
```bash
docker image rm -f arbeidsplan_scraper
docker build -t arbeidsplan_scraper .
docker container run arbeidsplan_scraper

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

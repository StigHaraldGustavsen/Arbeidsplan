

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
# Scraper code

utils:

```bash
poetry export --without-hashes --format=requirements.txt > requirements.txt
```
```bash
poetry config virtualenvs.in-project true
poetry install
```



```bash
poetry run python app.py
poetry run python main.py
```
if local not from docker file:
#### Activate the virtual environment
source /path/to/your/.venv/bin/activate


```bash
chmod +x run_gunicorn.sh
./run_gunicorn.sh
```
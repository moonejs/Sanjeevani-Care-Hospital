Welcome to the project MAD-II
Backend
---
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```


Run

`python app.py`


---
Frontend
`npm install`


---

`redis-server`

`MailHog`

`python app.py`

`celery -A app.celery worker --concurrency=1 --loglevel=info`

`celery -A app.celery beat --loglevel=info`

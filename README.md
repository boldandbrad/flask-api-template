# Flask API Template

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/b6e816cf534bbe741de7)

## About

Spin up and deploy a new flask REST api quickly.

## Local Setup

Make sure you have [Python 3x](https://www.python.org/) and [pip](https://pip.pypa.io/en/stable/installing/) installed.

```bash
git clone https://github.com/bradleycwojcik/flask-template.git
cd flask-template
pip install -r requirements.txt
python api/app.py
```

The web server is now be running on `http://localhost:5000`

## Deploy to Heroku

Install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).

From within the repository directory:

```bash
heroku create
git push heroku dev
heroku open
```

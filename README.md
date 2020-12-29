# Tribes Data Transporter (TDT)

Tribes Data Transporter(TDT) would be a simple flask app(with python3.7) which would be
running daily at a fixed time and would be responsible for reading JSON data from ​google
cloud storage and writing the data in Azure’s cosmos db with Gremlin API.

## Required Libraries

* gsutil
* gremlinpython==3.2.6
* flask
* apscheduler

To install the requirements, run the command `pip install requirements.txt`

## About the app

To run the app, just run the command `python app.py`. It will start a flask application server which will run the script `main.py` either daily, or at a regular interval as specified to the *background scheduler*.

For demonstration of this app, for now I have set an interval of 10 minutes. So, after starting the app, after 10 minutes, it will run the `main.py` script for the first time where the files will get downloaded and queries will get executed on the database. Again, after another 10 minutes, the script will execute and display the message as `no new files found`.

> Note: The command used to execute `main.py` in `app.py` is `python main.py`. If your system has different versions of python and you need to specify python3, just replace the command in line 7 in `app.py` from `python main.py` to `python3 main.py`.

> `config.py` contains bucket information and database details along with some utility functions to query the database.
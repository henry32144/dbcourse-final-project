Database 期末專案 - Database course final project
===============================
這是資料庫課程的期末專案，為了方便展示，Operation Console只有Select操作能用。


Demo
===============================



Built With
===============================
在這個應用中使用了以下框架、庫:

前端:
*  [Bootstrap4](https://v4-alpha.getbootstrap.com/)
*  [Bootstrap-html-template](https://github.com/BlackrockDigital/startbootstrap-sb-admin)
*  [Jquery](https://jquery.com/)
*  [Jinja2](http://jinja.pocoo.org/docs/2.10/)

後端:
*  [Python3.6](https://www.python.org/downloads/)
*  [Flask](http://flask.pocoo.org/)
*  [SQLAlchemy](https://www.sqlalchemy.org/)

資料庫:
*  [SQlite3](https://www.sqlite.org/)

如何使用
==============================
try it on Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)


### Local server ( Windows )

先裝好python 3 (這個編寫環境是3.6)

開啟cmd到這個資料夾後，輸入
```
pip -r requirements.txt
```
裝好後,輸入
```
python app.py
```
即可開啟local server


注意
==============================
為了方便管理，所以限制了使用者輸入只能使用SELECT，其他如Database操作都會被過濾掉(如CREATE,DELETE...)。


作者
==============================
[Henry](https://github.com/henry32144)


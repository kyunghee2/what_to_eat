# what_to_eat
2019 4차산업혁명 선도인력 양성과정 해피해킹 최종 프로젝트

## 설정방법

#### requirements install
```bash
$ pip install -r requirements.txt
```

#### python installed packages
```bash
$ pip install django==2.2.6

$ pip install django-extensions
$ pip install django-bootstrap4
$ pip install pylint-django

$ pip install python-decouple
$ pip install python-telegram-bot

$ pip install mysql-connector
$ pip install django-mysql
$ pip install ./lib/mysqlclient‑1.4.6‑cp38‑cp38‑win_amd64.whl
```

#### mysqlclient 다운로드 사이트
- python 버전 & bit 일치하는 것 확인 후 다운로드 및 설치
```
https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient
```

#### db migrate
```bash
$ pip manage.py migrate
```

#### admin 계정생성 
```bash
$ python manage.py createsuperuser
```
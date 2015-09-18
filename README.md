Development
===========

## Install

- Install python dependencies
```
pip install -r requirements.txt
```

- Python server
```
cd src
python manage.py runserver
```

- Install node dependencies
```
npm install
npm install -g gulp
```

- Static files watcher
```
gulp
```

## Load fixtures

```
python manage.py loaddata auth_relationship
```

## i18n

1. Make messages (`django.po`): Runs over the entire source tree of the current directory and pulls out all strings marked for translation.
```
python manage.py makemessages -l es_AR
```
2. Edit messages in the `django.po` file
3. Compile messages (`django.mo`)
```
python manage.py compilemessages -l es_AR
```

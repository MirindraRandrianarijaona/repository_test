# Environment and dependencies installation
```
python -m venv .venv
.venv\Scripts\activate
.venv\Scripts\python -m pip install -r requirements.txt
cd train\theme\static_src
npm install
```

# Deployment in development
bash 01 : 
```
.venv\Scripts\activate
cd train
python manage.py tailwind start
```
bash 02 :
```
.venv\Scripts\activate
cd train
python manage.py runserver

```
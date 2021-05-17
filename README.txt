SETUP REDIS
Install redis server and start the server

SETUP FRONTEND
npm install
npm run serve

SETUP BACKEND
pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py crontab add
python3 manage.py runserver

.PHONY: run
flask:
	flask --app flaskr run -h 0.0.0.0 --debug --reload

gunicorn:
	gunicorn -k gevent   -b 0.0.0.0:5000 'flaskalpr:create_app()'

wait:
	waitress-serve  --port=5000 --call 'flaskalpr:create_app'	

db_init:	
	flask --app flaskr init-db

default_user:	
	python3 flaskalpr/scripts/default_user.py 

clean: 
	rm flaskalpr/static/alprd1_images/*.jpg



#gunicorn --bind 0.0.0.0 --timeout 600 --access-logfile '-' --error-logfile '-' 'flaskalpr:create_app'	 
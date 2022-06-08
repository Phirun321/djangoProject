## initial project
##create folder 
#cd 
### 1.create vitaul environment : 
	# run : python -m venv env_name
### 2.use gitbush or powershell : 
	### activate env : 
		#run : source env_name/Script/activate 
	##for mac : 
		##run : source env_name/bin/activate
### 3.installing django :
	#cd to folder path-> run : python -m pip install Django
### 4.create django project : 
	#run : django-admin startproject project_name
### 5.folder structure : 
	-env_name
	-project_name:
		|-project_name
			|-__pycache__
			|-__init__.py
			|-asgi.py
			|-setting.py
			|-urls.py
			|-wsgi.py
		|-manage.py
		|-db.sqlite3
### 6.run project : 
	#run : python manage.py migrate
	#run : python manage.py runserver (defautl port => localhost:8000)

### Create admin ::
##run : python manage.py createsuperuser
### create app ::
#run : python manage.py startapp app_name
#add 'app_name' at INSTALL_APP section in setting.py file 


### file located :
	#model: is at model.py file
	#view: is at view.py file
	#template: is at template folder

###see more detail about migrations 'https://docs.djangoproject.com/en/4.0/topics/migrations/'
###see more about django 'https://docs.djangoproject.com/en/4.0/'

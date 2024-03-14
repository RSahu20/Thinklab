
1) Use a representative image of the cell (to be uploaded by the
user)
2) Generated a unique 10-digit Cell_ID and a Bar Code automatically and use
it as a unique identifier for the cell.

3) The page  have option to enter the meta information and electric parameters.

4) The webpage have an option to upload the data from a file:

5) After uploading the data, the webpage will transform the data to
produce the results listed below using this python library

## Installation 
 Use git commands to copy repo

#Create a Virtual Environment and install Dependencies.
If you don't have the virtualenv command yet, you can find installation instructions here. Learn more about Virtual Environments.
$ pip install virtualenv

#Create a new Virtual Environment for the project and activate it.

$ virtualenv venv
$ source venv/bin/activate

## Install requirements

```
pip install -r requirements.txt
```
## Database

```
Set the database from settings.py
```

## To migrate the database open terminal in project directory and type
```
python manage.py makemigrations
python manage.py migrate
```


## Collects all static files in your apps
```
python manage.py collectstatic
```

## Run the server
```
python manage.py runserver
```

# Main directory file

*   `battery_project`
 * `urls.py` - path reference to the app URLs
 * default django project files, such as: `settings.py`, `wsgi.py`, `asgi.py` etc.
		* `battery_app` - app directory
		


  * `static` - directory containing the JavaScript and CSS files inside the app directory within
        
  * `templates` - directory containing the HTML templates inside the app directory within
   
  * `manage.py` - default django file
  * `README.md` - this readme file
## Easyway Backend

# Navigate to easyway_backend folder
# create virtual environment and activate it

-------------------------------------
-- python -m venv venv
-- source venv/bin/activate
--------------------------------------
# Install requirements
-- pip install -r dev_requirements.txt
--------------------------------------

# Makemigrations
python manage.py makemigrations
python manage.py migrate

# Create superuser to monitor models fromadmin page
python manage.py createsuperuser

# Runserver
python manage.py runserver



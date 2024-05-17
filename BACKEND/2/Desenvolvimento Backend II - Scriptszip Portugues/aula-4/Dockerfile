FROM python:3.12

# DJANGO 

RUN python -m venv ./venv
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

WORKDIR /django

COPY ./referencial/django-produtos/ .

RUN /venv/bin/pip install -r requirements.txt

# RUN /venv/bin/python manage.py makemigrations
# RUN /venv/bin/python manage.py migrate
# CMD ["/venv/bin/python", "manage.py", "runserver", "0.0.0.0:8000"]

ENTRYPOINT [ "/entrypoint.sh" ]



# FAST API

# RUN python -m venv ./venv

# WORKDIR /fastapi

# COPY ./referencial/fastapi-produtos/requirements.txt .

# RUN /venv/bin/pip install -r requirements.txt

# CMD ["/venv/bin/uvicorn", "app:app", "--reload", "--host", "0.0.0.0", "--port", "4000"]
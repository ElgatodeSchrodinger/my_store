FROM tiangolo/uvicorn-gunicorn:python3.8-slim

COPY requirements.txt requirements.txt
RUN apt-get update
RUN apt-get install python-tk -y
RUN pip install -r requirements.txt

EXPOSE 8000

COPY ./app /app/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
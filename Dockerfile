FROM python:3.10.1
WORKDIR /flask-api
COPY requirements.txt . 
RUN pip install -r requirements.txt
COPY ./reply-api.py ./reply-api.py
EXPOSE 9090
CMD ["gunicorn", "-b", "0.0.0.0:9090", "reply-api:app"]
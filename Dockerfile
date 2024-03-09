FROM python:latest

WORKDIR /app

COPY api.py .

RUN pip install Flask flask-cors

EXPOSE 80

CMD ["python", "api.py"]

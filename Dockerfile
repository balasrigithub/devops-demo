FROM python:3.9-slim
ENV PYTHONUNBUFFERED True
COPY main/ /main/
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN python -c "import nltk; nltk.download('popular', download_dir='/home/nltk_data')"
CMD exec gunicorn --bind :$PORT --workers 1 --thread 8 --timeout 0 "main.app:create_app()"
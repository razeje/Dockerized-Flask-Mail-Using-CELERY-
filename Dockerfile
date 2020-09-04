
FROM python:3

WORKDIR ./celery
COPY .  /celery
RUN pip install -r /celery/requirements.txt

#RUN chmod +x /celery/entrypoint.sh
CMD ["python", "flasksmtp.py"]
#ENTRYPOINT["/celery/entrypoint.sh"]

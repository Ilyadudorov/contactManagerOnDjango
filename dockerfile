FROM python:3.11-alpine

RUN mkdir -p /home/app/web

ENV HOME=/home/app
ENV APP_HOME=/home/app/web

RUN mkdir $APP_HOME/staticfiles

WORKDIR $APP_HOME

# переменные окружения для python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt ./

RUN apk add ca-certificates

RUN pip install -r requirements.txt

# copy project
COPY . $APP_HOME

RUN sed -i 's/\r$//g' $APP_HOME/entrypoint.sh
RUN chmod +x $APP_HOME/entrypoint.sh


# run entrypoint.sh
ENTRYPOINT ["/home/app/web/entrypoint.sh"]

#EXPOSE 8080
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]

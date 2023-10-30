FROM python:3.11

RUN mkdir -p /home/app/web

RUN addgroup app 
RUN useradd -g app app

ENV HOME=/home/app
ENV APP_HOME=/home/app/web

RUN mkdir $APP_HOME/staticfiles

WORKDIR $APP_HOME

# переменные окружения для python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt ./

RUN apt-get install ca-certificates

RUN pip install -r requirements.txt


# copy entrypoint.sh
# COPY ./entrypoint.sh $APP_HOME


# copy project
COPY . $APP_HOME

RUN sed -i 's/\r$//g' $APP_HOME/entrypoint.sh
RUN chmod +x $APP_HOME/entrypoint.sh

RUN chown -R app:app $APP_HOME

USER app

# run entrypoint.sh
ENTRYPOINT ["/home/app/web/entrypoint.sh"]

#EXPOSE 8080
#нижняя команда нужна только если нет docker-compose.yml
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
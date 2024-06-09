FROM python:3.11

RUN mkdir /code_wars

WORKDIR /code_wars

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x /code_wars/docker/*.sh

EXPOSE 8000

CMD ["/code_wars/docker/app.sh"]
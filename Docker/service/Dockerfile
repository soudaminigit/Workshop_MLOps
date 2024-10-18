FROM python:3.9
COPY . /usr/app/service/
WORKDIR /usr/app/service/
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python deploy.py
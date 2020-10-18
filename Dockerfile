FROM python:3.7.4
WORKDIR /insights-backend
ADD . /insights-backend
RUN pip3 install -r requirements.txt
ENV FLASK_APP=main
CMD ["python","-m","flask","run"]
FROM redhat/ubi8

RUN dnf -y install python39

ADD requirements.txt .
ADD app.py .

RUN pip3 install -r requirements.txt

CMD ["python3","app.py"]
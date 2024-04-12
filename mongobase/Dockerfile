FROM python:alpine
WORKDIR /mongobase
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY database.py /mongobase
ENTRYPOINT [ "python", "database.py"]
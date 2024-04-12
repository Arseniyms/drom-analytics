FROM python:alpine
WORKDIR /analytics
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY drom_analytics.py /analytics
ENTRYPOINT [ "python", "drom_analytics.py"]
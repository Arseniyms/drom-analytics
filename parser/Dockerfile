FROM python:alpine
WORKDIR /parser
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY parser.py /parser
ENTRYPOINT [ "python", "parser.py"]
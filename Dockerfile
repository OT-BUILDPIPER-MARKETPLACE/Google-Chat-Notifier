FROM python:3.10-slim

ENV BODY ""

ENV GCHAT_URL ""

WORKDIR /code

COPY chat1.py /code/chat1.py

RUN pip install httplib2

RUN pip install requests

RUN pip install -U Jinja2

CMD ["python3", "chat1.py"]

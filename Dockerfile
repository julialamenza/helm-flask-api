FROM python:3.8.0b3-alpine3.10

WORKDIR /app/

COPY requirements.txt /app/
RUN pip install -r ./requirements.txt

COPY api.py /app/

EXPOSE  8075

CMD ["python", "api.py"]

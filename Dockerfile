# python
FROM python:3.8.1

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 3000
ENTRYPOINT ["python", "/code/main.py"]

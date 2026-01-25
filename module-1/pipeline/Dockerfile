FROM python:3.12-slim
RUN pip install pandas pyarrow
WORKDIR /app
COPY script.py script.py
ENTRYPOINT ["python", "script.py"]

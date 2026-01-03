FROM python:3.8-slim

WORKDIR /app

RUN pip install --no-cache-dir flask redis

COPY . .

EXPOSE 5002

CMD ["python", "flaskapp.py"]




















# FROM python:3.8-slim

# WORKDIR /app

# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# COPY . .

# EXPOSE 5002

# CMD ["python", "flaskapp.py"]


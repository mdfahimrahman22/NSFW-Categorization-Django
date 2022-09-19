FROM python:3.7
ENV PYTHONUNBUFFERED=1
RUN pip install --upgrade pip

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

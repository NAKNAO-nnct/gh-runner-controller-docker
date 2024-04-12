FROM python:3.12-alpine

WORKDIR /app

RUN pip install --upgrade setuptools
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# RUN apk add --no-cache curl docker-cli

COPY . .

# CMD ["tail", "-f", "/dev/null"]
CMD ["python", "-u", "app.py"]

FROM python:3.7
WORKDIR /app
COPY . .
RUN pip3 install -U -r requirements.txt

# ENV PYTHONBUFFERED 1
# ENV GOOGLE_CLOUDSDK_ACCOUNT_FILE "/creds.json"
# ENV GOOGLE_APPLICATION_CREDENTIALS "/creds.json"
# CMD make start-hello-world

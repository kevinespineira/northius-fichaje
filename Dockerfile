FROM mcr.microsoft.com/playwright/python:v1.39.0-jammy

WORKDIR /usr/src/app

COPY main.py .

CMD [ "python", "./main.py" ]

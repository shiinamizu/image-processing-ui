FROM python:3.9
WORKDIR /app
COPY . .
RUN apt -y update && apt -y upgrade
RUN apt -y install libopencv-dev
RUN pip install fastapi uvicorn
RUN pip install -r requirements.txt


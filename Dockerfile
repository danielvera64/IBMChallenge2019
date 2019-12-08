FROM python:3.7.5

RUN git clone https://github.com/zakumito/IBMChallenge2019.git /app/

WORKDIR /app

ENV SERVER_NAME 0.0.0.0:5000

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./api.py" ]

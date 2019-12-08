FROM python:3.7.5

RUN git clone https://github.com/zakumito/IBMChallenge2019.git /app/

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./api.py" ]

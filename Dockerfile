FROM python:3

WORKDIR C:/Users/Micael/Desktop/Projects/win_name

COPY . .

RUN pip install pyinstaller==6.9.0

CMD [ "python", "./main.py" ]
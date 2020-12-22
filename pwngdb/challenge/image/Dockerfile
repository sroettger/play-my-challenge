FROM kctf-nsjail

RUN apt-get update && apt-get install -y python3 python3-pip gdbserver

RUN mkdir /home/user

COPY requirements.txt /home/user/
RUN python3 -m pip install -r /home/user/requirements.txt && rm /home/user/requirements.txt

COPY flag gunicorn.conf.py pwngdb.py gdbproc.py index.html socket.io.min.js /home/user/

CMD cd /home/user && gunicorn -c gunicorn.conf.py -b :1337 pwngdb:app

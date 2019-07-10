FROM python:3

COPY app /tmp

WORKDIR /tmp

RUN pip install requests && chmod +x troller.py

VOLUME ["/var/log/troller/"]

CMD ["./troller.py"]

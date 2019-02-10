FROM frolvlad/alpine-python3

#RUN apk add wget bash man python3 pip3

COPY app /tmp

WORKDIR /tmp

RUN pip install requests && chmod +x troller.py

VOLUME ["/var/log/troller/"]

CMD ["./troller.py"]

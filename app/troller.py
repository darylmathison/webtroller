#!/usr/bin/env python3

import time
import requests


def main():
    with open("/var/log/troller/time.log", "w") as log, open("uri.list") as urls:
        for url in urls:
            starttime = time.time()
            requests.get(url, headers={"Accept": "application/json"})
            endtime = time.time()

            log_statment = "url -> {url}, start-> {starttime}, end -> {endtime}, difference -> {diff}".format(
                url=url, starttime=starttime, endtime=endtime, diff=endtime - starttime
            )
            print(log_statment)
            log.write(log_statment + "\n")
            time.sleep(30)


if __name__ == '__main__':
    main()

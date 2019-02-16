#!/usr/bin/env python3

import time
import requests


def main():
    with open("/var/log/troller/time.log", "w") as log, open("uri.list") as urls:
        for url in urls:
            starttime = time.time()
            requests.get(url, headers={"Accept": "application/json"})
            endtime = time.time()

            log_statement = f'url -> {url}, start-> {starttime}, end -> {endtime}, difference -> {endtime - starttime}'
            print(log_statement)
            log.write(log_statement + "\n")
            time.sleep(30)


if __name__ == '__main__':
    main()

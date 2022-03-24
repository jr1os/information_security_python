import os
import time


with open("hosts.txt", "r") as file:
    dump = file.read()
    dump = dump.splitlines()
    for ip in dump:
        os.system(f'ping -c 4 {ip}')
        time.sleep(4)

import os
import shutil
import time
import re
from threading import Timer

__version__ = "1.1.2"

def run_lt(port: int, subdomain: str = None):
    if not shutil.which('lt'):
        os.system('npm install -g localtunnel')
    command = f'lt -p {port}'
    if subdomain != None:
        subdomain = subdomain.strip()
        subdomain = subdomain.replace('.', '-')
        subdomain = subdomain.replace(' ', '-')        
        if re.match(r"^[\w-]+$", subdomain):
            command += f' -s {subdomain.lower()}'
    output = os.system(command)
    return output

def start_lt(port: int, subdomain: str = None):
    lt_adress = run_lt(port, subdomain)
    print(lt_adress)

def run_with_lt(app, subdomain: str = None):
    old_run = app.run

    def new_run(*args, **kwargs):
        port = kwargs.get('port', 5000)
        thread = Timer(1, start_lt, args=(port, subdomain,))
        thread.setDaemon(True)
        thread.start()
        old_run(*args, **kwargs)
    app.run = new_run

import os
import time
import shutil
from threading import Timer

__version__ = "1.0.4"

def run_lt(port):
	if not shutil.which('lt'):
		os.system('sudo npm install -g localtunnel')
	output = os.system(f'lt -p {port}')
	return output

def start_lt(port):
	lt_adress = run_lt(port)
	print(lt_adress)

def run_with_lt(app):
    old_run = app.run

    def new_run(*args, **kwargs):
        port = kwargs.get('port', 5000)
        thread = Timer(1, start_lt, args=(port,))
        thread.setDaemon(True)
        thread.start()
        old_run(*args, **kwargs)
    app.run = new_run
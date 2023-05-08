from threading import Timer
from py_localtunnel.lt import run_localtunnel

__version__ = "1.0.6"

def run_lt(port: int, subdomain: str = None):
    run_localtunnel(port, subdomain)

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
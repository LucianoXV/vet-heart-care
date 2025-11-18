import subprocess
import webbrowser
import os
import platform
import time

def start_django():
    # Start Django server
    subprocess.Popen(["python3", "manage.py", "runserver"])

    # Delay for server startup
    time.sleep(2)

    # Open web browser to access the app
    webbrowser.open("http://127.0.0.1:8000")

if __name__ == "__main__":
    os.chdir("/Users/lucianoxveiga/Documents/vetproject")  # Change directory to your Django app
    start_django()

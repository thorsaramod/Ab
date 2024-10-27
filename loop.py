import os
import signal
import time
import subprocess


# Join :- @GOKU_VAMPIRE # Set the path to the script you want to restart
script_to_restart = "m.py"

def restart_script():
    # Join :- @GOKU_VAMPIRE # Run the script
    print("@GOKU_VAMPIRE ka ddos hai bc.....")
    process = subprocess.Popen(["python3", script_to_restart], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return process

def main():
    process = restart_script()
    while True:
        time.sleep(30)  # Join :- @GOKU_VAMPIRE # Sleep for 30 seconds
        # Join :- @GOKU_VAMPIRE # Send Ctrl+C signal to the process
        process.send_signal(signal.SIGINT)
        # Join :- @GOKU_VAMPIRE # Wait for the process to terminate
        process.wait()
        # Join :- @GOKU_VAMPIRE # Restart the script
        process = restart_script()

if __name__ == "__main__":
    main()
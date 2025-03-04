import subprocess
from datetime import datetime

def process_test(args, inputs):
    args.extend(inputs)
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
    
    try:
        for output in process.stdout:
            print(f'---------- {datetime.now()} ------------')
            print(output.strip())
            print('--------------------------------------------------\n')
    except Exception as e:
        print(f"Error while reading the output: {e}")

    process.wait()

    error = process.stderr.read()
    if error:
        print("Error on process")
        print(error)

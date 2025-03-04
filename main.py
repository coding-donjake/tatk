from tat.directory import select_folder
from tat.process import process_test

root_folder = 'configuration'
portfolio = None
application = None
program = None

args = ['python', './test/module 1/program1.py']
inputs = ['input 1', 'input 2']

while True:
    if portfolio is None:
        print('\n--------------- List of portfolios ---------------')
        portfolio = select_folder(f'./{root_folder}', 'portfolio')
        
    elif application is None:
        print('\n-------------- List of applications --------------')
        application = select_folder(f'./{root_folder}/{portfolio}', 'application')
        
        if application is None:
            portfolio = None
        
    elif program is None:
        print('\n---------------- List of programs ----------------')
        program = select_folder(f'./{root_folder}/{portfolio}/{application}', 'application')
        
        if program is None:
            application = None
        
    if portfolio != None and application != None and program != None:
        break

command=""
started= True
while True:
    command=input('enter')
    if command.lower()=='start':
        if started:
            print('car already started')
        else:
            started=True
            print('start the car')
    elif command.lower()=='stop':
        if not started:
            print('car already stopped')
        else:
            started=False
            print('car stopped')
    elif command.lower()=='help':
        print("""
start:
stop:
exit:
        """)
    elif command.lower()=='exit':
        break
    else:
        print('wrong')
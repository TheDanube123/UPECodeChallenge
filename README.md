
Simply install IDLE.app 3.7. Open the file oldTryCodeWithWhile.py on IDLE. Click RUN, RUN MODULE.

Put this in module:
getReq = requests.get('http://ec2-34-216-8-43.us-west-2.compute.amazonaws.com/game?token=' + str(postReq.json()['token']))

Then put this in module:
getReq.json()

It will return:

{'maze_size': None, 'current_location': None, 'status': 'FINISHED', 'levels_completed': None, 'total_levels': None}

Therefore it has finished :)

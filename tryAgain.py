import requests

def move(direction):
    postReqMove = requests.post('http://ec2-34-216-8-43.us-west-2.compute.amazonaws.com/game?token=' + str(postReq.json()['token']), {'action':direction})
    return str(postReqMove.json()['result'])

def bounds(maxRow,maxColumn,curRow,curColumn):
    if (curRow >= maxRow):
        return False
    elif (curRow < 0):
        return False
    elif (curColumn >= maxColumn):
        return False
    elif (curColumn < 0):
        return False
    else:
        return True

def mazeSolver(curRow, curColumn, visited):
    if bounds(len(visited), len(visited[0]), curRow + 1, curColumn):
        if not visited[curRow +1][curColumn]:
            response = move('DOWN')
            visited[curRow +1][curColumn] = 1
            if response == 'END':
                return True
            elif response == 'SUCCESS':
                end = mazeSolver(curRow +1, curColumn, visited)
                if not end:
                    moveBack = move('UP')
                elif end:
                    return True
    if bounds(len(visited), len(visited[0]), curRow, curColumn + 1):
        if not visited[curRow][curColumn + 1]:
            response = move('RIGHT')
            visited[curRow][curColumn +1] = 1
            if response == 'END':
                return True
            elif response == 'SUCCESS':
                end = mazeSolver(curRow, curColumn + 1, visited)
                if not end:
                    moveBack = move('LEFT')
                elif end:
                    return True
    if bounds(len(visited),len(visited[0]),curRow - 1,curColumn):
        if not visited[curRow - 1][curColumn]:
            response = move('UP')
            visited[curRow-1][curColumn] = 1
            if response == 'END':
                return True
            elif response == 'SUCCESS':
                end = mazeSolver(curRow - 1,curColumn,visited)
                if not end:
                    moveBack = move('DOWN')
                elif end:
                    return True
    if bounds(len(visited),len(visited[0]),curRow,curColumn - 1):
        if not visited[curRow][curColumn - 1]:
            response = move('LEFT')
            visited[curRow][curColumn-1] = 1
            if response == 'END':
                return True
            elif response == 'SUCCESS':
                end = mazeSolver(curRow, curColumn -1,visited)
                if not end:
                    moveBack = move('RIGHT')
                elif end:
                    return True
    else:
        return False






postReq = requests.post('http://ec2-34-216-8-43.us-west-2.compute.amazonaws.com/session', {'uid': '004786138'})
getReq = requests.get('http://ec2-34-216-8-43.us-west-2.compute.amazonaws.com/game?token=' + str(postReq.json()['token']))
maxRow = getReq.json()['maze_size'][0]
maxColumn = getReq.json()['maze_size'][1]
startingPointRow = getReq.json()['current_location'][0]
startingPointColumn = getReq.json()['current_location'][1]
visited = [[0]*maxColumn for i in range(maxRow)]
answer = mazeSolver(startingPointRow, startingPointColumn, visited)
print(answer)

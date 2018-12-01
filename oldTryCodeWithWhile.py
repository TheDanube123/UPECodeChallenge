import requests

def move(direction):
    data2 = {'action': direction}
    urlB = 'http://ec2-34-216-8-43.us-west-2.compute.amazonaws.com/game?token=' + str(postReq.json()['token'])
    postReqMove = requests.post(url = urlB, data = data2, headers = headers)
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
                #print(str(curRow) + "," + str(curColumn))
                #print(getReq.json()['current_location'])
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
    return False

urlBase = 'http://ec2-34-216-8-43.us-west-2.compute.amazonaws.com/session'
data = {'uid': '004786138'}
headers = {"content type": "application/x-ww-form-urlencoded"}
postReq = requests.post(url = urlBase, data = data, headers = headers)
i = 1

while (i != 6):
    getReq = requests.get('http://ec2-34-216-8-43.us-west-2.compute.amazonaws.com/game?token=' + str(postReq.json()['token']))
    maxColumn = getReq.json()['maze_size'][0]
    maxRow = getReq.json()['maze_size'][1]
    startingPointColumn = getReq.json()['current_location'][0]
    startingPointRow = getReq.json()['current_location'][1]
    visited = [[0]*maxColumn for i in range(maxRow)]
    answer = mazeSolver(startingPointRow, startingPointColumn, visited)
    print(answer)
    i = i + 1





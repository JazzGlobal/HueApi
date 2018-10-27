# The script includes functions to interact with your Hue system


import requests


apiPrefix = 'FOLLOW TUTORIAL'
user = 'FOLLOW TUTORIAL'


def MakeRequest(type, requestString="", data=""):
    url = apiPrefix + requestString
    print(url)
    if(type == 'GET'):
        response = requests.get(url, data)
        print(response.json())
    elif(type == 'POST'):
        response = requests.post(url, data)
        print(response.json())
    elif(type == 'PUT'):
        pass
    else:
        print("Invalid Usage of \"MakeRequest(type, requestString, data)\"")


def UserRequest(type, requestString="", data=""):
    url = apiPrefix + user + requestString
    print(url)
    if(type == 'GET'):
        response = requests.get(url, data)
        return response.json()
    elif(type == 'PUT'):
        response = requests.put(url, data)


def GetLights():
    # Returns JSON of Philip's Hue Detected Lights
    return UserRequest('GET', 'lights')


def GetLightByNum(id):
    # Returns JSON of Philip's Hue Light By # ID:
    return UserRequest('GET', f'lights/{id}')


def ToggleLight(id):
    light = GetLightByNum(id)
    lightState = light['state']['on']
    print(lightState)
    if(str(lightState) == 'True'):
        UserRequest('PUT', f'lights/{id}/state', '{"on":false}')
    elif(str(lightState) == 'False'):
        UserRequest('PUT', f'lights/{id}/state', '{"on":true}')


def ChangeColor(id: int, color: str):
    if(color == 'green'):
        data = '{"on":true, "sat":254, "bri":254,"hue":20202}'
        print(data)
        UserRequest('PUT', f'lights/{id}/state', data)
    elif(color == 'red'):
        data = '{"on":true, "sat":254, "bri":254,"hue":65060}'
        print(data)
        UserRequest('PUT', f'lights/{id}/state', data)
    elif(color == 'yellow'):
        data = '{"on":true, "sat":254, "bri":254,"hue":10101}'
        print(data)
        UserRequest('PUT', f'lights/{id}/state', data)
    elif(color == 'blue'):
        data = '{"on":true, "sat":254, "bri":254,"hue":45454}'
        print(data)
        UserRequest('PUT', f'lights/{id}/state', data)
    elif(color == 'purple'):
        data = '{"on":true, "sat":254, "bri":254,"hue":50505}'
        print(data)
        UserRequest('PUT', f'lights/{id}/state', data)
    elif(color == 'white'):
        data = '{"on":true, "sat":150, "bri":254,"hue":10000}'
        print(data)
        UserRequest('PUT', f'lights/{id}/state', data)

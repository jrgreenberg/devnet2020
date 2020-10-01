
import requests
import json

def sendMessage(roomID):
    url = "https://webexapis.com/v1/messages"

    
    payload = "{\n    \"roomId\": \"" + roomID + "\" ,\n    \"text\": \"is there anybody out there? Just nod if you can hear me\"\n}"
    headers = {
    'Authorization': 'Bearer <redacted>',
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data = payload)

    if response.status_code == 200:
        print("Message created Successfully \n" + str(response.status_code))
    else:
        print('The Room did not create successfully! Go fix your code!!!')
        exit()


def main():
    url = "https://webexapis.com/v1/rooms"

    payload = "{\n    \"title\" : \"DevNet High 2020\"\n}"
    headers = {
    'Authorization': 'Bearer <redacted>',
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data = payload)
    output= json.loads(response.text.encode('utf8'))


    if response.status_code == 200:
        print("room created Successfully \n" + str(response.status_code))
        roomID = output['id']
        sendMessage(roomID)
    else:
        print('The Room did not create successfully! Go fix your code!!!')
        exit()




if __name__ == "__main__":
    main()

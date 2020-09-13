import requests
import json


def joke(category):
    if category is not "":
        url = f'https://api.chucknorris.io/jokes/random?category={category}'
    else:
        url = f'https://api.chucknorris.io/jokes/random'

    payload = {}
    headers = {
    }

    response = requests.request("GET", url, headers=headers, data = payload)
    jResponse = json.loads(response.text.encode('utf8'))
    return(jResponse['value'])


def get_categories():
    categories = []
    url = "https://api.chucknorris.io/jokes/categories"

    payload = {}
    headers = {
    }

    response = requests.request("GET", url, headers=headers, data = payload)
    jResponse = json.loads(response.text.encode('utf8'))
    
    for item in jResponse:
        item = str(item)
        categories.append(item)

    return(categories)


def getInput():
    userChoice = input("what categroy would you like to choose? Press 'enter' for a random category: ")
    return(userChoice)
def main():
    validCategory = False
    categories = get_categories() 
    while validCategory is False:
        print("available Categories\n")
        print(categories)
        userChoice = getInput()
        if userChoice in "":
            validCategory = True
        elif userChoice in categories:
            validCategory = True
        else:
            print('That is not a valid Category, try again')
    
    response = joke(userChoice)
    print(response)




if  __name__ == "__main__":
    main()
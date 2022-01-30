import requests
import json


def disaster_api_call (state):
    dec_endpoint = 'https://www.fema.gov/api/open/v1/FemaWebDisasterDeclarations'
    #dec_area_endpoint = 'https://www.fema.gov/api/open/v1/FemaWebDeclarationAreas'

    filter_state = '?$filter=stateName eq \'' + state + '\''

    response1 = requests.get(dec_endpoint + filter_state)
    data = response1.json()

    count = 0
    disaster_dict = dict()

    for i in data["FemaWebDisasterDeclarations"]:
        inc_type = data["FemaWebDisasterDeclarations"][count]["incidentType"]

        if inc_type in disaster_dict:
            num = disaster_dict.get(inc_type) + 1
            disaster_dict.update({inc_type : num})
        else:
            disaster_dict.update({inc_type : 1})

        count += 1

    for key, value in disaster_dict.items():
        print(key, ' : ', value)


def recommendation():



if __name__ == '__main__':
    disaster_api_call("Alaska")
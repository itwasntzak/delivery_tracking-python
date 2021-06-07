import json
import requests
from testing_tools import completed_shift


base_url = 'http://localhost:8000/api/'

def send_completed_shift(shift):
    send_url = f'{base_url}receive_completed_shift/'
    csrftoken = requests.get(send_url).cookies['csrftoken']
    headers = {'X-CSRFToken': csrftoken}
    cookies = {'csrftoken': csrftoken}

    send_shift = requests.post(
        send_url,
        data=json.dumps(shift.json_prep()),
        headers=headers,
        cookies=cookies,
        )

    # todo: change django to return a dictionary of primary keys
    #   correlating to shift.json_prep object
    # shift_pk = json.loads(send_shift.content)


def recieve_completed_shift(primary_key):
    recieve_url = f'{base_url}send_completed_shift/'
    request = requests.get(
        recieve_url,
        data=json.dumps( { 'pk': primary_key } )
        )
    print(request.text)

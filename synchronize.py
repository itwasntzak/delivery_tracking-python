import json
import requests
from testing_tools import completed_shift


main_url = 'http://localhost:8000/api/'

def send_completed_shift():
    csrftoken = requests.get(main_url).cookies['csrftoken']
    headers = {'X-CSRFToken': csrftoken}
    cookies = {'csrftoken': csrftoken}

    shift = completed_shift()

    send_shift = requests.post(
        f'{main_url}receive_completed_shift/',
        data=json.dumps(shift.json_prep()),
        headers=headers,
        cookies=cookies,
        )

    # todo: change django to return a dictionary of primary keys
    #   correlating to shift.json_prep object
    # shift_pk = json.loads(send_shift.content)


send_completed_shift()

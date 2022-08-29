import requests
from celery import shared_task


@shared_task
def get_active_calls():
    url = 'http://localhost/api/listcalls/'
    response = requests.get(url).json()
    print(response)
    return response
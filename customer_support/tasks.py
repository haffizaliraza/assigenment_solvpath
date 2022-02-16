from celery import shared_task
from .models import *
from django.contrib.sessions.models import Session
from customer_support.constants import MAX_CHASE_COUNT, SESSION_STATE, TIME_DELAY

@shared_task(max_retries=MAX_CHASE_COUNT)
def autoresponder(phone_number, session_id):
    print(session_id)
    try:
        session = Session.objects.get(pk=session_id)
    except:
        return False
    print(session.get_decoded()[str(phone_number)]['state'])
    if not session.get_decoded()[str(phone_number)]['state'] != SESSION_STATE[0][0]:
        send_message('sending message for join the session')
        autoresponder.retry(countdown=TIME_DELAY)
        
    return True

def send_message(mesage):
    print(mesage)




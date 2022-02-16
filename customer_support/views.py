from rest_framework import mixins, viewsets, status
from rest_framework.response import Response

import uuid
from datetime import datetime

from django.contrib.auth.hashers import make_password
from rest_framework.permissions import AllowAny, IsAuthenticated
from customer_support.models import Chaser
from customer_support.serializers import ChaserSerializer
from customer_support.constants import SESSION_STATE
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.sessions.models import Session
from customer_support.tasks import autoresponder, send_message



class SessionHandlingViewSet(mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):

    permission_classes = (AllowAny,)
    serializer_class = ChaserSerializer

    def create(self, request, *args, **kwargs):
        request_data = request.data.copy()

        s = SessionStore()
        s[request_data["phone_number"]] = {
            "state": SESSION_STATE[0][0],
            "time_stamp": str(datetime.now()),
            "chase_count": 0
        }
        s.create()
        send_message("sending message for joing the session")
        autoresponder.delay(request_data["phone_number"], str(s.session_key))
        return Response(
            {
                'success': True,
                'data': {
                    "id": s.session_key
                },
            },
            status=status.HTTP_201_CREATED
        )


    def get(self, request, *args, **kwargs):
        request.query_params.get('session_id')
        session = None
        try:
            session = Session.objects.get(pk=request.query_params.get('session_id'))
        except:
            return Response(
                {
                    'success': False,
                    'message': 'did not found any session agains your id',
                },
                status=status.HTTP_404_NOT_FOUND
            )
        session.get_decoded()['state'] = SESSION_STATE[1][0]
        

        return Response(
            {
                'success': False,
                'message': 'session has started.',
            },
            status=status.HTTP_201_CREATED
        )



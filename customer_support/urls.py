from django.urls import re_path
from customer_support.views import SessionHandlingViewSet

urlpatterns = [
    re_path(r'^receive_call/$', SessionHandlingViewSet.as_view({'post': 'create'})),
    re_path(r'^receive_call/(?P<session_id>\d+)/$', SessionHandlingViewSet.as_view({'get': 'get'})),

]
from rest_framework import serializers
from customer_support.models import Chaser

class ChaserSerializer(serializers.Serializer):

    class Meta:
        model = Chaser
        fields = ('id', 'message', )
        read_only_fields = ('created', 'modified')
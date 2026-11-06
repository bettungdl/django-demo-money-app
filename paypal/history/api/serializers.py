from rest_framework.serializers import ModelSerializer
from history.models import History
from user.api.serializer import UserPublicSerializer

class HistorySerializer(ModelSerializer):
    origin_user = UserPublicSerializer()
    target_user = UserPublicSerializer()

    class Meta:
        model = History
        fields = ['id', 'type', 'amount', 'origin_user', 'target_user', 'message', 'created_at']
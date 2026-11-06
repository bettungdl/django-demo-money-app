from rest_framework import serializers
from user.models import User
from wallet.api.serializers import WalletSerializer

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class UserSerializer(serializers.ModelSerializer):
    wallet = WalletSerializer()
    
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'first_name', 'last_name', 'date_joined', 'wallet']

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'password']

class UserPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'id']
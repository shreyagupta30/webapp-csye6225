from rest_framework import serializers
from user_auth.models import User

class CreateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ('id', 'username', 'firstname','lastname', 'password', 'account_created', 'account_updated')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
class UpdateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'password', 'firstname','lastname', 'account_created', 'account_updated')

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password is not None:
            instance.set_password(password)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

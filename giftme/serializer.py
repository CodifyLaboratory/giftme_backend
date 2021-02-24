from rest_framework import serializers

from giftme.models import GiftMeUser


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=65, min_length=8, write_only=True)
    email = serializers.EmailField(max_length=255, min_length=5)
    first_name = serializers.CharField(max_length=255, min_length=2)
    last_name = serializers.CharField(max_length=255, min_length=2)

    class Meta:
        model = GiftMeUser
        fields = ['email', 'first_name', 'last_name', 'password', 'username']

    def validate(self, attrs):
        email = attrs.get('email', '')
        if GiftMeUser.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email', ('Электронная почта уже зарегистрирована.')})
        return super().validate(attrs)

    def create(self, validated_data):
        return GiftMeUser.objects.create_user(**validated_data)
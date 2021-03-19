from rest_framework import serializers
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

from giftme.models import GiftMeUser, Holiday, Wish


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=65, min_length=8, write_only=True)
    email = serializers.EmailField(max_length=255, min_length=5)

    class Meta:
        model = GiftMeUser
        fields = ['email', 'password']

    def validate(self, attrs):
        email = attrs.get('email', '')
        if GiftMeUser.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email', ('Электронная почта уже зарегистрирована.')})
        return super().validate(attrs)

    def create(self, validated_data):
        return GiftMeUser.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=100, min_length=5)
    password = serializers.CharField(max_length=68, min_length=8, write_only=True)
    tokens = serializers.CharField(max_length=68, min_length=8, read_only=True)

    class Meta:
        model = GiftMeUser
        fields = ['email', 'password', 'tokens']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')

        user = auth.authenticate(email=email, password=password)

        if not user:
            raise AuthenticationFailed('Не верные логин/пароль, Повторите еще раз')

        return {
            'email': user.email,
            'password': user.password,
            'tokens': user.tokens
        }

        return super().validate(attrs)


class HolidaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Holiday
        exclude =[]


class WishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wish
        fields = ['name', 'status']


class WishDetailSerializer(serializers.ModelSerializer):
    pass


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_message = {
        'bad_token': ('Токен не верный или истек')
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad_token')
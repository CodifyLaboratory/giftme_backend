import json

from django.contrib.auth import logout
from django.http import JsonResponse
from django.views import View
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import generics, permissions
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

from .models import Holiday, Wish
from .serializer import UserSerializer, LoginSerializer, HolidaySerializer, LogoutSerializer, WishListSerializer, \
    WishDetailSerializer


class RegisterAPIView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutAPIView(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_204_NO_CONTENT)


class HolidayAPIView(View):
    def get(self, request, *args, **kwargs):
        holidays = Holiday.objects.all()
        serializer = HolidaySerializer(holidays, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        serializer = HolidaySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"status": "SUCCESS"}, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)


class WishAPIView(viewsets.ViewSet):
    def list(self, request):
        queryset = Wish.objects.all()
        serializer = WishListSerializer(queryset, many=True)
        return Response(serializer.data)

    def detail(self, request, pk=None):
        queryset = Wish.objects.all()
        wish = get_object_or_404(queryset, pk=pk)
        serialize = WishDetailSerializer(wish)
        return Response(serialize.data)
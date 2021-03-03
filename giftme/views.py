import json

from django.http import JsonResponse
from django.views import View
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from .models import Holiday
from .serializer import UserSerializer, LoginSerializer, HolidaySerializer


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

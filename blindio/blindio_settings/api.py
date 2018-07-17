from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Setting
from .serializers import SettingSerializer


class SettingApi(APIView):
    def get_object(self, name):
        try:
            return Setting.objects.get(name=name)
        except Setting.DoesNotExist:
            return None

    def get(self, request, name):
        setting = self.get_object(name)

        serializer = SettingSerializer(setting)
        return Response(serializer.data)

    def post(self, request, name):
        setting = self.get_object(name)
        serializer = SettingSerializer(setting, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
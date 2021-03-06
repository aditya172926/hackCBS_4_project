from django.contrib.auth.models import User
from django.core import serializers as core_serializers
from django.http.response import JsonResponse
from rest_framework import viewsets, generics
from rest_framework import serializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from api.serializers import UserSerializer, RegisterSerializer, UserDataSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import UserData

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.save()
        return Response({
            "status": "Done",
            "data": request.data
        })

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

@csrf_exempt
def userLogout(request):
    dictionary = json.loads(request.body)
    token_user_name = dictionary['key']
    Token.objects.get(user = token_user_name).delete()
    return HttpResponse('Done')

class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        rresponse = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key = rresponse.data['token'])
        return Response({'token': token.key, 'user_id': token.user_id})

class UserDataView(viewsets.ModelViewSet):
    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        print(self.request.user.id)
        data = UserData.objects.filter(author_id=self.request.user.id).values()
        return data

    def update(self, request, *args, **kwargs):
        print('called')
        print(request.data.get("origin"))
        instance = UserData.objects.filter(author_id = request.data.get("author"))
        instance.update(origin = request.data.get("origin"))
        instance.update(continent = request.data.get("continent"))
        instance.update(country = request.data.get("country"))
        return Response({'sone': 'some'})
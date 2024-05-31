from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from.serializer import UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

@api_view(['POST'])
def view_register(request):
    data={}
    if request.method=='POST':
        u_serialize=UserSerializer(data=request.data)
        if u_serialize.is_valid():
            u=u_serialize.save()
            data['msg']="User Register SuccessFully!"

            data['user']=u.username
            t=Token.objects.get(user=u)
            data['token']=t.key
        else:
            data=u_serialize.errors
            return

        Response(data=data)

        @api_view(['GET'])
        @permission_classes([IsAuthenticated])
        def view_secure(request):
            return
        Response(data="This is my Secure Page only access When Token is available")
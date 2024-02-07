from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CreateUserSerializer, UpdateUserSerializer
from rest_framework.permissions import IsAuthenticated

class UserAuthViewSet(GenericAPIView):

    def post(self, request):
        serializer = CreateUserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class GetUserAuthViewSet(GenericAPIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        serializer = CreateUserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        if not set(request.data.keys()).issubset(set(UpdateUserSerializer.Meta.fields)):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = UpdateUserSerializer(request.user, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

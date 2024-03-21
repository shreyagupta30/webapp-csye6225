from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CreateUserSerializer, UpdateUserSerializer
from rest_framework.permissions import IsAuthenticated
import logging


logger = logging.getLogger(__name__)

class UserAuthViewSet(GenericAPIView):

    def post(self, request):
        serializer = CreateUserSerializer(data=request.data)
        if not set(request.data.keys()).issubset(set(['firstname', 'lastname', 'password', 'username'])):
            logger.error("UserAuthViewSet: Certain fields are missing in the request body")
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if not serializer.is_valid():
            logger.error("UserAuthViewSet: Invalid request body is provided")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        logger.debug("GetUserAuthViewSet: The user information is saved")
        serializer.save()
        logger.info("UserAuthViewSet: POST method is successful")
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class GetUserAuthViewSet(GenericAPIView):
    permission_classes = [IsAuthenticated]
    logger.warning("GetUserAuthViewSet: User is not authenticated")
    
    def get(self, request):
        serializer = CreateUserSerializer(request.user)
        logger.info("GetUserAuthViewSet: GET method is successful")
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        if not set(request.data.keys()).issubset(set(['firstname', 'lastname', 'password'])):
            logger.error("GetUserAuthViewSet: Certain fields are missing in the request body")
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = UpdateUserSerializer(request.user, data=request.data, partial=True)
        if not serializer.is_valid():
            logger.error("GetUserAuthViewSet: Invalid request body is provided")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        logger.debug("GetUserAuthViewSet: The user information is updated")
        logger.info("GetUserAuthViewSet: PUT method is successful")
        return Response(status=status.HTTP_204_NO_CONTENT)

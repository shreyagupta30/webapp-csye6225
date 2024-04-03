from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CreateUserSerializer, UpdateUserSerializer
from rest_framework.permissions import IsAuthenticated
import logging
from google.cloud import pubsub_v1
import json
from django.core import signing
from django.conf import settings
from user_auth.models import User
from django.utils import timezone
from django.conf import settings
import base64


logger = logging.getLogger(__name__)


def send_to_pub_sub(data):
    publish = pubsub_v1.PublisherClient()
    topic_path = f"projects/{settings.GOOGLE_CLOUD_PROJECT_ID}/topics/{settings.GOOGLE_CLOUD_PUBSUB_TOPIC_NAME}"
    data["id"] = str(data["id"])
    data = json.dumps(data).encode("utf-8")
    publish.publish(topic_path, data)

class UserAuthViewSet(GenericAPIView):

    def post(self, request):
        serializer = CreateUserSerializer(data=request.data)
        print(serializer.data)
        if not set(request.data.keys()).issubset(set(['firstname', 'lastname', 'password', 'username'])):
            logger.error("UserAuthViewSet: Certain fields are missing in the request body")
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if not serializer.is_valid():
            logger.error("UserAuthViewSet: Invalid request body is provided")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        logger.debug("GetUserAuthViewSet: The user information is saved")
        serializer.save()
        logger.info("UserAuthViewSet: POST method is successful")
        if not settings.TESTING:
            try:
                send_to_pub_sub(
                    {
                        "id": serializer.data["id"],
                        "firstname": serializer.data["firstname"],
                        "lastname": serializer.data["lastname"],
                        "email": serializer.data["username"],
                        "token": base64.b64encode(str(serializer.data["id"]).encode()).decode()
                    }
                )
            except Exception as e:
                logger.error(f"UserAuthViewSet: Error in sending data to pubsub: {e}")
                return Response(status=status.HTTP_403_FORBIDDEN)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class GetUserAuthViewSet(GenericAPIView):
    permission_classes = [IsAuthenticated]
    logger.warning("GetUserAuthViewSet: User is not authenticated")
    
    def get(self, request):
        serializer = CreateUserSerializer(request.user)
        if not settings.TESTING:
            if not serializer.data['is_verified']:
                print("I am here!")
                logger.error("GetUserAuthViewSet: User is not verified")
                return Response("User is not verified!", status=status.HTTP_403_FORBIDDEN)
        logger.info("GetUserAuthViewSet: GET method is successful")
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        if not settings.TESTING:
            if not serializer.data['is_verified']:
                logger.error("UserPut: User is not verified")
                return Response(status=status.HTTP_403_FORBIDDEN)
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
    
class UserAuthVerificationViewSet(GenericAPIView):
    def get(self, request, *args, **kwargs):
        token = request.query_params.get('token')
        if not token:
            logger.error("UserAuthVerificationViewSet: Token is missing in the request")
            return Response(status=status.HTTP_403_FORBIDDEN)
        try:
            user = User.objects.get(email_token_generated=token)
        except Exception:
            logger.error("UserAuthVerificationViewSet: Token is invalid")
            return Response("Token is invalid!", status=status.HTTP_403_FORBIDDEN)
        
        time_of_email = User.objects.get(email_token_generated=token).email_token_generated_at
        if timezone.now().timestamp() - time_of_email.timestamp() > 60 * 2:
            logger.error("UserAuthVerificationViewSet: Token is expired")
            return Response("Token is expired", status=status.HTTP_403_FORBIDDEN)

        user.is_verified = True
        user.save()
        logger.info("UserAuthVerificationViewSet: User is verified")
        return Response(status=status.HTTP_200_OK)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import connection
import logging

logger = logging.getLogger(__name__)
class DBHealthCheck(APIView):
    def get(self, request):
        if request.body or request.query_params:
            logger.warning("DBHealthCheck: GET method does not accept any parameters")
            logger.error("DBHealthCheck: GET method does not accept any parameters")
            return Response(status=status.HTTP_400_BAD_REQUEST)
        try:
            connection.ensure_connection()
            logger.info("DBHealthCheck: Connection to the database is successful")
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            logger.error("DBHealthCheck: Connection to the database is not successful")
            return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)
        
    def post(self, request):
        logger.error("DBHealthCheck: POST method is not allowed")
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def put(self, request):
        logger.error("DBHealthCheck: PUT method is not allowed")
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def delete(self, request):
        logger.error("DBHealthCheck: DELETE method is not allowed")
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def head(self, request):
        logger.error("DBHealthCheck: HEAD method is not allowed")
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def options(self, request):
        logger.error("DBHealthCheck: OPTIONS method is not allowed")
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

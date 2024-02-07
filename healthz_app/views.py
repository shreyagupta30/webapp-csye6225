from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import connection

class DBHealthCheck(APIView):
    def get(self, request):
        if request.body or request.query_params:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        try:
            connection.ensure_connection()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)
        
    def post(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def put(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def delete(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def head(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def options(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

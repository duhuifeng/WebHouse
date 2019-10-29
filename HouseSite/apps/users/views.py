from .serializers import DeviceReportSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class DeviceReport(APIView):
    """
    上报设备信息, 无需鉴权
    """
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        serializer = DeviceReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

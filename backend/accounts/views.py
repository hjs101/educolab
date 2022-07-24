from rest_framework.decorators import APIView
""" from .serializers import SignupSerializer """
from rest_framework.response import Response

""" class SignupView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201) """
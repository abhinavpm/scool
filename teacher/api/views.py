from rest_framework.views import APIView
from teacher.models import Student, Teacher
from teacher.api.serializers import StudentRegisterSerializer
from rest_framework.response import Response

class StudentRegisterview(APIView):
    def post(self, request,*args,**kwargs):
        #         serializer = UserSerializer()
        serializers=StudentRegisterSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors)
        
    def get(self, request,*args,**kwargs):
        instance=Student.objects.all()
        serializers=StudentRegisterSerializer(instance, many=True)
        return Response(serializers.data) 
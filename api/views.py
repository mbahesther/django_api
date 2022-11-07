from .models import employee
from .serializers import employeeSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def employee_list(request):
    employees = employee.objects.all()
    serializer = employeeSerializer(employees, many=True)
    return Response({'employees list':serializer.data})


@api_view(['POST'])
def add_employee(request):
    serializer = employeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)  


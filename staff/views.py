from django.shortcuts import render
from django.http import Http404
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response

from staff.models import Staff
from staff.serializers import StaffSerializer


class ViewStaff(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer


class StaffList(APIView):
    """
    列出所有干员或者创建一个干员
    """

    def get(self, request, format=None):
        staffs = Staff.objects.all()
        serializer = StaffSerializer(staffs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        staff_data = request.data
        staff_data['tag'] = str(staff_data['tag'])
        staff_data['race'] = str(staff_data['race'])
        staff_data['approach'] = str(staff_data['approach'])

        serializer = StaffSerializer(data=staff_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

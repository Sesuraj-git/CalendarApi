import datetime

import django
from django.db import IntegrityError
from django.utils.datastructures import MultiValueDictKeyError
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import User, Student, Teacher, DepartmentEvent, Department, CollegeEvent
from .serializers import UserSerializer, StudentSerializer, TeacherSerializer, DepartmentEventSerializer, \
    CollegeEventSerializer
from django.utils.dateparse import parse_date


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        user = request.user
        user = User.objects.get(username=user)

        try:
            student = Student.objects.get(user=user.id)
            serializer = StudentSerializer(student)
            print('View')
            response = {'result': serializer.data}

        except:
            response = {'failed': "User is Not a Registered Student"}
            return Response(response, status=status.HTTP_403_FORBIDDEN)

        return Response(response, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        """user = request.user
        user = User.objects.get(username=user)

        try:
            student = Student.objects.create(user=user, **kwargs)
            serializer = StudentSerializer(student)
            print('View')
            response = {'result': serializer.data}
            return Response(response, status=status.HTTP_200_OK)

        except IntegrityError:"""
        response = {'failed': "Not Allowed "}
        return Response(response, status=status.HTTP_403_FORBIDDEN)


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        user = request.user
        user = User.objects.get(username=user)

        response = {'failed': "Not Allowed"}
        return Response(response, status=status.HTTP_403_FORBIDDEN)


class DepartmentEventViewSet(viewsets.ModelViewSet):
    queryset = DepartmentEvent.objects.all()
    serializer_class = DepartmentEventSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        user = request.user
        user = User.objects.get(username=user)

        event = DepartmentEvent.objects.filter(created_by=user.id)
        serializer = DepartmentEventSerializer(event, many=True)
        print('View')
        response = {'result': serializer.data}
        return Response(response, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        user = request.user
        print(request.data)
        response = {}
        try:
            department = int(request.data["department"])
        except KeyError:
            response["department"] = "This field is required"
        except ValueError:
            response["department"] = "Invalid Format"
        try:
            date = request.data["due_date"]
            date = parse_date(date)
            if date is None:
                response['due_date'] = "Invalid Format"
            print(date)
        except KeyError:
            response['due_date'] = "This field is required"
        print(response)
        if response.__len__() >= 1:
            response = {'result': response}
            return Response(response, status=status.HTTP_404_NOT_FOUND)

        department = Department.objects.get(id=department)
        user = User.objects.get(username=user)
        event = DepartmentEvent.objects.create(created_by=user, due_date=date, department=department, **kwargs)
        serializer = DepartmentEventSerializer(event)
        print('View')
        response = {'result': serializer.data}
        return Response(response, status=status.HTTP_200_OK)


class CollegeEventViewSet(viewsets.ModelViewSet):
    queryset = CollegeEvent.objects.all()
    serializer_class = CollegeEventSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        user = request.user
        user = User.objects.get(username=user)

        event = CollegeEvent.objects.filter(created_by=user.id)
        print(event)
        serializer = CollegeEventSerializer(event, many=True)
        print('View', user.id)
        response = {'result': serializer.data}
        return Response(response, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        user = request.user
        print(request.data)
        response = {}
        try:
            date = request.data["due_date"]
            date = parse_date(date)
            if date is None:
                response['due_date'] = "Invalid Format"
            print(date)
        except KeyError:
            response['due_date'] = "This field is required"
        print(response)
        if response.__len__() >= 1:
            response = {'result': response}
            return Response(response, status=status.HTTP_404_NOT_FOUND)

        user = User.objects.get(username=user)
        event = CollegeEvent.objects.create(created_by=user, due_date=date, **kwargs)
        serializer = CollegeEventSerializer(event)
        print('View')
        response = {'result': serializer.data}
        return Response(response, status=status.HTTP_200_OK)

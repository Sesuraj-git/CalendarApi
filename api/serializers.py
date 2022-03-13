from rest_framework import serializers
from rest_framework.authtoken.models import Token

from api.models import User, Student, Teacher, DepartmentEvent, CollegeEvent


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ("user", "student_id", "name", "email", "class_id", "id")


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ("staff_id", "name", "department", "id")


class DepartmentEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentEvent
        fields = ("department", "created_by", "type", "name", "description", "added_on", "due_date", "id")


class CollegeEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollegeEvent
        fields = ("created_by", "type", "name", "description", "added_on", "due_date", "id")

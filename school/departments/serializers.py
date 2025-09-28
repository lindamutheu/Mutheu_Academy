from rest_framework import serializers
from .models import Students

class StudentsSerializer(serializers.ModelSerializer):  # ✅ Uppercase S

    class Meta:
        model = Students
        fields = ["first_name", "last_name", "registration", "published_date"]  # ✅ fields not field

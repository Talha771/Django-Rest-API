from rest_framework import serializers
from base.models import User,ToDoList

class userserializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields =  '__all__'

class ToDoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = '__all__'
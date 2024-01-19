from rest_framework import serializers

class customersignupserializer(serializers.Serializer):
    username = serializers.CharField(max_length=10)
    mobile = serializers.IntegerField()
    email = serializers.EmailField()
    password = serializers.CharField(max_length=100)


class customerloginserializer(serializers.Serializer):
    username = serializers.CharField(max_length=10)
    password = serializers.CharField(max_length=100)

class updateProfileSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=10)
    first_name = serializers.CharField(max_length=10,required=False)
    last_name = serializers.CharField(max_length=10,required=False)
    gender = serializers.CharField(max_length=10,required=False)
    age = serializers.IntegerField(required=False)
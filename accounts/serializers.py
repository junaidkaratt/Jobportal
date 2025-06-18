from rest_framework import serializers
from .models import User, UserRole



class userregister(serializers.ModelSerializer):

    password= serializers.CharField(write_only=True)

    class Meta:
        model= User
        fields= ('email','password','roles')

    def validate_roles(self, value):
        role_values=[role.value for role in UserRole]
        if value not in role_values:
            raise serializers.ValidationError("Invalid role")
        return value
    
    def create(self, validated_data):
        password= validated_data.pop('password')
        user=User(**validated_data)
        user.set_password(password)
        user.save()
        return user

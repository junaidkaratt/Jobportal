from rest_framework import serializers
from .models import User, UserRole, jobSeekerProfileModel, employerProfileModel
from django.contrib.auth import authenticate


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
    


class LoginSerializer(serializers.Serializer):
    email= serializers.EmailField()
    password= serializers.CharField()
    def validate(self, data):
        user = authenticate(email=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError("invalid email or password")
        data['user']=user
        return data



class jobSeekerprofileSerializer(serializers.ModelSerializer):
    email= serializers.EmailField(source= 'user.email', read_only=True)
    full_name= serializers.CharField(source= 'user.full_name')
    phone_number = serializers.CharField(source= 'user.phone_number', allow_blank= True)

    class Meta:
        model= jobSeekerProfileModel
        fields= ['email', 'full_name', 'phone_number', 'resume', 'skills', 'experience', 'education']

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', {})
        instance.user.full_name = user_data.get('full_name', instance.user.full_name)
        instance.user.phone_number = user_data.get('phone_number', instance.user.phone_number)
        instance.user.save()

        instance.resume = validated_data.get('resume', instance.resume)
        instance.skills = validated_data.get('skills', instance.skills)
        instance.experience = validated_data.get('experience', instance.experience)
        instance.education = validated_data.get('education', instance.education)
        instance.save()
        return instance
    


class employerprofileSerializer(serializers.ModelSerializer):
    email= serializers.EmailField(source= 'user.email', read_only=True)
    full_name= serializers.CharField(source= 'user.full_name')
    phone_number = serializers.CharField(source= 'user.phone_number', allow_blank= True)

    class Meta:
        model= employerProfileModel
        fields= ['email', 'full_name', 'phone_number', 'company_name', 'company_website', 'logo', 'description']

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user',{})
        instance.user.full_name = user_data.get('full_name', instance.user.full_name)
        instance.user.phone_number = user_data.get('phone_number', instance.user.phone_number)
        instance.user.save()

        instance.company_name = validated_data.get('company_name', instance.company_name)
        instance.company_website = validated_data.get('company_website', instance.company_website)
        instance.logo = validated_data.get('logo', instance.logo)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


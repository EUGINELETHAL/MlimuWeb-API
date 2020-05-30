from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=255, read_only=True)
    
    class Meta:
        model = User
        fields = ( 'username','email', 'password', 'password2', 'is_student','is_active','is_teacher','token')
    
    extra_kwargs = {'password': {'write_only': True}}, {'password2': {'write_only': True}}

    def create(self, validated_data):
        email = validated_data['email'],
        password = validated_data['password']
        password2 = validated_data['password2']

        if password != password2:
                raise serializers.ValidationError("Your Passwords do not match")        
            # role = validated_data['role'],
            #active = validated_data['active'],
            # verified = validated_data['verified'],
        user = User(**validated_data)
            
            
                           # role=role, active=active, verified=verified)
    
        user.set_password(password)
        user.is_student = True
        
        user.save()           

class StudentSerializer(serializers.ModelSerializer):
    

    def create(self, validated_data):
        email = validated_data['email'],
        password = validated_data['password']
        password2 = validated_data['password2']

        if password != password2:
                raise serializers.ValidationError("Your Passwords do not match")        
            # role = validated_data['role'],
            #active = validated_data['active'],
            # verified = validated_data['verified'],
        user = User(**validated_data)
            
            
                           # role=role, active=active, verified=verified)
    
        user.set_password(password)
        user.is_student = True
        
        user.save()           

        return user        return user

    



class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        # The `validate` method is where we make sure that the current
        # instance of `LoginSerializer` has "valid". In the case of logging a
        # user in, this means validating that they've provided an email
        # and password and that this combination matches one of the users in
        # our database.
        email = data.get('email', None)
        password = data.get('password', None)

        # Raise an exception if an
        # email is not provided.
        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in.'
            )

        # Raise an exception if a
        # password is not provided.
        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

        # The `authenticate` method is provided by Django and handles checking
        # for a user that matches this email/password combination. Notice how
        # we pass `email` as the `username` value since in our User
        # model we set `USERNAME_FIELD` as `email`.
        user = authenticate(username=email, password=password)

        # If no user was found matching this email/password combination then
        # `authenticate` will return `None`. Raise an exception in this case.
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found.'
            )

        # Django provides a flag on our `User` model called `is_active`. The
        # purpose of this flag is to tell us whether the user has been banned
        # or deactivated. This will almost never be the case, but
        # it is worth checking. Raise an exception in this case.
        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )

        # The `validate` method should return a dictionary of validated data.
        # This is the data that is passed to the `create` and `update` methods
        # that we will see later on.
        return {
            'email': user.email,
            'username': user.username,
            # 'token': user.token
        }       
           




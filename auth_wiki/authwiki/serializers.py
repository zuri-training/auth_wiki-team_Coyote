from rest_framework import serializers
from .models import Users
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class RegisterSerializer(serializers.ModelSerializer):
    refresh = serializers.SerializerMethodField()
    access = serializers.SerializerMethodField()


    class Meta:

        model = Users
        fields = ['first_name', 'email', 'last_name', 'username',
                  'password', 'password2', 'refresh', 'access']
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'email': {'required': True},
            'password': {'write_only': True, 'required': True},
            'password2': {'write_only': True, 'required': True}
        }

    def validate(self, attrs):
        email = attrs.get('email')
        if Users.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {"email": "email already exist"})

        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = Users.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        # saves the following validated data to database
        user.set_password(validated_data['password'])
        user.save()

        refresh = TokenObtainPairSerializer.get_token(user)

        self._refresh = str(refresh)
        self._access = str(refresh.access_token)

        return user

    def get_refresh(self, obj):
        return self._refresh

    def get_access(self,obj):
        return self._access


     
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _
from rest_framework.validators import UniqueValidator

from authentication.models import CustomUser


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # orders = serializers.HyperlinkedModelSerializer(many=True, read_only=True)
    orders = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ('id', 'orders', 'url', 'first_name', 'middle_name', 'last_name',
                  'email', 'password', 'updated_at', 'created_at', 'role', 'is_active')

        extra_kwargs = {
            'password': {'write_only': True},
            'url': {'view_name': 'users:user_profile', 'lookup_url_kwarg': 'user_id'},
        }

    def get_created_at(self, obj):
        return int(obj.created_at.timestamp())

    def get_updated_at(self, obj):
        return int(obj.updated_at.timestamp())

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super(UserSerializer, self).update(instance, validated_data)


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True,
                                   validators=[UniqueValidator(queryset=CustomUser.objects.all(),
                                                               message=_('An account with this email already exists'))
                                               ]
                                   )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True,
                                      required=True,
                                      help_text=_('Must match the password')
                                      )

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'middle_name', 'last_name', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': _('Password didn\'t match!.')})

        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

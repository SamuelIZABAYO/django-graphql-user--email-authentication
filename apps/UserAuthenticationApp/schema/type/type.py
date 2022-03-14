from dataclasses import fields
from graphene_django import DjangoObjectType

from apps.UserAuthenticationApp.models import User


class UserType(DjangoObjectType):
    
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email')

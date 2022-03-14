import graphene
from django.contrib.auth import get_user_model
from apps.UserAuthenticationApp.models import User

from apps.UserAuthenticationApp.schema.type.type import UserType


class CreateUser(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        first_name = graphene.String()
        last_name = graphene.String()
        password=graphene.String(required=True)

    user = graphene.Field(UserType)

    @classmethod
    def mutate(self, root, *args, **kwargs):
        user=get_user_model().objects.create_user(email=kwargs.get("email"),password=kwargs.get("password"),first_name=kwargs.get("first_name"),last_name=kwargs.get("last_name"))

        return CreateUser(user=user)

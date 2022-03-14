import graphene
from apps.UserAuthenticationApp.models import User

from apps.UserAuthenticationApp.schema.type.type import UserType


class Query(graphene.AbstractType):
    users = graphene.List(UserType)

    def resolve_users(self, info):
        return User.objects.all()

import graphene

from apps.UserAuthenticationApp.schema.mutation.user_mutation import CreateUser


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()

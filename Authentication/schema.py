import graphene
from apps.UserAuthenticationApp.schema.query.query import Query as UserQueries
from apps.UserAuthenticationApp.schema.mutation.mutation import Mutation as UserMutation


class Query(graphene.ObjectType,UserQueries):
    pass


class Mutation(UserMutation):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)

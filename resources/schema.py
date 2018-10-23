import graphene
import apps.core.schema


class Query(apps.core.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
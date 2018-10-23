import graphene
import apps.aranceles.schema


class Query(apps.core.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
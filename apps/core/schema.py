from apps.core import models
import graphene

from graphene_django.types import DjangoObjectType


class CompanyType(DjangoObjectType):
    class Meta:
        model = models.Company


class ProfileType(DjangoObjectType):
    class Meta:
        model = models.Profile


class Query(object):
    all_companies = graphene.List(CompanyType)
    all_profiles = graphene.List(ProfileType)

    def resolve_all_companies(self, info, **kwargs):
        return models.Company.objects.all()

    def resolve_all_profiles(self, info, **kwargs):
        return models.Profile.objects.all()



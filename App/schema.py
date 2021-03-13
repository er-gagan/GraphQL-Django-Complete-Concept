import graphene
from graphene_django import DjangoObjectType
from .models import Singer,Song
from graphene_django.filter import DjangoFilterConnectionField
from graphene import relay

class SingerType(DjangoObjectType):
    class Meta:
        model = Singer
        filter_fields = {
            'id' : ['exact','iexact'],
            'Name' : ['exact','iexact'],
            'Phone' : ['exact'],
            'Email' : ['exact','iexact'],
        }
        interfaces = (relay.Node, )

class SongType(DjangoObjectType):
    class Meta:
        model = Song
        filter_fields = {
            'id' : ['exact','iexact'],
            'Name' : ['exact','iexact'],
            'Duration' : ['gte','lte'],
        }
        interfaces = (relay.Node, )

class Query(graphene.ObjectType):
    singer = relay.Node.Field(SingerType)
    singers = DjangoFilterConnectionField(SingerType, Address=graphene.String())

    song = relay.Node.Field(SongType)
    songs = DjangoFilterConnectionField(SongType)

class create_Singer_Mutation(graphene.Mutation):
    class Arguments:
        Name = graphene.String(required=True)
        Phone = graphene.String(required=True)
        Email = graphene.String(required=True)
    singer = graphene.Field(SingerType)

    @classmethod
    def mutate(cls, root, info, Name, Phone, Email):
        singer = Singer(Name=Name, Phone=Phone, Email=Email)
        singer.save()
        return create_Singer_Mutation(singer=singer)

class update_Singer_Mutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        Name = graphene.String(required=True)
        Phone = graphene.String(required=True)
        Email = graphene.String(required=True)
    singer = graphene.Field(SingerType)

    @classmethod
    def mutate(cls, root, info, id, Name, Phone, Email):
        singer = Singer.objects.get(id=id)
        singer.Name=Name
        singer.Phone=Phone
        singer.Email=Email
        singer.save()
        return update_Singer_Mutation(singer=singer)

class delete_Singer_Mutation(graphene.Mutation):    
    class Arguments:
        id = graphene.ID()
    singer = graphene.Field(SingerType)
    
    @classmethod
    def mutate(cls, root, info, id):
        singer = Singer.objects.get(id=id)
        singer.delete()
        return

class Mutation(graphene.ObjectType):
    create_Singer = create_Singer_Mutation.Field()
    update_Singer = update_Singer_Mutation.Field()
    delete_Singer = delete_Singer_Mutation.Field()

    # create_Song = create_Song_Mutation.Field()
    # update_Song = update_Song_Mutation.Field()
    # delete_Song = delete_Song_Mutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)


# superuser
# user and password: admin

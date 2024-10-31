from graphene import ObjectType

from app.gql.mutations.missions_mutation import AddMission


class Mutation(ObjectType):
    add_mission = AddMission.Field()
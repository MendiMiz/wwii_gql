from graphene import ObjectType

from app.gql.mutations.missions_mutation import AddMission, UpdateMission
from app.gql.mutations.targets_mutation import AddTarget


class Mutation(ObjectType):
    add_mission = AddMission.Field()
    add_target = AddTarget.Field()
    update_mission = UpdateMission.Field()
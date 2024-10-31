from graphene import ObjectType

from app.gql.mutations.missions_mutation import AddMission, UpdateMission, DeleteMission
from app.gql.mutations.targets_mutation import AddTarget
from app.repository.missions_repository import delete_mission


class Mutation(ObjectType):
    add_mission = AddMission.Field()
    add_target = AddTarget.Field()
    update_mission = UpdateMission.Field()
    delete_mission = DeleteMission.Field()
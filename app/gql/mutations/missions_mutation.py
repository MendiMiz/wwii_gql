from graphene import InputObjectType, Mutation, Field, Date, Float, Int, Boolean
from sqlalchemy import func

from app.db.database import session_maker
from app.db.models import Missions
from app.gql.types.missions_type import MissionsType
from app.repository.missions_repository import delete_mission, update_mission, create_mission


class MissionMutationInput(InputObjectType):
    mission_date = Date()
    airborne_aircraft = Float()
    attacking_aircraft = Float()
    bombing_aircraft = Float()
    aircraft_returned = Float()
    aircraft_failed = Float()
    aircraft_damaged = Float()
    aircraft_lost = Float()




class AddMission(Mutation):
    class Arguments:
        mission_input = MissionMutationInput(required=True)

    mission = Field(MissionsType)

    @staticmethod
    def mutate(root, info, mission_input=None):
        return AddMission(mission=create_mission(mission_input))



class UpdateMission(Mutation):
    class Arguments:
        mission_id = Int(required=True)
        mission_input = MissionMutationInput(required=True)

    mission = Field(MissionsType)

    @staticmethod
    def mutate(root, info, mission_id, mission_input=None):
        return UpdateMission(mission=update_mission(mission_id, mission_input))



class DeleteMission(Mutation):
    class Arguments:
        mission_id = Int(required=True)

    result = Field(Boolean)

    @staticmethod
    def mutate(root, info, mission_id):
        return DeleteMission(result= delete_mission(mission_id))






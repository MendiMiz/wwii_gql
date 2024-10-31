from graphene import ObjectType, Field, Int, Date, List

from app.gql.types.missions_type import MissionsType
from app.repository.missions_repository import mission_by_id


class Query(ObjectType):
    get_mission_by_id = Field(MissionsType, mission_id=Int(required=True))
    mission_by_dates_range = List(MissionsType, start_date=Date(required=True), end_date=Date(required=True))

    @staticmethod
    def resolve_get_mission_by_id(root, info, mission_id):
        return mission_by_id(mission_id).value_or(None)
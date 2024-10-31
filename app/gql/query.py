from graphene import ObjectType, Field, Int, Date, List, String

from app.gql.types.missions_type import MissionsType
from app.repository.missions_repository import mission_by_id, missions_by_dates_range, missions_by_country, \
    missions_by_target_industry, missions_by_target_type


class Query(ObjectType):
    get_mission_by_id = Field(MissionsType, mission_id=Int(required=True))
    get_missions_by_dates_range = List(MissionsType, start_date=Date(required=True), end_date=Date(required=True))
    get_missions_by_country = List(MissionsType, country_name=String(required=True))
    get_missions_by_target_industry = List(MissionsType, target_industry=String(required=True))
    get_missions_by_target_type = List(MissionsType, target_type=String(required=True))

    @staticmethod
    def resolve_get_mission_by_id(root, info, mission_id):
        return mission_by_id(mission_id).value_or(None)

    @staticmethod
    def resolve_get_missions_by_dates_range(root, info, start_date, end_date):
        return missions_by_dates_range(start_date, end_date).value_or(None)

    @staticmethod
    def resolve_get_missions_by_country(root, info, country_name):
        return missions_by_country(country_name).value_or(None)

    @staticmethod
    def resolve_get_missions_by_target_industry(root, info, target_industry):
        return missions_by_target_industry(target_industry).value_or(None)

    @staticmethod
    def resolve_get_missions_by_target_type(root, info, target_type):
        return missions_by_target_type(target_type).value_or(None)




from graphene import ObjectType, Int, String, List, Field



class TargetsType(ObjectType):
    target_id = Int()
    mission_id = Int()
    target_industry = String()
    city_id = Int()
    target_type_id = Int()
    target_priority = Int()

    mission = Field('app.gql.types.missions_type.MissionsType')
    city = Field('app.gql.types.cities_type.CitiesType')
    target_type = Field('app.gql.types.target_types_type.TargetTypesType')
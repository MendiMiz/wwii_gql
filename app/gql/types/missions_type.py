from graphene import ObjectType, Int, String, Field, Date, Float



class MissionsType(ObjectType):
    mission_id = Int()
    mission_date = Date()
    airborne_aircraft = Float()
    attacking_aircraft = Float()
    bombing_aircraft = Float()
    aircraft_returned = Float()
    aircraft_failed = Float()
    aircraft_damaged = Float()
    aircraft_lost = Float()

    target = Field('app.gql.types.targets_type.TargetsType')
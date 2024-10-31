from graphene import ObjectType, Int, String, Field, Float, List


class CitiesType(ObjectType):
    city_id = Int()
    city_name = String()
    country_id = Int()
    latitude = Float()
    longitude = Float()

    country = Field('app.gql.types.countries_type.CountriesType')
    targets = List('app.gql.types.targets_type.TargetsType')
from graphene import ObjectType, Int, String, Field, List

import app.gql.types.cities_type


class CountriesType(ObjectType):
    country_id = Int()
    country_name = String

    cities = List('app.gql.types.cities_type.CitiesType')

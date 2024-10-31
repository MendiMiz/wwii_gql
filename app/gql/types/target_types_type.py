from graphene import ObjectType, Int, String, List


class TargetTypesType(ObjectType):
    target_type_id = Int()
    target_type_name = String

    targets = List('app.gql.types.targets_type.TargetsType')
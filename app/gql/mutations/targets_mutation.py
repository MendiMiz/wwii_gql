from graphene import InputObjectType, Mutation, Field, Int, String
from sqlalchemy import func

from app.db.database import session_maker
from app.db.models import Targets
from app.gql.types.targets_type import TargetsType
from app.repository.targets_repository import create_target


class TargetMutationInput(InputObjectType):
    mission_id = Int()
    target_industry = String()
    city_id = Int()
    target_type_id = Int()
    target_priority = Int()

class AddTarget(Mutation):
    class Arguments:
        target_input = TargetMutationInput(required=True)

    target = Field(TargetsType)

    @staticmethod
    def mutate(root, info, target_input=None):
        return AddTarget(target=create_target(target_input))


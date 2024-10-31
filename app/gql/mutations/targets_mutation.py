from graphene import InputObjectType, Mutation, Field, Int, String
from sqlalchemy import func

from app.db.database import session_maker
from app.db.models import Targets
from app.gql.types.targets_type import TargetsType


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
        with session_maker() as session:
            new_target_id = session.query(func.max(Targets.target_id)).scalar() + 1
            target_to_insert = Targets(
                target_id = new_target_id,
                mission_id= target_input.mission_id,
                target_industry=target_input.target_industry,
                city_id =target_input.city_id,
                target_type_id =target_input.target_type_id,
                target_priority =target_input.target_priority
            )
            session.add(target_to_insert)
            session.commit()
            session.refresh(target_to_insert)
            return AddTarget(target=target_to_insert)

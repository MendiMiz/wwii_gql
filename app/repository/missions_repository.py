from returns.maybe import Maybe
from app.db.database import session_maker
from app.db.models import Missions


def mission_by_id(mission_id: int) -> Maybe[Missions]:
    with session_maker() as session:
        return Maybe.from_optional(session.query(Missions).filter(Missions.mission_id == mission_id).first())

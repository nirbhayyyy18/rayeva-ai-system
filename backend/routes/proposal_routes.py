from fastapi import APIRouter

from backend.services.ai_proposal_service import generate_proposal

from backend.database.database import SessionLocal
from backend.database.models import Proposal

router = APIRouter()


@router.post("/generate-proposal")
def proposal(data: dict):

    budget = data["budget"]

    event = data["event"]

    audience = data["audience"]

    result = generate_proposal(budget, event, audience)

    db = SessionLocal()

    proposal_data = Proposal(

        budget=budget,

        event=event,

        audience=audience,

        total_cost=result.get("total_cost"),

        impact_summary=result.get("impact_summary")
    )

    db.add(proposal_data)

    db.commit()

    return result
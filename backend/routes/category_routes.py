from fastapi import APIRouter

from backend.services.ai_category_service import generate_category

from backend.database.database import SessionLocal
from backend.database.models import Category

router = APIRouter()


@router.post("/generate-category")
def category(data: dict):

    name = data["name"]

    description = data["description"]

    result = generate_category(name, description)

    db = SessionLocal()

    category_data = Category(

        name=name,

        description=description,

        category=result.get("category"),

        sub_category=result.get("sub_category"),

        tags=",".join(result.get("tags", []))
    )

    db.add(category_data)

    db.commit()

    return result
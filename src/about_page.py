from my_db import MyDb
from my_templates import MyTemplates
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def about_me(req: Request, template: MyTemplates, db: MyDb):
    my_about = await db.find_one({"type": "about_me"})

    if my_about is None:
        my_about = {"description": "temporary"}

    return template.TemplateResponse(
        "pages/main.j2", {"request": req, "about_text": my_about["description"]}
    )

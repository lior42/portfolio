from my_db import MyDb
from my_templates import MyTemplates
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from pydantic import NonNegativeInt

router = APIRouter(prefix="/career")


@router.get("/", response_class=HTMLResponse)
async def career_main_page(
    db: MyDb,
    templates: MyTemplates,
    request: Request,
    start: NonNegativeInt = 0,
    lim: NonNegativeInt = 50,
):
    basic_query = (
        db.find({"type": "career"}).sort([("time_start", -1), ("title", 1)]).limit(lim)
    )

    if start > 0:
        basic_query = basic_query.skip(start)

    all_careers = await basic_query.to_list(None)

    for i in range(len(all_careers)):
        all_careers[i]["time_start"] = all_careers[i]["time_start"].strftime("%b, %Y")
        if all_careers[i].get("time_end") is not None:
            all_careers[i]["time_end"] = all_careers[i]["time_end"].strftime("%b, %Y")

    return templates.TemplateResponse(
        "pages/careers.j2", {"request": request, "career_list": all_careers}
    )

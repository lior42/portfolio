from my_db import MyDb
from my_templates import MyTemplates
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from pydantic import NonNegativeInt
from app_conf import app_conf

router = APIRouter(prefix="/career")


@router.get("/", response_class=HTMLResponse)
async def career_main_page(
    db: MyDb, templates: MyTemplates, request: Request, page: NonNegativeInt = 0
):
    start = page * app_conf.pagination_limit
    lim = app_conf.pagination_limit

    total_pages = __count_total_pages(db)

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

    total_pages_int = await total_pages

    return templates.TemplateResponse(
        "pages/careers.j2",
        {
            "request": request,
            "career_list": all_careers,
            "all_pages": range(total_pages_int),
            "current_page": page,
            "should_display_pagination": total_pages_int > 1,
        },
    )


async def __count_total_pages(db) -> int:
    num_docs = await db.count_documents({"type": "career"})
    return (num_docs + app_conf.pagination_limit - 1) // app_conf.pagination_limit

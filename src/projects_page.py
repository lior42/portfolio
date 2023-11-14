from my_db import MyDb
from my_templates import MyTemplates
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from pydantic import NonNegativeInt
from pathlib import Path
from app_conf import app_conf

router = APIRouter(prefix="/projects")

__STATIC_DIR = Path("static")


@router.get("/", response_class=HTMLResponse)
async def projects_page_main(
    db: MyDb,
    templates: MyTemplates,
    request: Request,
    page: NonNegativeInt = 0,
):
    start = page * app_conf.pagination_limit
    lim = app_conf.pagination_limit

    total_pages = __count_total_pages(db)

    basic_query = db.find({"type": "project"}).sort([("title", 1)]).limit(lim)

    if start > 0:
        basic_query = basic_query.skip(start)

    all_projects = await basic_query.to_list(None)

    github_svg = ""
    github_logo_f = __STATIC_DIR / "images" / "github-logo" / "m-black.svg"

    github_svg = github_logo_f.read_text()
    total_pages_int = await total_pages

    return templates.TemplateResponse(
        "pages/projects.j2",
        {
            "request": request,
            "projects_list": all_projects,
            "github_logo": github_svg,
            "all_pages": range(total_pages_int),
            "current_page": page,
            "should_display_pagination": total_pages_int > 1,
        },
    )


async def __count_total_pages(db) -> int:
    num_docs = await db.count_documents({"type": "project"})
    return (num_docs + app_conf.pagination_limit - 1) // app_conf.pagination_limit

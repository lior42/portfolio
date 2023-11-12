from my_db import MyDb
from my_templates import MyTemplates
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from pydantic import NonNegativeInt
from pathlib import Path

router = APIRouter(prefix="/projects")

__STATIC_DIR = Path("static")


@router.get("/", response_class=HTMLResponse)
async def projects_page_main(
    db: MyDb,
    templates: MyTemplates,
    request: Request,
    start: NonNegativeInt = 0,
    lim: NonNegativeInt = 50,
):
    basic_query = db.find({"type": "project"}).sort([("title", 1)]).limit(lim)

    if start > 0:
        basic_query = basic_query.skip(start)

    all_projects = await basic_query.to_list(None)

    github_svg = ""
    github_logo_f = __STATIC_DIR / "images" / "github-logo" / "m-black.svg"

    github_svg = github_logo_f.read_text()

    return templates.TemplateResponse(
        "pages/projects.j2",
        {"request": request, "projects_list": all_projects, "github_logo": github_svg},
    )

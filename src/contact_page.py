from my_db import MyDb
from my_templates import MyTemplates
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, EmailStr, HttpUrl
from datetime import datetime, timezone


class ContactMeModel(BaseModel):
    name: str
    return_email: EmailStr
    link: HttpUrl | None = None
    company: str | None = None
    job_description: str | None = None


__CONTACT_ME_TYPE = "contact"


router = APIRouter(prefix="/contact")


@router.get("/", response_class=HTMLResponse)
async def contact_main_page(req: Request, template: MyTemplates):
    return template.TemplateResponse("pages/contact.j2", {"request": req})


@router.post("/api")
async def post_contact_me(info: ContactMeModel, db: MyDb):
    to_add = {
        "time_added": datetime.now(timezone.utc),
        "type": __CONTACT_ME_TYPE,
        **info.model_dump(exclude_none=True, mode="json"),
    }

    res = "Thank you for your submission, i will contact you if relevant."
    status = 200

    await db.insert_one(to_add)

    return JSONResponse(
        {
            "content": res,
        },
        status_code=status,
    )

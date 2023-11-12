from fastapi import FastAPI, Request, status
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.exceptions import RequestValidationError
from fastapi.staticfiles import StaticFiles
from uvicorn import run as uvi_run
from my_templates import MyTemplates
from app_conf import app_conf
from career_page import router as router_career
from projects_page import router as router_projects
from contact_page import router as router_contact
from about_page import router as router_about

app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), "static")

app.include_router(router_career)
app.include_router(router_projects)
app.include_router(router_contact)
app.include_router(router_about)


@app.exception_handler(RequestValidationError)
async def validation_error_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"content": exc.body, "details": exc.errors()},
    )


if __name__ == "__main__":
    uvi_run(app, host=app_conf.bind_ip)

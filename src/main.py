from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from uvicorn import run as uvi_run
from my_templates import MyTemplates
from app_conf import app_conf
from career_page import router as router_career
from projects_page import router as router_projects

app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), "static")

app.include_router(router_career)
app.include_router(router_projects)


@app.get("/", response_class=HTMLResponse)
async def example(templates: MyTemplates, req: Request):
    return templates.TemplateResponse("pages/main.j2", {"request": req})


if __name__ == "__main__":
    uvi_run(app, host=app_conf.bind_ip)

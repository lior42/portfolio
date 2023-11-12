from fastapi.templating import Jinja2Templates
from fastapi import Depends
from typing import Annotated

__templates = Jinja2Templates(directory="templates")


def __get_templates():
    return __templates


MyTemplates = Annotated[Jinja2Templates, Depends(__get_templates)]

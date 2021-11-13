from pydantic.fields import Field
from models.domains import page


class PageIn(page.Page):
    page_type:str = Field(alias="PageType")
    pass

class PageResp(page.Page):
    pass
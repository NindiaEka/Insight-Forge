from pydantic import BaseModel
from typing import Optional


class CompanySources(BaseModel):

    company_name: str

    official_website: Optional[str] = None

    linkedin_url: Optional[str] = None

    news_urls: list[str] = []
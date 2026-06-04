from pydantic import BaseModel


class CrawlResult(BaseModel):
    url: str
    markdown: str
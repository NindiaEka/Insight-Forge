from tavily import TavilyClient

from .discovery import SourceDiscovery
from .models import CompanySources


class TavilySourceDiscovery(SourceDiscovery):

    def __init__(self, api_key: str):
        self.client = TavilyClient(api_key=api_key)

    def discover(self, company_name: str) -> CompanySources:

        website_result = self.client.search(
            query=f"{company_name} official website",
            max_results=5
        )

        linkedin_result = self.client.search(
            query=f"{company_name} linkedin",
            max_results=5
        )

        BLOCKED_DOMAINS = [
            "linkedin.com",
            "instagram.com",
            "facebook.com",
            "twitter.com",
            "x.com",
            "leadiq.com",
            "zoominfo.com",
            "crunchbase.com",
        ]

        official_website = None

        for result in website_result["results"]:

            url = result["url"]

            if not any(blocked in url
                for blocked in BLOCKED_DOMAINS):
                official_website = url
                break

        linkedin_url = None

        for result in linkedin_result["results"]:

            url = result["url"]

            if "linkedin.com/company" in url:
                linkedin_url = url
                break

        return CompanySources(
            company_name=company_name,
            official_website=official_website,
            linkedin_url=linkedin_url
        )
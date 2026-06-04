from src.crawler.crawl4ai_crawler import Crawl4AICrawler

crawler = Crawl4AICrawler()

result = crawler.crawl(
    "https://phe.pertamina.com"
)

print(result.markdown[:2000])
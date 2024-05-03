import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from downFiles.items import DownfilesItem


class JkmaSpider(CrawlSpider):
    name = "jkma"
    allowed_domains = ["www.jkma.org"]
    start_urls = ["https://www.jkma.org/articles/archive.php"]
    visited = set()

    rules = (
        # Rule(LinkExtractor(allow=r'current/?vol=67&no=2'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'current/\?vol=\d+&no=\d+$'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        file_urls = []
        matched_elements = response.xpath('//a[@class="icon5"]')
        for el in matched_elements: 
            onclick_value = el.get()
            match = re.search(r'journal_download\("pdf", "\d+", "(.*?\.pdf)"\)', onclick_value)
            if match:
                file_name = match.group(1)
                file_url = 'https://www.jkma.org/upload/pdf/' + file_name
                file_urls.append(file_url)
        with open('urls.txt', 'a') as f:
            for url in file_urls:
                f.write(url + '\n')

# -*- coding: utf-8 -*-
from datetime import date, timedelta
import scrapy

from ..items import AdvertisementItem


class BazosSpider(scrapy.Spider):
    name = "bazos"
    allowed_domains = ["motorky.bazos.cz"]
    start_urls = (
        'http://motorky.bazos.cz/prodam/cestovni/?hledat=&rubriky=motorky&hlokalita=&humkreis=25&cenaod=&cenado=50000&Submit=Hledat&kitx=ano',
        'http://motorky.bazos.cz/prodam/enduro/?hledat=&rubriky=motorky&hlokalita=&humkreis=25&cenaod=&cenado=50000&Submit=Hledat&kitx=ano',
        'http://motorky.bazos.cz/prodam/silnicni/?hledat=&rubriky=motorky&hlokalita=&humkreis=25&cenaod=&cenado=50000&Submit=Hledat&kitx=ano',
    )
    age_threshold = timedelta(days=2)

    def parse(self, response):
        continue_crawling = True
        for ad in response.css("span.vypis"):
            row = ad.xpath("table/tr[1]")
            title = row.xpath("td/span[1]/a/text()").extract_first()
            date_ = row.xpath("td/span[2]/text()").re(r'\d{1,2}\.\d{1,2}\. \d{4}')[0]
            d, m, y = map(int, date_.split("."))
            date_ = date(y, m, d)
            # Stop crawling if the ad is too old
            if date_ < date.today() - self.age_threshold:
                continue_crawling = False
                yield None
            else:
                permalink = response.urljoin(row.xpath("td/span/a/@href").extract_first())
                description = row.xpath("td/div[@class='popis']/text()").extract_first()
                price = row.xpath("td[2]/span/b/text()").extract_first().strip()
                yield AdvertisementItem(title=title, description=description, price=price, permalink=permalink,
                                        date=date_)

        next_url = response.css(".strankovani").xpath("a[last()]/@href").extract()
        if continue_crawling and next_url:
            yield scrapy.Request(response.urljoin(next_url[0]), self.parse)

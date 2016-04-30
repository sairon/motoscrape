# -*- coding: utf-8 -*-
from datetime import date
import scrapy

from ..db import ads_db
from ..items import AdvertisementItem


class MotorkariSpider(scrapy.Spider):
    name = "motorkari"
    allowed_domains = ["www.motorkari.cz"]
    start_urls = (
        'http://www.motorkari.cz/motobazar/motorky/?s[cat]=2&s[cena][1]=50000&s[vykon][0]=25&s[vykon][1]=35&s[typ_pk]=1',
    )

    def make_requests_from_url(self, url):
        request = super(MotorkariSpider, self). make_requests_from_url(url)
        request.cookies['paging-bazar'] = "100"
        return request

    def parse_moto(self, response):
        ad = response.css("div.main")
        title = ad.css("h1::text").extract_first()
        description = ad.xpath("div[2]/div/p/text()").extract_first()
        price = ad.css("td.high.bold.bigger::text").extract_first()
        power = ad.re(u"<th>Výkon:</th>\s*<td>([0-9\.,]*) kW")[0]
        year = ad.re(u"<th>Vyrobeno:</th>\s*<td>(\d+)")[0]
        mileage = ad.re(u"<th>Najeto:</th>\s*<td>(\d+) Km")
        mileage = mileage[0] if mileage else None
        date_ = ad.xpath("div[2]/div/div[@class='info']/p").re("\d{1,2}\.\d{1,2}\.\d{4}")[0]
        d, m, y = map(int, date_.split("."))
        date_ = date(y, m, d)

        return AdvertisementItem(title=title, description=description, price=price, power=power,
                                 year=year, mileage=mileage, permalink=response.url, date=date_)

    def parse(self, response):
        for ad in response.css("ul.list li"):
            url = ad.xpath("div[2]/div/div/h3/a/@href").extract_first()
            if url in ads_db:
                yield None
            else:
                yield scrapy.Request(url, self.parse_moto)

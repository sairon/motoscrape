# -*- coding: utf-8 -*-
from datetime import date
import scrapy

from ..db import ads_db
from ..items import AdvertisementItem


class TipmotoSpider(scrapy.Spider):
    name = "tipmoto"
    allowed_domains = ["www.tipmoto.com", "www.motoinzerce.cz"]
    start_urls = (
        'http://www.motoinzerce.cz/hledat.php?cenaod=&cenado=50000&vykonod=25&vykondo=35&razeni=cenaa&submit.x=0&submit.y=0&strankovani=100',
        'http://www.tipmoto.com/hledat.php?vykonod=25&vykondo=35&cenaod=&cenado=50000&razeni=cenaa&submit.x=0&submit.y=0&strankovani=100',
    )

    def parse_moto(self, response):
        ad = response.css("#prava-in")
        title = ad.xpath("h1/text()").extract_first()
        description = ad.xpath("div/div[@id='detail-popis']/h2[text()='Popis:']/following-sibling::p/text()").extract_first()
        price = ad.xpath("p[@id='detail-cena']/text()").extract_first().strip()
        year = ad.css("div.indent p.d33.d1").re(u"<strong>(Vyrobeno|Provoz):</strong>\s*(\d+)")
        year = year[1] if year else None
        mileage = ad.css("div.indent p.d33.d1").re(u"<strong>Najeto:</strong>\s*(\d+) km")
        mileage = mileage[0] if mileage else None
        power = ad.css("div.indent p.d33.d2").re(u"<strong>Výkon:</strong>\s*([0-9\.,]+)")[0]
        date_ = ad.re(u'<strong>Vloženo:</strong>\s*<span>(.*)</span>') or None
        if date_:
            d, m, y = map(int, date_[0].split("."))
            date_ = date(y, m, d)
        return AdvertisementItem(title=title, description=description, price=price, power=power,
                                 year=year, mileage=mileage, permalink=response.url, date=date_)

    def parse(self, response):
        for ad in response.css("table.vypis tr:not(.th):not(.prvnitipmoto):not(.tipmoto):not(.tipmotoposledni)"):
            url = response.urljoin(ad.xpath("td[1]/a/@href").extract_first())
            if url in ads_db:
                yield None
            else:
                yield scrapy.Request(url, self.parse_moto)

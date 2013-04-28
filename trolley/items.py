from __future__ import unicode_literals

from scrapy.item import Item, Field


class ShopItem(Item):
    name = Field()
    price = Field()
    extra_info = Field()


class CompanyItem(Item):
    name = Field()
    code = Field()
    price = Field()
    change = Field()
    bid = Field()
    offer = Field()
    open = Field()
    high = Field()
    low = Field()
    vol = Field()

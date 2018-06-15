from __future__ import absolute_import

from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity
from scrapy.spiders import Rule

from ..utils.spiders import BasePortiaSpider
from ..utils.starturls import FeedGenerator, FragmentGenerator
from ..utils.processors import Item, Field, Text, Number, Price, Date, Url, Image, Regex
from ..items import PortiaItem


class AltemaJp(BasePortiaSpider):
    name = "altema.jp"
    allowed_domains = [u'altema.jp']
    start_urls = [{u'url': u'https://altema.jp/destinychild/chara/[1-300]',
                   u'fragments': [{u'valid': True,
                                   u'type': u'fixed',
                                   u'value': u'https://altema.jp/destinychild/chara/'},
                                  {u'valid': True,
                                   u'type': u'range',
                                   u'value': u'1-300'}],
                   u'type': u'generated'}]
    rules = [
        Rule(
            LinkExtractor(
                allow=(u'.*/chara/.*'),
                deny=()
            ),
            callback='parse_item',
            follow=True
        )
    ]
    items = [[Item(PortiaItem,
                   None,
                   u'table:nth-child(31) > tr:nth-child(5), table:nth-child(31) > tbody > tr:nth-child(5)',
                   [Field(u'name',
                          'h2:nth-of-type(3) *::text',
                          [Regex(u'(.*)\u306e\u30b9\u30ad\u30eb')]),
                       Field(u'\u901a\u5e38\u653b\u6483',
                             'h2:nth-of-type(3)+table > tbody > tr:nth-child(1) > td *::text',
                             [Regex(u'.*\u3011\\s+(.*)')]),
                       Field(u'\u30ce\u30fc\u30de\u30eb',
                             'h2:nth-of-type(3)+table > tbody > tr:nth-child(2) > td *::text',
                             [Regex(u'.*\u3011\\s+(.*)')]),
                       Field(u'\u30b9\u30e9\u30a4\u30c9',
                             'h2:nth-of-type(3)+table > tbody > tr:nth-child(3) > td *::text',
                             [Regex(u'.*\u3011\\s+(.*)')]),
                       Field(u'\u30c9\u30e9\u30a4\u30d6',
                             'h2:nth-of-type(3)+table > tbody > tr:nth-child(4) > td *::text',
                             [Regex(u'.*\u3011\\s+(.*)')]),
                       Field(u'\u30ea\u30fc\u30c0\u30fc',
                             'table:nth-child(31) > tr:nth-child(5) > td *::text, table:nth-child(31) > tbody > tr:nth-child(5) > td *::text',
                             [])])]]

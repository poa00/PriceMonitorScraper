# -*- coding: utf-8 -*-

from scrapy.loader.processors import MapCompose
from w3lib.html import replace_entities, replace_escape_chars, remove_tags
from price_monitor.item_loaders.product_item_loader import ProductItemLoader, remove_latin_space

class IGAProductItemLoader(ProductItemLoader):
    default_input_processor = MapCompose(remove_tags, replace_escape_chars, replace_entities, remove_latin_space, lambda x: ' '.join(x.split()))
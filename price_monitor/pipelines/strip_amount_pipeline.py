# -*- coding: utf-8 -*-

from price_monitor.items import Offer, Product
from price_monitor.pipelines.price_monitor_pipeline import PriceMonitorPipeline

class StripAmountPipeline(PriceMonitorPipeline):
    def process_item(self, item, spider):
        if item.get(Product.KEY_CURRENT_OFFER) and item.get(Product.KEY_CURRENT_OFFER).get(Offer.KEY_AMOUNT):
            item[Product.KEY_CURRENT_OFFER][Offer.KEY_AMOUNT] = float(item[Product.KEY_CURRENT_OFFER][Offer.KEY_AMOUNT].strip('$'))
        
        return item
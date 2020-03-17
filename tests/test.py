from unittest import TestCase
from crawl import crawl_page


class GetQAPairTestCase(TestCase):

    def setUp(self):
        self.page = 'https://www.fmprc.gov.cn/web/wjdt_674879/fyrbt_674889/t1708958.shtml'

    def test_crawl(self):
        crawl_page(self.page)

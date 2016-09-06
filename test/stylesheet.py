import unittest

from odplib import preso


class TestSize(unittest.TestCase):
    def setUp(self):
        self.red = preso.Template('data/templates/redsmall.otp')
        self.t2014 = preso.Template('data/templates/2014.otp')


    def test_basic(self):
        self.assertEquals(self.red.get_size(), ('20cm', '16cm'))
        self.assertEquals(self.red.get_size('PM1'), ('20cm', '16cm'))

        self.assertEquals(self.t2014.get_size(), ('27.991cm', '21.006cm'))

    def test_frame_prop(self):
        props = self.red.get_frame_properties('redsmall', 'title')
        self.assertEquals(props['width'], '17.999cm')

        props = self.red.get_frame_properties('bad', 'title')
        self.assertEquals(props, None)

        props = self.red.get_frame_properties('redsmall', 'bad')
        self.assertEquals(props, None)

        props = self.t2014.get_frame_properties('Section', 'title')
        self.assertEquals(props['width'], '25.191cm')

    def test_master_page_name(self):
        name = list(self.red.get_master_page_names())
        self.assertEquals(name, ['redsmall'])

        name = list(self.t2014.get_master_page_names())
        self.assertEquals(name, ['MacTemplateNew', 'Section', 'End'])

if __name__ == '__main__':
    unittest.main()

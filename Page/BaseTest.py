from selenium.webdriver.support import expected_conditions as EC

import pytest

from utilities.DriverWrapper import DriverWrapper

@pytest.mark.usefixtures('get_browser_name')
@pytest.mark.usefixtures('get_base_url')
class BaseTest(object):

    def setup(self):
        self.driver = DriverWrapper.get_webdriver()
        try:
            self.driver.maximize_window()

        except Exception as error:
            DriverWrapper.close_driver()
            pytest.fail('Setup test failed: {}'.format(error))

    def teardown(self):
        DriverWrapper.close_driver()


    def add_rout_in_url_and_go_to_url(self, url):
        print('______________base URL_____________')
        print(self.base_url)
        base_url = self.base_url
        edit_url = base_url + url
        print('\n-------edit-url-----------\n' + str(edit_url))
        self.driver.get(edit_url)
        return self




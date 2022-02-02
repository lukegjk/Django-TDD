from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it(self):
        self.browser.get('http://127.0.0.1:8000/')
        # Title should contain 'Lists', if not: test will fail
        self.assertIn('Lists', self.browser.title)
        self.fail('End of test.')


if __name__ == '__main__':
    unittest.main(warnings='ignore')

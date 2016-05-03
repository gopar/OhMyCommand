from django.contrib.auth import get_user_model
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver
from selenium.webdriver.support.ui import Select


User = get_user_model()


class UserStoryTest(StaticLiveServerTestCase):
    SITE_NAME = 'Oh My Command!'

    def setUp(self):
        user = User(username="gopar", email="gopar@gopar.com",
                    first_name="Daniel", last_name="Gopar")
        user.set_password('password')
        user.save()
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_login_and_enter_a_command(self):
        # Gopar goes to website
        self.browser.get(self.live_server_url)

        # He notices the title of the website
        self.assertEqual(self.SITE_NAME, self.browser.title)

        # He clicks the login link
        self.browser.find_element_by_link_text('Log in').click()

        # Gopar fills outs his information
        username_inputbox = self.browser.find_element_by_name('username')
        username_inputbox.send_keys('gopar')

        password_inputbox = self.browser.find_element_by_name('password')
        password_inputbox.send_keys('password')

        # He clicks button to login
        self.browser.find_element_by_class_name('btn').click()

        # He can now see the commands page and sees text welcoming him
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('gopar', header_text)

        # Gopar wants to add a new command
        self.browser.find_element_by_class_name('btn').click()
        # Modal appears
        self.browser.switch_to_active_element()
        # Starts typing in new command
        new_command_inputbox = self.browser.find_element_by_id('newCommand')
        new_command_inputbox.send_keys('rm -rf')

        new_os_inputbox = Select(self.browser.find_element_by_id('newOs'))
        new_os_inputbox.select_by_value('L')

        new_version_inputbox = self.browser.find_element_by_id('newVersion')
        new_version_inputbox.send_keys('0.1')

        new_note_inputbox = self.browser.find_element_by_id('newNote')
        new_note_inputbox.send_keys('Deletes everything')

        # Submits the new command
        self.browser.find_element_by_css_selector('button[class="btn btn-primary"]').click()

        # Focus back to main page
        self.browser.switch_to.default_content()

        import time;time.sleep(5)
        self.fail('finish making tests')

from seleniumbase import BaseCase
from selenium import webdriver
driver = webdriver.Chrome()


class LoginDelete(BaseCase):
    def test_login_delete(self):
        # open page
        self.open("http://localhost:3000/")

        # click login
        self.click(".css-svqtq2")
        get_started_url = self.get_current_url()
        self.assert_equal(get_started_url,"http://localhost:3000/Login")

        self.sleep(1)

        # login
        self.send_keys('#username', 'kevink')
        # self.sleep(1)
        self.send_keys('#password', 'drillshare777')
        # self.sleep(1)
        self.click("#log-in-button")
        self.sleep(1)

        # check to see if we are on home url logged in
        get_started_url = self.get_current_url()
        self.assert_equal(get_started_url, "http://localhost:3000/")

        # fill form
        self.send_keys("#search", "Test Create Form")
        self.sleep(1)

        # hit enter
        self.click("#enter")
        self.sleep(1)

        # check to see if we are on search page
        get_started_url = self.get_current_url()
        self.assert_equal(get_started_url, "http://localhost:3000/search")

        # click listing button
        # self.sleep(1)
        self.find_element('h5:contains("Test Create Form")').click()

        # check to see if we are on new listing url logged in
        get_started_url = self.get_current_url()
        self.assert_equal(get_started_url, "http://localhost:3000/listing")

        # click delete button
        self.sleep(1)
        self.click("#delete-button")

        self.sleep(1)
        self.click("#confirm-delete")
        self.sleep(1)
        # check to see if we are on home url with listing gone
        get_started_url = self.get_current_url()
        self.assert_equal(get_started_url, "http://localhost:3000/")

        self.sleep(3)

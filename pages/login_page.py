from pages.base_page import BasePage
from config.config import BASE_URL

class LoginPage(BasePage):

    def navigate(self):
        self.page.goto(f"{BASE_URL}/web/index.php/auth/login")

    def login(self, username, password):
        self.get_by_role("textbox", name="Username").fill(username)
        self.get_by_role("textbox", name="Password").fill(password)
        self.get_by_role("button", name="Login").click()

    def is_login_successful(self):
        return self.page.get_by_role("link", name="My Info").is_visible()

    def is_invalid_credentials_displayed(self):
        return self.page.get_by_text("Invalid credentials").is_visible()
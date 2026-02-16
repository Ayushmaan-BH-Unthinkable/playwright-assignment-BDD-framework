from pages.base_page import BasePage


class DashboardPage(BasePage):

    def click_admin_menu(self):
        self.get_by_role("link", name="Admin").click()

    def logout(self):
        # Click user dropdown (top right profile)
        self.page.locator("span.oxd-userdropdown-tab").click()
        self.get_by_role("menuitem", name="Logout").click()

    def is_login_page_displayed(self):
        return self.get_by_role("heading", name="Login").is_visible()

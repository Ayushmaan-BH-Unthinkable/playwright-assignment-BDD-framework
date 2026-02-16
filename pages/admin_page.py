from pages.base_page import BasePage

class AdminPage(BasePage):

    def click_add_user(self):
        self.get_by_role("button", name="Add").click()

    def select_user_role(self, role):
        self.page.locator("div.oxd-select-text").first.click()
        self.get_by_role("option", name=role).click()

    def select_employee(self, employee_name):
        self.get_by_role("textbox", name="Type for hints...").fill(employee_name)
        self.get_by_role("option", name=employee_name).click()

    def select_status(self, status):
        self.page.locator("div.oxd-select-text").nth(1).click()
        self.get_by_role("option", name=status).click()

    def enter_username(self, username):
        self.page.locator("//div[normalize-space()='Username']//following-sibling::input").first.fill(username)

    def enter_password(self, password):
        self.page.locator("//div[normalize-space()='Password']//following-sibling::input").first.fill(password)

    def confirm_password(self, password):
        self.page.locator("//div[normalize-space()='Confirm Password']//following-sibling::input").fill(password)

    def click_save(self):
        self.page.locator("//button[normalize-space()='Save']").click()

    def search_user(self, username):
        self.page.locator("input").nth(1).fill(username)
        self.get_by_role("button", name="Search").click()

    def verify_user_present(self, username):
        self.get_by_text(username).click()
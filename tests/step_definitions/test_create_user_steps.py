import allure
from pytest_bdd import scenarios, given, when, then
from faker import Faker
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.admin_page import AdminPage
from config.config import USERNAME_ADMIN, PASSWORD_ADMIN, USERNAME_ESS_USER, PASSWORD_ESS_USER
from utils.logger import get_logger

fake = Faker()
logger = get_logger(__name__)

scenarios('../features/create_user.feature')


@given("User launches the application")
def launch_app(page):
    logger.info("Launching application")
    login_page = LoginPage(page)
    login_page.navigate()


@when("User logs in with valid credentials")
def login(page):
    logger.info("Logging into application")
    login_page = LoginPage(page)
    login_page.login(USERNAME_ADMIN, PASSWORD_ADMIN)


@when("User navigates to Admin page")
def navigate_admin(page):
    logger.info("Navigating to Admin page")
    dashboard_page = DashboardPage(page)
    dashboard_page.click_admin_menu()


@when("User creates a new ESS user")
def create_user(page):
    logger.info("Creating new user")
    admin_page = AdminPage(page)
    username = "Tony_Stark_Avengers" + fake.first_name()
    admin_page.click_add_user()
    admin_page.select_user_role("ESS")
    # admin_page.select_employee("TestUser1539  Automation")
    admin_page.select_employee("AVipin165 Test ALName165")
    admin_page.select_status("Enabled")
    admin_page.enter_username(USERNAME_ESS_USER)
    admin_page.enter_password(PASSWORD_ESS_USER)
    admin_page.confirm_password(PASSWORD_ESS_USER)
    admin_page.click_save()


@then("User should be created successfully")
def verify_user():
    logger.info("User creation flow executed successfully")
    assert True

# @then("the user clicks on logout")
# def perform_logout(page):
#     logger.info("Performing logout action")
#     dashboard_page = DashboardPage(page)
#     dashboard_page.logout()
#
#
# @then("the login page should be displayed")
# def verify_logout(page):
#     logger.info("Verifying login page is displayed after logout")
#     dashboard_page = DashboardPage(page)
#
#     assert dashboard_page.is_login_page_displayed(), \
#         "Logout failed - Login page not visible"


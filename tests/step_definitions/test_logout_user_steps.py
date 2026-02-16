import allure
from pytest_bdd import scenarios, given, when, then
import pytest

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from config.config import USERNAME_ADMIN, PASSWORD_ADMIN
from utils.logger import get_logger

logger = get_logger(__name__)

scenarios("../features/logout.feature")


# ---------------- FIXTURES ---------------- #

@pytest.fixture
def login_page(page):
    logger.info("Launching application and logging in as Admin")

    login = LoginPage(page)

    with allure.step("Navigate to Login Page"):
        login.navigate()

    with allure.step("Login as Admin"):
        login.login(USERNAME_ADMIN, PASSWORD_ADMIN)

    return login


@pytest.fixture
def dashboard_page(login_page):
    return DashboardPage(login_page.page)


# ---------------- GIVEN ---------------- #

@given("the user is logged into the application")
def user_logged_in(login_page):
    logger.info("User successfully logged into application")
    return login_page


# ---------------- WHEN ---------------- #

@when("the user clicks on logout")
def perform_logout(dashboard_page):
    logger.info("Performing logout action")

    with allure.step("Click Logout from user dropdown"):
        dashboard_page.logout()


# ---------------- THEN ---------------- #

@then("the login page should be displayed")
def verify_logout(dashboard_page):
    logger.info("Verifying login page is displayed")

    with allure.step("Verify Login page is visible"):
        assert dashboard_page.is_login_page_displayed(), \
            "Logout failed - Login page not visible"

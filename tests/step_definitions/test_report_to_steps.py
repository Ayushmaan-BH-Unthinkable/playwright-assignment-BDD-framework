import allure
from pytest_bdd import scenarios, when, then, given, parsers
import pytest

from pages.myinfo_page import MyInfoPage
from pages.login_page import LoginPage
from config.config import USERNAME_ESS_USER, PASSWORD_ESS_USER
from utils.logger import get_logger

logger = get_logger(__name__)

scenarios("../features/report_to.feature")


# ---------------- FIXTURES ---------------- #

@pytest.fixture
def login_page(page):
    logger.info("Launching application and logging in as ESS user")

    login = LoginPage(page)

    with allure.step("Navigate to Login Page"):
        login.navigate()

    with allure.step("Login as ESS User"):
        login.login(USERNAME_ESS_USER, PASSWORD_ESS_USER)

    return login


@pytest.fixture
def myinfo_page(login_page):
    return MyInfoPage(login_page.page)


# ---------------- GIVEN ---------------- #

@given("user is logged in as ESS user")
def login(login_page):
    logger.info("ESS user logged in successfully")
    return login_page


# ---------------- WHEN ---------------- #

@when("user navigates to MyInfo tab")
def open_myinfo(myinfo_page):
    logger.info("Navigating to MyInfo tab")

    with allure.step("Open MyInfo tab"):
        myinfo_page.open_myinfo_tab()


@when(parsers.parse('user opens "{section}" section'))
def open_section(myinfo_page, section):
    logger.info(f"Opening section: {section}")

    with allure.step(f"Open {section} section"):
        myinfo_page.open_section(section)


# ---------------- THEN ---------------- #

@then("supervisors list should be visible")
def verify_supervisors(myinfo_page):
    logger.info("Verifying supervisors list is visible")

    with allure.step("Verify supervisors table is visible"):
        assert myinfo_page.is_supervisors_list_visible(), \
            "Supervisors list is not visible"

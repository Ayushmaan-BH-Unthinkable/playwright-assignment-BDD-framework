import allure
from pytest_bdd import scenarios, when, then, given, parsers
import pytest

from pages.myinfo_page import MyInfoPage
from pages.login_page import LoginPage
from config.config import USERNAME_ESS_USER, PASSWORD_ESS_USER
from utils.logger import get_logger

logger = get_logger(__name__)

scenarios("../features/immigration.feature")


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
    logger.info("ESS User logged in successfully")
    return login_page


# ---------------- WHEN ---------------- #

@when("user navigates to MyInfo tab")
def open_myinfo(myinfo_page):
    logger.info("Navigating to MyInfo tab")

    with allure.step("Click MyInfo tab"):
        myinfo_page.open_myinfo_tab()


@when(parsers.parse('user opens "{section}" section'))
def open_section(myinfo_page, section):
    logger.info(f"Opening section: {section}")

    with allure.step(f"Open {section} section"):
        myinfo_page.open_section(section)


@when(parsers.parse('user adds immigration record with number "{number}"'))
def add_immigration(myinfo_page, number):
    logger.info(f"Adding immigration record with number: {number}")

    with allure.step("Add immigration record"):
        assert myinfo_page.add_immigration(number), \
            "Immigration record was not saved successfully"


# ---------------- THEN ---------------- #

@then(parsers.parse('immigration record "{number}" should appear in table'))
def verify_immigration(myinfo_page, number):
    logger.info(f"Verifying immigration record exists: {number}")

    with allure.step("Verify immigration record present in table"):
        assert myinfo_page.is_record_present(number), \
            "Immigration record not found in table"

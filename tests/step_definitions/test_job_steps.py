import allure
from pytest_bdd import scenarios, given, when, then, parsers
import pytest

from pages.login_page import LoginPage
from pages.myinfo_page import MyInfoPage
from config.config import USERNAME_ESS_USER, PASSWORD_ESS_USER
from utils.logger import get_logger

logger = get_logger(__name__)

scenarios("../features/job.feature")


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

@then(parsers.parse('the following fields should not be editable: {fields}'))
def fields_not_editable(myinfo_page, fields):
    logger.info(f"Validating non-editable fields: {fields}")

    field_list = [f.strip() for f in fields.split(',')]

    with allure.step("Validate fields are not editable"):
        for field_name in field_list:
            assert not myinfo_page.is_field_editable_by_label(field_name), \
                f"Field '{field_name}' is editable!"

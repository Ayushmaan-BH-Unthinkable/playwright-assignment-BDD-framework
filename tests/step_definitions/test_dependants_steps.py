import allure
from pytest_bdd import scenarios, when, then, given, parsers
import pytest

from config.config import USERNAME_ESS_USER, PASSWORD_ESS_USER
from pages.login_page import LoginPage
from pages.myinfo_page import MyInfoPage
from utils.logger import get_logger

logger = get_logger(__name__)

scenarios("../features/dependants.feature")


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


# ---------------- STEP DEFINITIONS ---------------- #

@given("user is logged in as ESS user")
def login(login_page):
    logger.info("User logged in successfully")
    return login_page


@when("user navigates to MyInfo tab")
def open_myinfo(myinfo_page):
    logger.info("Navigating to MyInfo tab")

    with allure.step("Click MyInfo tab"):
        myinfo_page.open_myinfo_tab()


@when('user opens "Dependents" section')
def open_dependents(myinfo_page):
    logger.info("Opening Dependents section")

    with allure.step("Open Dependents section"):
        myinfo_page.open_dependents_section()


@when(parsers.parse('user adds dependent with name "{name}"'))
def add_dependant(myinfo_page, name):
    logger.info(f"Adding dependent: {name}")

    with allure.step("Add dependent details"):
        myinfo_page.add_dependant(name, "Child", "2020-01-01")


@then("record should be saved successfully")
def verify_save_success(myinfo_page):
    logger.info("Verifying success message")

    with allure.step("Verify success toast"):
        assert myinfo_page.wait_for_success_message(), \
            "Dependent was not saved successfully"

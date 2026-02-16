import allure
from pytest_bdd import scenarios, given, when, then, parsers
import pytest

from pages.login_page import LoginPage
from pages.myinfo_page import MyInfoPage
from config.config import USERNAME_ESS_USER, PASSWORD_ESS_USER
from utils.logger import get_logger

logger = get_logger(__name__)

scenarios("../features/emergency_contacts.feature")


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
    logger.info("ESS User logged in successfully")
    return login_page


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


@when(parsers.parse('user adds emergency contact with name "{name}"'))
def add_emergency_contact(myinfo_page, name):
    logger.info(f"Adding emergency contact: {name}")

    with allure.step("Add emergency contact details"):
        myinfo_page.add_emergency_contact(
            name=name,
            relation="Brother",
            home="1111111111",
            mobile="9999999999",
            work="2222222222"
        )


@then("record should be saved successfully")
def verify_record_saved(myinfo_page):
    logger.info("Verifying emergency contact saved")

    with allure.step("Verify record present in table"):
        assert myinfo_page.wait_for_success_message(), \
            "Record was not saved successfully"


@when(parsers.parse('user deletes record "{name}"'))
def delete_record(myinfo_page, name):
    logger.info(f"Deleting record: {name}")

    with allure.step(f"Delete record {name}"):
        myinfo_page.delete_record(name)


@then("record should be deleted successfully")
def verify_record_deleted(myinfo_page):
    logger.info("Verifying record deletion")

    with allure.step("Verify record no longer present"):
        assert not myinfo_page.is_record_present("Rahul"), \
            "Record was not deleted successfully"

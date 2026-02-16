import allure
from pytest_bdd import scenarios, given, when, then, parsers
import pytest

from pages.login_page import LoginPage
from pages.myinfo_page import MyInfoPage
from config.config import USERNAME_ESS_USER, PASSWORD_ESS_USER
from utils.logger import get_logger

logger = get_logger(__name__)

scenarios("../features/myinfo.feature")


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


@when(parsers.parse(
    'user updates First Name "{first}", Middle Name "{middle}", Last Name "{last}"'
))
def edit_details(myinfo_page, first, middle, last):
    logger.info(f"Updating personal details: {first} {middle} {last}")

    with allure.step("Edit personal details"):
        myinfo_page.edit_personal_details(first, middle, last)


@when("user clicks save")
def save_details(myinfo_page):
    logger.info("Clicking Save button")

    with allure.step("Save personal details"):
        myinfo_page.save_personal_details()


# ---------------- THEN ---------------- #

@then("personal details should be updated")
def verify_update(myinfo_page):
    logger.info("Verifying personal details updated")

    with allure.step("Verify updated values in input fields"):
        assert myinfo_page.get_first_name() == "Test"
        assert myinfo_page.get_last_name() == "User"


@then("restricted fields should not be editable")
def restricted_fields(myinfo_page):
    logger.info("Verifying restricted fields are not editable")

    restricted_labels = ["Employee Id"]

    with allure.step("Validate restricted fields"):
        for field in restricted_labels:
            assert not myinfo_page.is_field_editable_by_label(field), \
                f"Field '{field}' is editable"


# ---------------- PHOTO UPLOAD ---------------- #

@when(parsers.parse('user uploads photo "{file_path}"'))
def upload_photo(myinfo_page, file_path):
    logger.info(f"Uploading photo: {file_path}")

    with allure.step(f"Upload photo: {file_path}"):
        myinfo_page.upload_photo(file_path)


@then(parsers.parse('upload should be "{result}"'))
def verify_upload(myinfo_page, result):
    logger.info(f"Verifying upload result: {result}")

    with allure.step("Validate upload result"):
        if result == "success":
            assert myinfo_page.is_upload_successful(), \
                "Expected upload to succeed but it failed"
        else:
            assert myinfo_page.is_upload_failed(), \
                "Expected upload to fail but it succeeded"

import allure
from pytest_bdd import scenarios, given, when, then, parsers
from config.config import USERNAME_ESS_USER, PASSWORD_ESS_USER
from pages.login_page import LoginPage
from utils.logger import get_logger

logger = get_logger(__name__)

scenarios("../features/ess_login.feature")


# ---------------- STEP DEFINITIONS ---------------- #

@given("the user is on the login page")
def navigate_to_login(page):
    logger.info("Navigating to login page")

    login_page = LoginPage(page)

    with allure.step("Navigate to Login Page"):
        login_page.navigate()


@when(parsers.parse('the user logs in with "{username}" and "{password}"'))
def login_with_credentials(page, username, password):
    # load ENV variables dynamically in the test
    if username == "USERNAME_ESS_USER":
        username = USERNAME_ESS_USER

    if password == "PASSWORD_ESS_USER":
        password = PASSWORD_ESS_USER

    logger.info(f"Attempting login with Username: {username}")

    login_page = LoginPage(page)

    with allure.step(f"Login with Username: {username}"):
        login_page.login(username, password)


@then(parsers.parse('"{result}" should be displayed'))
def verify_login_result(page, result):
    logger.info(f"Verifying result: {result}")

    with allure.step(f"Verify expected result: {result}"):

        if result == "MyInfo page visible":
            assert LoginPage.is_login_successful()
            assert page.get_by_role("link", name="My Info").is_visible(), \
                "MyInfo page not visible after login"

        elif result == "Invalid credentials":
            assert LoginPage.is_invalid_credentials_displayed()
            assert page.get_by_text("Invalid credentials").is_visible(), \
                "Invalid credentials message not displayed"

        else:
            raise AssertionError(f"Unknown expected result: {result}")

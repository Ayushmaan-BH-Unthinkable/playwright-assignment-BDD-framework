Feature: Logout Functionality

  Scenario: Successful logout from application
    Given the user is logged into the application
    When the user clicks on logout
    Then the login page should be displayed

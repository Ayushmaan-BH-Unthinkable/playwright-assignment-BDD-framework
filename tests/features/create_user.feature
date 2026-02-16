Feature: Admin User Management

  Scenario: Create a new user successfully
    Given User launches the application
    When User logs in with valid credentials
    And User navigates to Admin page
    And User creates a new ESS user
    Then User should be created successfully
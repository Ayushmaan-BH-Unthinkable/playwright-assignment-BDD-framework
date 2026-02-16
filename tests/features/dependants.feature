Feature: Dependants Management

  Scenario: ESS user can add Dependants
    Given user is logged in as ESS user
    When user navigates to MyInfo tab
    And user opens "Dependents" section
    And user adds dependent with name "Aman"
    Then record should be saved successfully

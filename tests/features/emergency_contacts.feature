Feature: Emergency Contacts Management

  Scenario: ESS user can add Emergency Contact
    Given user is logged in as ESS user
    When user navigates to MyInfo tab
    And user opens "Emergency Contacts" section
    And user adds emergency contact with name "Rahul"
    Then record should be saved successfully

  Scenario: ESS user can delete Emergency Contact
    Given user is logged in as ESS user
    When user navigates to MyInfo tab
    And user opens "Emergency Contacts" section
    And user deletes record "Rahul"
    Then record should be deleted successfully

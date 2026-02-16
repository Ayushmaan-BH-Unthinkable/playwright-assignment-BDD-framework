Feature: Job Section Restrictions

  Scenario: ESS user cannot edit Job fields
    Given user is logged in as ESS user
    When user navigates to MyInfo tab
    And user opens "Job" section
    Then the following fields should not be editable: Joined Date

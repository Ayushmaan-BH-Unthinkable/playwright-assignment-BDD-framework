Feature: Report To Section

  Scenario: ESS user can view supervisors
    Given user is logged in as ESS user
    When user navigates to MyInfo tab
    And user opens "Report-to" section
    Then supervisors list should be visible

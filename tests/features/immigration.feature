Feature: Immigration Management

  Scenario: ESS user can add Immigration record
    Given user is logged in as ESS user
    When user navigates to MyInfo tab
    And user opens "Immigration" section
    And user adds immigration record with number "ABC123"
    Then immigration record "ABC123" should appear in table

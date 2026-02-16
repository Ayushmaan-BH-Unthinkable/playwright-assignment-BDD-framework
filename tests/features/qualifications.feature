Feature: Qualifications Section

  Scenario: ESS user can add Work Experience
    Given user is logged in as ESS user
    When user navigates to MyInfo tab
    And user opens "Qualifications" section
    And user adds work experience for company "TCS"
    Then qualification "TCS" should appear in table

  Scenario: ESS user can add Education
    Given user is logged in as ESS user
    When user navigates to MyInfo tab
    And user opens "Qualifications" section
    And user adds education with institute "IIT"
    Then qualification "IIT" should appear in table

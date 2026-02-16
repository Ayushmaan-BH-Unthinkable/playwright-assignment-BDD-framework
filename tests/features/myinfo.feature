Feature: Orange HRM - MyInfo Module
  ESS User should be able to view and edit personal details and upload photographs

  Scenario: ESS User can edit Personal Details
    Given user is logged in as ESS user
    When user navigates to MyInfo tab
    And user updates First Name "Test", Middle Name "Auto", Last Name "User"
    And user clicks save
    Then personal details should be updated

  Scenario: ESS User cannot edit restricted fields
    Given user is logged in as ESS user
    When user navigates to MyInfo tab
    Then restricted fields should not be editable

  Scenario Outline: ESS User uploads photograph
    Given user is logged in as ESS user
    When user navigates to MyInfo tab
    And user uploads photo "<file_path>"
    Then upload should be "<result>"

    Examples:
      | file_path                     | result  |
      | tests/files/photo1.jpg        | success |
      | tests/files/photo2.gif        | success |
      | tests/files/photo3.png        | success |
      | tests/files/photo4.png        | fail    |
      | tests/files/photo5.gif        | fail    |
      | tests/files/vs_BuildTools.exe | fail    |

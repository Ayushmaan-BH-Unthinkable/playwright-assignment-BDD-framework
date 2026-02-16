Feature: ESS Login

  Scenario Outline: ESS login validation
    Given the user is on the login page
    When the user logs in with "<username>" and "<password>"
    Then "<result>" should be displayed

    Examples:
      | TC_ID         | username          | password          | result              |
      | TC_MyInfo_001 | USERNAME_ESS_USER | PASSWORD_ESS_USER | MyInfo page visible |
      | TC_MyInfo_002 | USERNAME_ESS_USER | xxxxxx            | Invalid credentials |
      | TC_MyInfo_003 | xxxxxxxx          | PASSWORD_ESS_USER | Invalid credentials |
      | TC_MyInfo_004 | xxxxxxxx          | xxxxxx            | Invalid credentials |

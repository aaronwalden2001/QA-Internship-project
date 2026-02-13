# Created by aaronwalden at 2/13/26
Feature: Change Password

  Scenario: User can open change password page
    Given User opens the main page
    When User logs in with valid credentials
    And User clicks on the settings option
    And User clicks on Change password
    Then Change password page should open
    And User fills in new password fields
    And Change password button should be visible

Feature: Verify the UCM College's Master Program

  Scenario: Hit UCM Website and get list of Courses available in this University
    Given Launch the chrome driver and navigate to Official site of UCM
    Then  Look for available courses list under "UCM Programs" and get the list of it


Scenario: Validate Whether Computer Science is available in UCM
   Given List of available courses in UCM
   Then Validate that "Computer Science" is available as part of Masters Program
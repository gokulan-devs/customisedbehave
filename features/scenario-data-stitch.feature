Feature: Scenario - Data - Sticher POC
	
        Scenario: Enter data from csv to form
            Given Google Contact Form is launched
             When User enter Name,Email,Address,Phone Number
              And Submit
             Then Google form confirmation message should displayed

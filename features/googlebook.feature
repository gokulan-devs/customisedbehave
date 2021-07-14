Feature: Verify Google Book page
	
	Scenario: Verify logo of Google Book home page
		Given Google page is launched
		When User navigates to Google books app
		Then Google book logo should appear in the page
	
	Scenario : Search Ponniyin Selvan book
		Given Google book page is on browser
		When User enter Ponniyin Selvan in book search field
		And user hit enter on search field
		Then Search results page should appear with link text ponniyin selvan
		
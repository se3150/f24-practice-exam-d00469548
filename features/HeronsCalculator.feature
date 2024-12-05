Feature: calculate the area of a triangle
As an aspiring mathematician
I should be able to calculate the area of a triangle
So that I can chat with my math friends like a pro

 Background:
   Given I open the url "https://byjus.com/herons-calculator/"
   And I pause for 500ms

 Scenario: I can calculate the area of a triangle
   When I set "20" to the inputfield "#a"
   And I set "26" to the inputfield "#b"
   And I set "7" to the inputfield "#c"
   And I click on the button ".clcbtn"
   Then I expect that element "#_d" contains the text "40.981"

 Scenario: I can use bad inputs and not crash the website
   When I set "20" to the inputfield "#a"
   And I set "20" to the inputfield "#b"
   And I set "41" to the inputfield "#c"
   And I click on the button ".clcbtn"
   Then I expect that a alertbox is opened
    


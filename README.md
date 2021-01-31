# pokerOddsCalc
Uses screen recognition and inputs your hand into a readily-available online hand-odds calcualtor.

For use with POKERSTARS desktop windows app. User must also have firefox and have Geckodriver.exe installed.

The calcuatlor is simply the one readily available at 888 Poker. This program only captures the data from the players POKERSTARS app screen, and enters it into the calcualor faster than a human could. This program does not hack or in anyway provide an advantage that is not already available to the player.

For use with 1920x1080 displays only.

This program uses real-time image capture to input your hand into the odd calcuatlor so these exact settings must be entered into the POKERSTARS app:
  -Table Appearance>Theme =Mercury (see uploaded "tableSample.png" to see which front and back card deck must be selected.
  -Table Appearance>Animation>Throwables = Disabled
  -Table Appearance>Chat>Display Chat Bubbles = Off
  -Table Appearance>Chat>Display Emoticons = Off
  
  When the program starts it will ask:
  
 Display the calculator on the same screen as the poker table? Y/N:
  User can choose to display the calculator on the same screen as the POKERSTARS app or on a seperate display if detected
  
Enter how many seats at table:
The player must enter depending on the table size they have chosen to play at.

It will then ask, depending on the answer given above, which seat the player has chosen to sit at:
Please select own seat number 1-N clockwise:
The player must enter which seat position they are sitting at, starting from 12-o'clock and working clockwise.
 
The program will then start geckdriver.exe and a firefox window will appear with the calculator displayed.  Another window will also apear with a handy poker hands ranking cheat-sheet for reference.

If the calcualtor has been initiated halfway through a hand or if there are windows/objects blocking the view of the program, then the cacluatlor will settle and start working properly on the next round.

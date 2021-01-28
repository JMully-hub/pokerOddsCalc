# pokerOddsCalc
Uses screen recognition and inputs your hand into a readily-available online hand-odds calcualtor.

For use with POKERSTARS desktop windows app. User must also have firefox and have Geckodriver.exe installed.

The calcuatlor is simply the one readily available at 888 Poker. This program only captures the data from the players POKERSTARS app screen, and enters it into the calcualor faster than a human could. This program does not hack or in anyway provide an advantage that is not already available to the player.

The POKERSTARS desktop app must be enlarged to full screen on the user's primary display and must be 1920x1080, the calculator is best viewed on a seperate display to the POKERSTARS app. If a seperate display is not available then the calculator window size must be reduced as not to overlap any of the other player's cards. The calculator can be placed in the bottom-left of the display; covering the chatbox but must not cover the card-backs of the player in the bottom-left.

This program uses real-time image capture to input your hand into the odd calcuatlor so these exact settings must be entered into the POKERSTARS app:
  -Table Appearance>Theme =Mercury (see uploaded "tableSample.png" to see which front and back card deck must be selected.
  -Table Appearance>Animation>Throwables = Disabled
  -Table Appearance>Chat>Display Chat Bubbles = Off
  -Table Appearance>Chat>Display Emoticons = Off
  
  When the program starts it will ask:
    Enter how many seats at table:
    * 2
    * 6
    * 9
The player must enter depending on the table size they have chosen to play at.

It will then ask, depending on the answer given above, which seat the player has chosen to sit at:
  Please select own seat number 1-N clockwise:
  * 1
  * 2
  * 3
  * 4
  * N
 The player must enter which seat position they are sitting at, starting from 12-o'clock and working clockwise..
 
The program will then start geckdriver.exe and a firefox window will appear with the calculator displayed. The user must then move the firefox window so that it does not interfere with the image capture of the POKERSTARS app, a seperate display is best.

If the calcualtor has been initiated halfway through a hand or if there are windows/objects blocking the view of the program, then the cacluatlor will settle and start working properly on the next round.

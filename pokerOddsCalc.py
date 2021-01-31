#! python3
# pokerOdds.py - Simple screen recognition software to input current screen data to a ready-made poker
# hands online calculator


import sys, time, pyautogui, subprocess, os, logging, cv2
import pygetwindow as gw
from screeninfo import get_monitors
import pyinputplus as pyip
from pathlib import Path
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options

logging.disable(logging.CRITICAL)
logging.basicConfig(level=logging.INFO, format='%(asctime)s -  %(levelname)s-  %(message)s')
logging.info('Start of program')

def activePlayers():
    otherPlayers = 0
    for location in playerSeats:
        if pyautogui.locateOnScreen(str(Path('./images/'+screenKey+'cardBack.png')),
                                    region=(playerSeats[location]), confidence=0.99) is not None:
            otherPlayers = otherPlayers + 1
    return otherPlayers

def findCard(dictionary, key):
    deckList =  os.listdir(Path('./images/'+screenKey+'suits'))
    returnDic = {}
    for s in deckList:
        if pyautogui.locateOnScreen(str(Path('./images/'+screenKey+'suits/'+s)),
                                    region=dictionary[key], confidence=0.99) is not None:
            suit = str(os.path.basename(s)).replace('.png', '')
            if suit == 'HEART' or suit == 'DIAMOND':
                valueList = os.listdir(str(Path('./images/'+screenKey+'redValues')))
                for v in valueList:
                    if pyautogui.locateOnScreen(str(Path('./images/'+screenKey+'redValues/'+v)),
                                                region=dictionary[key], confidence=0.99) is not None:
                        value = str(os.path.basename(v)).replace('.png', '')
                        card = value+suit
                        returnDic.setdefault('SUIT', suit)
                        returnDic.setdefault('CARD', card)
                        return returnDic
            elif suit == 'CLUB' or suit == 'SPADE':
                valueList = os.listdir(str(Path('./images/'+screenKey+'blackValues')))
                for v in valueList:
                    if pyautogui.locateOnScreen(str(Path('./images/'+screenKey+'blackValues/'+v)),
                                                region=dictionary[key], confidence=0.99) is not None:
                        value = str(os.path.basename(v)).replace('.png', '')
                        card = value+suit
                        returnDic.setdefault('SUIT', suit)
                        returnDic.setdefault('CARD', card)
                        return returnDic
                
def StartNewRound():
    reset.click()
    resetConfirm.click()
    while True:
        time.sleep(0.5)
        newRoundStarted = activePlayers()
        if newRoundStarted != 0:
            break
        
def playerAddRemove():
    calcPlayers = -1
    for i in playerTables:
        isInactive = "inactive" in i.get_attribute("data-status")
        if isInactive is False:
            calcPlayers = calcPlayers +1
    playerDifference = calcPlayers - players
    if playerDifference < 0:
    # add to calc
        playerDifference = playerDifference *-1
        for i in range(playerDifference):
            driver.execute_script("arguments[0].scrollIntoView(true);", addPlayer)
            addPlayer.click()
            driver.execute_script("arguments[0].scrollIntoView(true);", tableView)
    elif playerDifference > 0:
    #remove from calc
        removePlayersLink.click()
        for i in range(playerDifference):
            removePlayer.click()
        closeremovePlayersLink.click()

def clickMyCards():
    myCalcCard1.click()
    index = myCard1['SUIT']
    link = deckDict[index]
    link.click()
    index = myCard1['CARD']
    link = deckDict[index]
    link.click()
    index = myCard2['SUIT']
    link = deckDict[index]
    link.click()
    link.click()
    index = myCard2['CARD']
    link = deckDict[index]
    link.click()
    done.click()

def clickAllFlopCards():
    flop1Click.click()
    cardSelViewFlop1.click()
    index = firstFlop['SUIT']
    link = deckDict[index]
    link.click()
    index = firstFlop['CARD']
    link = deckDict[index]
    link.click()
    cardSelViewFlop2.click()
    index = secondFlop['SUIT']
    link = deckDict[index]
    link.click()
    index = secondFlop['CARD']
    link = deckDict[index]
    link.click()
    cardSelViewFlop3.click()
    index = thirdFlop['SUIT']
    link = deckDict[index]
    link.click()
    index = thirdFlop['CARD']
    link = deckDict[index]
    link.click()
    done.click()

def clickTurn():
    turnClick.click()
    cardSelViewTurn.click()
    index = turnCard['SUIT']
    link = deckDict[index]
    link.click()
    index = turnCard['CARD']
    link = deckDict[index]
    link.click()
    done.click()

def clickRiver():
    riverClick.click()
    cardSelViewRiver.click()
    index = riverCard['SUIT']
    link = deckDict[index]
    link.click()
    index = riverCard['CARD']
    link = deckDict[index]
    link.click()
    done.click()

monitorList = []
for m in get_monitors():
	monitorList.append(m)

print('\nONLY WORKS WITH 1920x1080 DISPLAYS\n\nWorks best if you have the poker room\n'
      'already open before starting this program\n\nPress CTRL + C to quit\n')
if len(monitorList) > 1:
    sameScreenOption = pyip.inputYesNo(prompt='Display the calculator on the same screen as the poker table? Y/N: ')
sizeOfTable = pyip.inputMenu(['2', '6', '9'], '\nEnter how many seats at table:\n')
if sizeOfTable == '2':
    mySeat = pyip.inputMenu(['1', '2'], 'Please select own seat number, 1 = top, 2 = bottom\n')
elif sizeOfTable == '6':
    mySeat = pyip.inputMenu(['1', '2', '3', '4', '5', '6'], 'Please select own seat number 1-6 clockwise\n')
elif sizeOfTable == '9':
    mySeat = pyip.inputMenu(['1', '2', '3', '4', '5', '6', '7', '8', '9'], 'Please select own seat number 1-9 clockwise\n')


options = Options()
options.add_argument('--kiosk')
binary = FirefoxBinary(str(Path(r'C:/Program Files/Mozilla Firefox/firefox.exe')))
driver = webdriver.Firefox(options=options, firefox_binary = binary, executable_path = str(Path('.\geckodriver.exe')))
driver2 = webdriver.Firefox(options=options, firefox_binary = binary, executable_path = str(Path('.\geckodriver.exe')))
driver.set_window_size(466, 500)
driver2.set_window_size(466, 550)
if len(monitorList) == 1 or sameScreenOption == 'yes':
    if gw.getWindowsWithTitle('Hold\'em') != []:
        pokerRoom = gw.getWindowsWithTitle('Hold\'em')[0]
        pokerRoom.resizeTo(1480, 1048)
        pokerRoom.moveTo(-9, 0)
        pyautogui.keyDown('altleft')
        pokerRoom.activate()
        pyautogui.keyUp('altleft')
    driver.set_window_position(1457,0)
    driver2.set_window_position(1457,494)
    screenKey = '1'
elif len(monitorList) > 1 and sameScreenOption == 'no':
    driver.set_window_position(1914,0)
    driver2.set_window_position(1914,494)
    screenKey = '2'
    if gw.getWindowsWithTitle('Hold\'em') != []:
        pokerRoom = gw.getWindowsWithTitle('Hold\'em')[0]
        pokerRoom.maximize()
        pyautogui.keyDown('altleft')
        pokerRoom.activate()
        pyautogui.keyUp('altleft')

driver.get('https://www.888poker.com/poker/poker-odds-calculator')
driver2.get('https://betandbeat.com/poker/rules/hands/')

deckDict = {'CLUB': driver.find_element_by_xpath('//*[@id="suit-selection-container"]/div/a[1]'),
            'twoCLUB': driver.find_element_by_xpath('//*[@id="card-selection-table"]/div[1]/div[1]/a[1]'),
            'threeCLUB' : driver.find_element_by_xpath('//*[@id="card-selection-table"]/div[1]/div[1]/a[2]'),
            'fourCLUB' : driver.find_element_by_xpath('//*[@id="card-selection-table"]/div[1]/div[1]/a[3]'),
            'fiveCLUB' : driver.find_element_by_xpath('//*[@id="card-selection-table"]/div[1]/div[1]/a[4]'),
            'sixCLUB' : driver.find_element_by_xpath('//*[@id="card-selection-table"]/div[1]/div[1]/a[5]'),
            'sevenCLUB' : driver.find_element_by_xpath('//*[@id="card-selection-table"]/div[1]/div[1]/a[6]'),
            'eightCLUB' : driver.find_element_by_xpath('//*[@id="card-selection-table"]/div[1]/div[1]/a[7]'),
            'nineCLUB' : driver.find_element_by_xpath('//*[@id="card-selection-table"]/div[1]/div[1]/a[8]'),
            'tenCLUB' : driver.find_element_by_xpath('//*[@id="card-selection-table"]/div[1]/div[1]/a[9]'),
            'jackCLUB' : driver.find_element_by_xpath('//*[@id="card-selection-table"]/div[1]/div[1]/a[10]'),
            'queenCLUB' : driver.find_element_by_xpath('//*[@id="card-selection-table"]/div[1]/div[1]/a[11]'),
            'kingCLUB' : driver.find_element_by_xpath('//*[@id="card-selection-table"]/div[1]/div[1]/a[12]'),
            'aceCLUB' : driver.find_element_by_xpath('//*[@id="card-selection-table"]/div[1]/div[1]/a[13]'),
            'SPADE' : driver.find_element_by_xpath('//*[@id="suit-selection-container"]/div/a[3]'),
            'twoSPADE' : driver.find_element_by_xpath('//*[@id="card-selection-table"]/div[1]/div[3]/a[1]'),
            'threeSPADE' : driver.find_element_by_xpath('//*[@id="card-selection-table"]/div[1]/div[3]/a[2]'),
            'fourSPADE' : driver.find_element_by_xpath('//*[@id="card-selection-table"]/div[1]/div[3]/a[3]'),
            'fiveSPADE' : driver.find_element_by_xpath('//*[@id="card-selection-table"]/div[1]/div[3]/a[4]'),
            'sixSPADE' : driver.find_element_by_xpath('//*[@id="card-selection-table"]/div[1]/div[3]/a[5]'),
            'sevenSPADE' : driver.find_element_by_xpath('//*[@id="card-selection-table"]/div[1]/div[3]/a[6]'),
            'eightSPADE' : driver.find_element_by_xpath('//*[@id="card-selection-table"]/div[1]/div[3]/a[7]'),
            'nineSPADE' : driver.find_element_by_xpath('//*[@id="card-selection-table"]/div[1]/div[3]/a[8]'),
            'tenSPADE' : driver.find_element_by_xpath('//*[@id="card-selection-table"]/div[1]/div[3]/a[9]'),
            'jackSPADE' : driver.find_element_by_xpath('//*[@id="card-selection-table"]/div[1]/div[3]/a[10]'),
            'queenSPADE' : driver.find_element_by_xpath('//*[@id="card-selection-table"]/div[1]/div[3]/a[11]'),
            'kingSPADE' : driver.find_element_by_xpath('//*[@id="card-selection-table"]/div[1]/div[3]/a[12]'),
            'aceSPADE' : driver.find_element_by_xpath('//*[@id="card-selection-table"]/div[1]/div[3]/a[13]'),
            'DIAMOND' : driver.find_element_by_xpath('//*[@id="suit-selection-container"]/div/a[2]'),
            'twoDIAMOND' : driver.find_element_by_xpath('//*[@id="card-selection-table"]/div[1]/div[2]/a[1]'),
            'threeDIAMOND' : driver.find_element_by_xpath('//*[@id="card-selection-table"]/div[1]/div[2]/a[2]'),
            'fourDIAMOND' : driver.find_element_by_xpath('//*[@id="card-selection-table"]/div[1]/div[2]/a[3]'),
            'fiveDIAMOND' : driver.find_element_by_xpath('//*[@id="card-selection-table"]/div[1]/div[2]/a[4]'),
            'sixDIAMOND' : driver.find_element_by_xpath('//*[@id="card-selection-table"]/div[1]/div[2]/a[5]'),
            'sevenDIAMOND' : driver.find_element_by_xpath('//*[@id="card-selection-table"]/div[1]/div[2]/a[6]'),
            'eightDIAMOND' : driver.find_element_by_xpath('//*[@id="card-selection-table"]/div[1]/div[2]/a[7]'),
            'nineDIAMOND' : driver.find_element_by_xpath('//*[@id="card-selection-table"]/div[1]/div[2]/a[8]'),
            'tenDIAMOND' : driver.find_element_by_xpath('//*[@id="card-selection-table"]/div[1]/div[2]/a[9]'),
            'jackDIAMOND' : driver.find_element_by_xpath('//*[@id="card-selection-table"]/div[1]/div[2]/a[10]'),
            'queenDIAMOND' : driver.find_element_by_xpath('//*[@id="card-selection-table"]/div[1]/div[2]/a[11]'),
            'kingDIAMOND' : driver.find_element_by_xpath('//*[@id="card-selection-table"]/div[1]/div[2]/a[12]'),
            'aceDIAMOND' : driver.find_element_by_xpath('//*[@id="card-selection-table"]/div[1]/div[2]/a[13]'),
            'HEART' : driver.find_element_by_xpath('//*[@id="suit-selection-container"]/div/a[4]'),
            'twoHEART' : driver.find_element_by_xpath('//*[@id="card-selection-table"]/div[1]/div[4]/a[1]'),
            'threeHEART' : driver.find_element_by_xpath('//*[@id="card-selection-table"]/div[1]/div[4]/a[2]'),
            'fourHEART' : driver.find_element_by_xpath('//*[@id="card-selection-table"]/div[1]/div[4]/a[3]'),
            'fiveHEART' : driver.find_element_by_xpath('//*[@id="card-selection-table"]/div[1]/div[4]/a[4]'),
            'sixHEART' : driver.find_element_by_xpath('//*[@id="card-selection-table"]/div[1]/div[4]/a[5]'),
            'sevenHEART' : driver.find_element_by_xpath('//*[@id="card-selection-table"]/div[1]/div[4]/a[6]'),
            'eightHEART' : driver.find_element_by_xpath('//*[@id="card-selection-table"]/div[1]/div[4]/a[7]'),
            'nineHEART' : driver.find_element_by_xpath('//*[@id="card-selection-table"]/div[1]/div[4]/a[8]'),
            'tenHEART' : driver.find_element_by_xpath('//*[@id="card-selection-table"]/div[1]/div[4]/a[9]'),
            'jackHEART' : driver.find_element_by_xpath('//*[@id="card-selection-table"]/div[1]/div[4]/a[10]'),
            'queenHEART' : driver.find_element_by_xpath('//*[@id="card-selection-table"]/div[1]/div[4]/a[11]'),
            'kingHEART' : driver.find_element_by_xpath('//*[@id="card-selection-table"]/div[1]/div[4]/a[12]'),
            'aceHEART' : driver.find_element_by_xpath('//*[@id="card-selection-table"]/div[1]/div[4]/a[13]')}

MainDict = {'2myHandPositions9': {'1a': (1104,41,40,80), '1b': (1200,40,40,80),
                                    '2a': (1377,141,40,80), '2b': (1474,140,40,80),
                                    '3a': (1441,342,40,80), '3b': (1535,340,40,80),
                                    '4a': (1292,545,40,80), '4b': (1389,549,40,80),
                                    '5a': (864,640,40,80), '5b': (962,640,40,80),
                                    '6a': (436,548,40,80), '6b': (534,548,40,80),
                                    '7a': (297,342,40,80), '7b': (388,339,40,80),
                                    '8a': (351,137,40,80), '8b': (447,140,40,80),
                                    '9a': (627,43,40,80), '9b': (722,41,40,80)},
            '2myHandPositions6': {'1a': (870,43,40,80), '1b': (964,43,40,80),
                                    '2a': (1378,138,40,80), '2b': (1476,139,40,80),
                                    '3a': (1426,458,40,80), '3b': (1521,455,40,80),
                                    '4a': (866,642,40,80), '4b': (963,645,40,80),
                                    '5a': (306,456,40,80), '5b': (404,457,40,80),
                                    '6a': (353,138,40,80), '6b': (448,138,40,80)},
            '2myHandPositions2': {'1a': (870,43,40,80), '1b': (964,43,40,80),
                                    '2a': (866,642,40,80), '2b': (963,645,40,80)},
            '2dealerHandPositions': {'flop1':(713,354,40,80),
                                    'flop2':(815,355,40,80),
                                    'flop3':(914,355,40,80),
                                    'turnCard':(1015,353,40,80),
                                    'riverCard':(1116,353,40,80)},
            '2seatPositions9': {'1': (1215,84,80,35), 
                                '2': (1483,184,80,35),
                                '3': (1545,384,80,35),
                                '4': (1397,593,80,35),
                                '5': (874,683,80,35),
                                '6': (446,593,80,35),
                                '7': (302,383,80,35),
                                '8': (361,179,80,35),
                                '9': (633,83,80,35)},
            '2seatPositions6': {'1': (870,79,80,35),
                                '2': (1480,179,80,35),
                                '3': (1526,496,80,35),
                                '4': (968,681,80,35),
                                '5': (314,496,80,35),
                                '6': (361,182,80,35)},
            '2seatPositions2': {'1': (870,79,80,35), 
                                '2': (967,683,80,35)},
            '1myHandPositions9': {'1a': (877,46,35,77), '1b': (974,46,35,77),
                                    '2a': (1147,144,35,77), '2b': (1242,144,35,77),
                                    '3a': (1207,346,35,77), '3b': (1302,345,35,77),
                                    '4a': (1065,551,35,77), '4b': (1157,553,35,77),
                                    '5a': (638,645,35,77), '5b': (736,645,35,77),
                                    '6a': (213,550,35,77), '6b': (308,553,35,77),
                                    '7a': (70,344,35,77), '7b': (163,344,35,77),
                                    '8a': (130,146,35,77), '8b': (224,144,35,77),
                                    '9a': (398,47,35,77), '9b': (491,47,35,77)},
            '1myHandPositions6': {'1a': (638,46,35,77), '1b': (734,45,35,77),
                                    '2a': (1148,145,35,77), '2b': (1240,143,35,77),
                                    '3a': (1194,458,35,77), '3b': (1289,459,35,77),
                                    '4a': (638,643,35,77), '4b': (734,645,35,77),
                                    '5a': (84,459,35,77), '5b': (179,456,35,77),
                                    '6a': (130,144,35,77), '6b': (225,143,35,77)},
            '1myHandPositions2': {'1a': (638,46,35,77), '1b': (734,45,35,77),
                                    '4a': (638,643,35,77), '4b': (734,645,35,77)},
            '1dealerHandPositions': {'flop1':(484,358,35,77),
                                    'flop2':(585,360,35,77),
                                    'flop3':(685,360,35,77),
                                    'turnCard':(784,358,35,77),
                                    'riverCard':(885,358,35,77)},
            '1seatPositions9': {'1': (980,92,80,35),    
                                '2': (1247,185,80,35),
                                '3': (1308,385,80,35),
                                '4': (1162,591,80,35),
                                '5': (643,684,80,35),   
                                '6': (219,591,80,35),
                                '7': (75,384,80,35),
                                '8': (137,187,80,35),
                                '9': (403,87,80,35)},
            '1seatPositions6': {'1': (645,88,80,35),
                                '2': (1247,186,80,35),
                                '3': (1294,500,80,35),
                                '4': (739,684,80,35),
                                '5': (89,500,80,35),
                                '6': (135,186,80,35)},
            '1seatPositions2': {'1': (643,86,80,35), 
                                '2': (738,684,80,35)}}


reset = driver.find_element_by_xpath('//*[@id="reset-poker-table-mobile"]')
resetConfirm = driver.find_element_by_xpath('//*[@id="reset-confirm-btn"]')
done = driver.find_element_by_xpath('//*[@id="card-selection-complete"]/span')
myCalcCard1 = driver.find_element_by_xpath('//*[@id="player-listing"]/div[1]/div[3]/div[1]/div[1]/div/div/div[2]')
myCalcCard2 = driver.find_element_by_xpath('//*[@id="player-listing"]/div[1]/div[3]/div[1]/div[2]/div/div/div[2]')
cardSelViewMyCard1 = driver.find_element_by_xpath('//*[@id="card-selection-view"]/div[1]/div/div[1]/div/div/div[2]')
cardSelViewMyCard2 = driver.find_element_by_xpath('//*[@id="card-selection-view"]/div[1]/div/div[2]/div/div/div[2]')
cardSelViewFlop1 = driver.find_element_by_xpath('//*[@id="card-selection-view"]/div[1]/div/div[1]/div/div/div[2]')
cardSelViewFlop2 = driver.find_element_by_xpath('//*[@id="card-selection-view"]/div[1]/div/div[2]/div/div/div[2]')
cardSelViewFlop3 = driver.find_element_by_xpath('//*[@id="card-selection-view"]/div[1]/div/div[3]/div/div/div[2]')
cardSelViewTurn = driver.find_element_by_xpath('//*[@id="card-selection-view"]/div[1]/div/div[4]/div/div/div[2]')
cardSelViewRiver = driver.find_element_by_xpath('//*[@id="card-selection-view"]/div[1]/div/div[5]/div/div/div[2]')
flop1Click = driver.find_element_by_xpath('//*[@id="poker-table"]/ul/li[1]/div/div/div[2]')
flop2Click = driver.find_element_by_xpath('//*[@id="poker-table"]/ul/li[2]/div/div/div[2]')
flop3Click = driver.find_element_by_xpath('//*[@id="poker-table"]/ul/li[3]/div/div/div[2]')
turnClick = driver.find_element_by_xpath('//*[@id="poker-table"]/ul/li[4]/div/div/div[2]')
riverClick = driver.find_element_by_xpath('//*[@id="poker-table"]/ul/li[5]/div/div/div[2]')
removePlayersLink = driver.find_element_by_xpath('//*[@id="remove-players-link"]')
closeremovePlayersLink = driver.find_element_by_xpath('//*[@id="remove-players-link"]')
removePlayer = driver.find_element_by_xpath('//*[@id="player-listing"]/div[2]/div[1]')
addPlayer = driver.find_element_by_xpath('//*[@id="add-player-link"]/span')
tableView = driver.find_element_by_xpath('//*[@id="poker-table"]')
playerTables = driver.find_elements_by_class_name('player--single.card-selection-block')
pokerHands = driver2.find_element_by_xpath('//*[@id="silo-20"]/div[1]/div[5]/div/figure/img')

try:
    popupClose = driver.find_element_by_xpath('/html/body/div[2]/div/img[2]')
    popupClose.click()
except NoSuchElementException:
    pass
driver2.execute_script("arguments[0].scrollIntoView(true);", pokerHands)

firstFlop = None
secondFlop = None
thirdFlop = None
turnCard = None
riverCard = None
myCard1 = None
myCard2 = None
count = 0
lastPlayers = 9
myCardsClicked = 'no'
flopClicked = 'no'
turnClicked = 'no'
riverClicked = 'no'
if sizeOfTable == '2':
    myHandPositions = screenKey+'myHandPositions2'
    playerSeats = MainDict[screenKey+'seatPositions2']  
elif sizeOfTable == '6':
    myHandPositions = screenKey+'myHandPositions6'
    playerSeats = MainDict[screenKey+'seatPositions6']
elif sizeOfTable == '9':
    myHandPositions = screenKey+'myHandPositions9'
    playerSeats = MainDict[screenKey+'seatPositions9']   
if mySeat in playerSeats:
    del playerSeats[mySeat]
  
myHand1 = mySeat+'a'
myHand2 = mySeat+'b'

dealerHandPositions = screenKey+'dealerHandPositions'

try:
    while True: #main loop
        players = activePlayers()
        logging.info('Number other players: '+str(players))
        logging.info('Last loop\'s players '+str(lastPlayers))
        if players != 0 and lastPlayers != 0 and lastPlayers < players:
            players = 0
        if players != lastPlayers and players != 0:
            playerAddRemove()
        if players == 0:
            logging.info('\n********RESET*********\n')
            myCard1 = None
            myCard2 = None
            firstFlop = None
            secondFlop = None
            thirdFlop = None
            turnCard = None
            riverCard = None
            myCardsClicked = 'no'
            flopClicked = 'no'
            turnClicked = 'no'
            riverClicked = 'no'
            StartNewRound()
            players = int(sizeOfTable)-1
            playerAddRemove()
        lastPlayers = players

        
        if myCard1 is None:
            myCard1 = findCard(MainDict[myHandPositions], myHand1)
            logging.info('My 1st card is '+str(myCard1))
        if myCard2 is None:
            myCard2 = findCard(MainDict[myHandPositions], myHand2)
            logging.info('My 2nd card is '+str(myCard2))
        elif myCard1 is None and myCard2 is not None:
            myCard1 = findCard(MainDict[myHandPositions], myHand1)
            logging.info('2nd Pass: My 1st card is '+str(myCard1))
        if myCardsClicked == 'no':
            if myCard1 is not None and myCard2 is not None:
                clickMyCards()
                myCardsClicked = 'yes'
                driver.execute_script("arguments[0].scrollIntoView(true);", tableView)
        logging.info('myCardsClicked = '+myCardsClicked)
        if firstFlop is None:
            firstFlop = findCard(MainDict[dealerHandPositions], 'flop1')
            logging.info('1st Flop is '+str(firstFlop))
        if secondFlop is None:
            secondFlop = findCard(MainDict[dealerHandPositions], 'flop2')
            logging.info('2nd Flop is '+str(secondFlop))
        if thirdFlop is None:
            thirdFlop = findCard(MainDict[dealerHandPositions], 'flop3')
            logging.info('3rd Flop is '+str(thirdFlop))
        if turnCard is None:
            turnCard = findCard(MainDict[dealerHandPositions], 'turnCard')
            logging.info('Turn Card is '+str(turnCard))
        if riverCard is None:
            riverCard = findCard(MainDict[dealerHandPositions], 'riverCard')
            logging.info('River Card is '+str(riverCard))
        if firstFlop is None and secondFlop is not None:
            firstFlop = findCard(MainDict[dealerHandPositions], 'flop1')
            logging.info('2nd Pass: 1st Flop is '+str(firstFlop))
        if secondFlop is None and thirdFlop is not None:
            secondFlop = findCard(MainDict[dealerHandPositions], 'flop2')
            logging.info('2nd Pass: 2nd Flop is '+str(secondFlop))
        if thirdFlop is None and turnCard is not None:
            thirdFlop = findCard(MainDict[dealerHandPositions], 'flop3')
            logging.info('2nd Pass: 3rd Flop is '+str(thirdFlop))
        if turnCard is None and riverCard is not None:
            turnCard = findCard(MainDict[dealerHandPositions], 'turnCard')
            logging.info('2nd Pass: turnCard is '+str(turnCard))
        if flopClicked == 'no':
            if firstFlop is not None and secondFlop is not None and thirdFlop is not None:
                clickAllFlopCards()
                flopClicked = 'yes'
                driver.execute_script("arguments[0].scrollIntoView(true);", tableView)
        logging.info('flopClicked = '+flopClicked)
        if turnClicked == 'no':
            if turnCard is not None:
                clickTurn()
                turnClicked = 'yes'
                driver.execute_script("arguments[0].scrollIntoView(true);", tableView)
        logging.info('turnClicked = '+turnClicked)
        if riverClicked == 'no':
            if riverCard is not None:
                clickRiver()
                riverClicked = 'yes'
                driver.execute_script("arguments[0].scrollIntoView(true);", tableView)
        logging.info('riverClicked = '+riverClicked)

except KeyboardInterrupt:
    print('Closing geckodriver and firefox...')
    driver.quit()
    driver2.quit()
    subprocess.call(["taskkill","/F","/IM","firefox.exe"])
    print('Done, now exiting...')
    logging.info('End of program')
    time.sleep(2)
    sys.exit()


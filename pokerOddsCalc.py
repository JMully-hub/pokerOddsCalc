#! python3
# pokerOdds.py - Simple screen recognition software to input current screen data to a ready-made poker
# hands online calculator

import pyinputplus as pyip
import sys, time, pyautogui, subprocess, shutil, os, threading, logging
from pathlib import Path
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

logging.disable(logging.CRITICAL)
logging.basicConfig(level=logging.INFO, format='%(asctime)s -  %(levelname)s-  %(message)s')
logging.info('Start of program')

def activePlayers():
    if sizeOfTable == '2':
        playerSeats = seatPositions2
    elif sizeOfTable == '6':
        playerSeats = seatPositions6
    elif sizeOfTable == '9':
        playerSeats = seatPositions9
    if mySeat in playerSeats:
        del playerSeats[mySeat]
    otherPlayers = 0
    for location in playerSeats:
        if pyautogui.locateOnScreen(str(Path('./images/cardBack.png')),
                                    region=(playerSeats[location]), confidence=0.99) is not None:
            otherPlayers = otherPlayers + 1
    logging.info('Number other players: '+str(otherPlayers))
    return otherPlayers

def myFirstCard():
    if sizeOfTable == '2':
        myHandPositions = myHandPositions2
    elif sizeOfTable == '6':
        myHandPositions = myHandPositions6
    elif sizeOfTable == '9':
        myHandPositions = myHandPositions9
    myHand1 = mySeat+ 'a'
    deckList =  os.listdir(r'.\images\suits')
    for suitA in deckList:
        if pyautogui.locateOnScreen(('.\\images\\suits\\'+suitA),
                                    region=myHandPositions[myHand1], confidence=0.99) is not None:
            mySuit1 = str(os.path.basename(suitA)).replace('.png', '')
            if mySuit1 == 'HEART' or mySuit1 == 'DIAMOND':
                valueList = os.listdir(r'.\images\redValues')
                for valueA in valueList:
                    if pyautogui.locateOnScreen(('.\\images\\redValues\\'+valueA),
                                                region=myHandPositions[myHand1], confidence=0.99) is not None:
                        myValue1 = str(os.path.basename(valueA)).replace('.png', '')
                        myCard1 = str(myValue1+mySuit1)
                        logging.info('My 1st card is '+str(myCard1))
                        returnDic = {}
                        returnDic.setdefault('SUIT', mySuit1)
                        returnDic.setdefault('CARD', myCard1)
                        return returnDic
            elif mySuit1 == 'CLUB' or mySuit1 == 'SPADE':
                valueList = os.listdir(r'.\images\blackValues')
                for valueA in valueList:
                    if pyautogui.locateOnScreen(('.\\images\\blackValues\\'+valueA),
                                                region=myHandPositions[myHand1], confidence=0.99) is not None:
                        myValue1 = str(os.path.basename(valueA)).replace('.png', '')
                        myCard1 = str(myValue1+mySuit1)
                        logging.info('My 1st card is '+str(myCard1))
                        returnDic = {}
                        returnDic.setdefault('SUIT', mySuit1)
                        returnDic.setdefault('CARD', myCard1)
                        return returnDic

        

def mySecondCard():
    if sizeOfTable == '2':
        myHandPositions = myHandPositions2
    elif sizeOfTable == '6':
        myHandPositions = myHandPositions6
    elif sizeOfTable == '9':
        myHandPositions = myHandPositions9
    myHand2 = mySeat+ 'b'
    deckList =  os.listdir(r'.\images\suits')                    
    for suitB in deckList:
        if pyautogui.locateOnScreen(('.\\images\\suits\\'+suitB),
                                    region=myHandPositions[myHand2], confidence=0.99) is not None:
            mySuit2 = str(os.path.basename(suitB)).replace('.png', '')
            if mySuit2 == 'HEART' or mySuit2 == 'DIAMOND':
                valueList = os.listdir(r'.\images\redValues')
                for valueB in valueList:
                    if pyautogui.locateOnScreen(('.\\images\\redValues\\'+valueB),
                                                region=myHandPositions[myHand2], confidence=0.99) is not None:
                        myValue2 = str(os.path.basename(valueB)).replace('.png', '')
                        myCard2 = str(myValue2+mySuit2)
                        logging.info('My 2nd card is '+str(myCard2))
                        returnDic = {}
                        returnDic.setdefault('SUIT', mySuit2)
                        returnDic.setdefault('CARD', myCard2)
                        return returnDic
            elif mySuit2 == 'CLUB' or mySuit2 == 'SPADE':
                valueList = os.listdir(r'.\images\blackValues')
                for valueB in valueList:
                    if pyautogui.locateOnScreen(('.\\images\\blackValues\\'+valueB),
                                                region=myHandPositions[myHand2], confidence=0.99) is not None:
                        myValue2 = str(os.path.basename(valueB)).replace('.png', '')
                        myCard2 = str(myValue2+mySuit2)
                        logging.info('My 2nd card is '+str(myCard2))
                        returnDic = {}
                        returnDic.setdefault('SUIT', mySuit2)
                        returnDic.setdefault('CARD', myCard2)
                        return returnDic

def firstFlopF():
    deckList =  os.listdir(r'.\images\suits')
    for flopA in deckList:
        if pyautogui.locateOnScreen(('.\\images\\suits\\'+flopA),
                                    region=dealerHandPositions['flop1'], confidence=0.99) is not None:
            flop1Suit= str(os.path.basename(flopA)).replace('.png', '')           
            if flop1Suit == 'HEART' or flop1Suit == 'DIAMOND':
                valueList = os.listdir(r'.\images\redValues')
                for valueA in valueList:
                    if pyautogui.locateOnScreen(('.\\images\\redValues\\'+valueA),
                                                region=dealerHandPositions['flop1'], confidence=0.99) is not None:
                        flop1Value = str(os.path.basename(valueA)).replace('.png', '')
                        flop1Card = str(flop1Value+flop1Suit)
                        logging.info('1st Flop is '+str(flop1Card))
                        returnDic = {}
                        returnDic.setdefault('SUIT', flop1Suit)
                        returnDic.setdefault('CARD', flop1Card)
                        return returnDic
            elif flop1Suit == 'CLUB' or flop1Suit == 'SPADE':
                valueList = os.listdir(r'.\images\blackValues')
                for valueA in valueList:
                    if pyautogui.locateOnScreen(('.\\images\\blackValues\\'+valueA),
                                                region=dealerHandPositions['flop1'], confidence=0.99) is not None:
                        flop1Value = str(os.path.basename(valueA)).replace('.png', '')
                        flop1Card = str(flop1Value+flop1Suit)
                        logging.info('1st Flop is '+str(flop1Card))
                        returnDic = {}
                        returnDic.setdefault('SUIT', flop1Suit)
                        returnDic.setdefault('CARD', flop1Card)
                        return returnDic


def secondFlopF():
    deckList =  os.listdir(r'.\images\suits')              
    for flopB in deckList:
        if pyautogui.locateOnScreen(('.\\images\\suits\\'+flopB),
                                    region=dealerHandPositions['flop2'], confidence=0.99) is not None:
            flop2Suit= str(os.path.basename(flopB)).replace('.png', '')
            if flop2Suit == 'HEART' or flop2Suit == 'DIAMOND':
                valueList = os.listdir(r'.\images\redValues')
                for valueB in valueList:
                    if pyautogui.locateOnScreen(('.\\images\\redValues\\'+valueB),
                                                region=dealerHandPositions['flop2'], confidence=0.99) is not None:
                        flop2Value = str(os.path.basename(valueB)).replace('.png', '')
                        flop2Card = str(flop2Value+flop2Suit)
                        logging.info('2nd Flop is '+str(flop2Card))
                        returnDic = {}
                        returnDic.setdefault('SUIT', flop2Suit)
                        returnDic.setdefault('CARD', flop2Card)
                        return returnDic
            elif flop2Suit == 'CLUB' or flop2Suit == 'SPADE':
                valueList = os.listdir(r'.\images\blackValues')
                for valueB in valueList:
                    if pyautogui.locateOnScreen(('.\\images\\blackValues\\'+valueB),
                                                region=dealerHandPositions['flop2'], confidence=0.99) is not None:
                        flop2Value = str(os.path.basename(valueB)).replace('.png', '')
                        flop2Card = str(flop2Value+flop2Suit)
                        logging.info('2nd Flop is '+str(flop2Card))
                        returnDic = {}
                        returnDic.setdefault('SUIT', flop2Suit)
                        returnDic.setdefault('CARD', flop2Card)
                        return returnDic
                            
def thirdFlopF():
    deckList =  os.listdir(r'.\images\suits')                               
    for flopC in deckList: 
        if pyautogui.locateOnScreen(('.\\images\\suits\\'+flopC),
                                    region=dealerHandPositions['flop3'], confidence=0.99) is not None:
            flop3Suit= str(os.path.basename(flopC)).replace('.png', '')
            if flop3Suit == 'HEART' or flop3Suit == 'DIAMOND':
                valueList = os.listdir(r'.\images\redValues')
                for valueC in valueList:
                    if pyautogui.locateOnScreen(('.\\images\\redValues\\'+valueC),
                                                region=dealerHandPositions['flop3'], confidence=0.99) is not None:
                        flop3Value = str(os.path.basename(valueC)).replace('.png', '')
                        flop3Card = str(flop3Value+flop3Suit)
                        logging.info('3rd Flop is '+str(flop3Card))
                        returnDic = {}
                        returnDic.setdefault('SUIT', flop3Suit)
                        returnDic.setdefault('CARD', flop3Card)
                        return returnDic
            elif flop3Suit == 'CLUB' or flop3Suit == 'SPADE':
                valueList = os.listdir(r'.\images\blackValues')
                for valueC in valueList:
                    if pyautogui.locateOnScreen(('.\\images\\blackValues\\'+valueC),
                                                region=dealerHandPositions['flop3'], confidence=0.99) is not None:
                        flop3Value = str(os.path.basename(valueC)).replace('.png', '')
                        flop3Card = str(flop3Value+flop3Suit)
                        logging.info('3rd Flop is '+str(flop3Card))
                        returnDic = {}
                        returnDic.setdefault('SUIT', flop3Suit)
                        returnDic.setdefault('CARD', flop3Card)
                        return returnDic

def turnCardF():
    deckList =  os.listdir(r'.\images\suits')                                
    for turnA in deckList: 
        if pyautogui.locateOnScreen(('.\\images\\suits\\'+turnA),
                                    region=dealerHandPositions['turnCard'], confidence=0.99) is not None:
            turnSuit = str(os.path.basename(turnA)).replace('.png', '')
            if turnSuit == 'HEART' or turnSuit == 'DIAMOND':
                valueList = os.listdir(r'.\images\redValues')
                for turn in valueList:
                    if pyautogui.locateOnScreen(('.\\images\\redValues\\'+turn),
                                                region=dealerHandPositions['turnCard'], confidence=0.99) is not None:
                        turnValue = str(os.path.basename(turn)).replace('.png', '')
                        turnCard = str(turnValue+turnSuit)
                        logging.info('Turn card is '+str(turnCard))
                        returnDic = {}
                        returnDic.setdefault('SUIT', turnSuit)
                        returnDic.setdefault('CARD', turnCard)
                        return returnDic
            elif turnSuit == 'CLUB' or turnSuit == 'SPADE':
                valueList = os.listdir(r'.\images\blackValues')
                for turn in valueList:
                    if pyautogui.locateOnScreen(('.\\images\\blackValues\\'+turn),
                                                region=dealerHandPositions['turnCard'], confidence=0.99) is not None:
                        turnValue = str(os.path.basename(turn)).replace('.png', '')
                        turnCard = str(turnValue+turnSuit)
                        logging.info('Turn card is '+str(turnCard))
                        returnDic = {}
                        returnDic.setdefault('SUIT', turnSuit)
                        returnDic.setdefault('CARD', turnCard)
                        return returnDic
                        
def riverCardF():
    deckList =  os.listdir(r'.\images\suits')                               
    for river1 in deckList: 
        if pyautogui.locateOnScreen(('.\\images\\suits\\'+river1),
                                    region=dealerHandPositions['riverCard'], confidence=0.99) is not None:
            riverSuit = str(os.path.basename(river1)).replace('.png', '')
            if riverSuit == 'HEART' or riverSuit == 'DIAMOND':
                valueList = os.listdir(r'.\images\redValues')
                for river in valueList:
                    if pyautogui.locateOnScreen(('.\\images\\redValues\\'+river),
                                                region=dealerHandPositions['riverCard'], confidence=0.99) is not None:
                        riverValue = str(os.path.basename(river)).replace('.png', '')
                        riverCard = str(riverValue+riverSuit)
                        logging.info('River card is '+str(riverCard))
                        returnDic = {}
                        returnDic.setdefault('SUIT', riverSuit)
                        returnDic.setdefault('CARD', riverCard)
                        return returnDic
            elif riverSuit == 'CLUB' or riverSuit == 'SPADE':
                valueList = os.listdir(r'.\images\blackValues')
                for river in valueList:
                    if pyautogui.locateOnScreen(('.\\images\\blackValues\\'+river),
                                                region=dealerHandPositions['riverCard'], confidence=0.99) is not None:
                        riverValue = str(os.path.basename(river)).replace('.png', '')
                        riverCard = str(riverValue+riverSuit)
                        logging.info('River card is '+str(riverCard))
                        returnDic = {}
                        returnDic.setdefault('SUIT', riverSuit)
                        returnDic.setdefault('CARD', riverCard)
                        return returnDic
                        
def StartNewRound():
    reset.click()
    resetConfirm.click()

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
    
    


print('Press CTRL + C to quit')
sizeOfTable = pyip.inputMenu(['2', '6', '9'], 'Enter how many seats at table:\n')
if sizeOfTable == '2':
    mySeat = pyip.inputMenu(['1', '2'], 'Please select own seat number, 1 = top, 2 = bottom\n')
elif sizeOfTable == '6':
    mySeat = pyip.inputMenu(['1', '2', '3', '4', '5', '6'], 'Please select own seat number 1-6 clockwise\n')
elif sizeOfTable == '9':
    mySeat = pyip.inputMenu(['1', '2', '3', '4', '5', '6', '7', '8', '9'], 'Please select own seat number 1-9 clockwise\n')


myHandPositions9 = {'1a': (1104,41,40,80), '1b': (1200,40,40,80),
                   '2a': (1377,141,40,80), '2b': (1474,140,40,80),
                   '3a': (1441,342,40,80), '3b': (1535,340,40,80),
                   '4a': (1292,545,40,80), '4b': (1389,549,40,80),
                   '5a': (864,640,40,80), '5b': (962,640,40,80),
                   '6a': (436,548,40,80), '6b': (534,548,40,80),
                   '7a': (534,548,40,80), '7b': (388,339,40,80),
                   '8a': (351,137,40,80), '8b': (447,140,40,80),
                   '9a': (627,43,40,80), '9b': (722,41,40,80)}

myHandPositions6 = {'1a': (870,43,40,80), '1b': (964,43,40,80),
                   '2a': (1378,138,40,80), '2b': (1476,139,40,80),
                   '3a': (1426,458,40,80), '3b': (1521,455,40,80),
                   '4a': (866,642,40,80), '4b': (963,645,40,80),
                   '5a': (306,456,40,80), '5b': (404,457,40,80),
                   '6a': (353,138,40,80), '6b': (448,138,40,80)}

myHandPositions2 = {'1a': (870,43,40,80), '1b': (964,43,40,80),
                   '2a': (866,642,40,80), '2b': (963,645,40,80)}

dealerHandPositions = {'flop1':(713,354,40,80),
                       'flop2':(815,355,40,80),
                       'flop3':(914,355,40,80),
                       'turnCard':(1015,353,40,80),
                       'riverCard':(1116,353,40,80)}

seatPositions9 = {'1': (1215,84,80,35), 
                  '2': (1483,184,80,35),
                  '3': (1545,384,80,35),
                  '4': (1397,593,80,35),
                  '5': (874,683,80,35),
                  '6': (446,593,80,35),
                  '7': (302,383,80,35),
                  '8': (361,179,80,35),
                  '9': (633,83,80,35)}

seatPositions6 = {'1': (870,79,80,35),
                  '2': (1480,179,80,35),
                  '3': (1526,496,80,35),
                  '4': (968,681,80,35),
                  '5': (314,496,80,35),
                  '6': (361,182,80,35)}

seatPositions2 = {'1': (870,79,80,35), 
                  '2': (967,683,80,35)}


binary = FirefoxBinary(str(Path(r'C:/Program Files/Mozilla Firefox/firefox.exe')))
driver = webdriver.Firefox(firefox_binary = binary, executable_path = str(Path('.\geckodriver.exe')))
driver.set_window_size(200, 700)
driver.get('https://www.888poker.com/poker/poker-odds-calculator')

try:
    popupClose = driver.find_element_by_xpath('/html/body/div[2]/div/img[2]')
    popupClose.click()
except NoSuchElementException:
    pass

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
topOfPage = driver.find_element_by_xpath('//*[@id="poker-table"]')
playerTables = driver.find_elements_by_class_name('player--single.card-selection-block')


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

firstFlop = {}
secondFlop = {}
thirdFlop = {}
turnCard = {}
riverCard = {}
myCard1 = {}
myCard2 = {}
count = 0
lastPlayers = 9
myCardsClicked = 'no'
flopClicked = 'no'
turnClicked = 'no'
riverClicked = 'no'

try:
    while True: #main loop
        if myCard1 == {} or myCard1 is None:
            myCard1 = myFirstCard()
        if myCard2 == {} or myCard2 is None:
            myCard2 = mySecondCard()
        elif myCard1 is None and myCard2 is not None:
            myCard1 = myFirstCard()
        if myCardsClicked == 'no':
            if myCard1 is not None and myCard1 != {}:
                if myCard2 is not None and myCard2 != {}:
                    clickMyCards()
                    myCardsClicked = 'yes'

        players = activePlayers()  
        if players != 0 and lastPlayers != 0:
            if lastPlayers < players:
                players = 0
        if players != lastPlayers:
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
                    driver.execute_script("arguments[0].scrollIntoView(true);", topOfPage)
            elif playerDifference > 0:
            #remove from calc
                removePlayersLink.click()
                for i in range(playerDifference):
                    removePlayer.click()
                closeremovePlayersLink.click()
        lastPlayers = players
                    
        if firstFlop == {} or firstFlop is None:
            firstFlop = firstFlopF()
        if secondFlop == {} or secondFlop is None:
            secondFlop = secondFlopF()
        if thirdFlop == {} or thirdFlop is None:
            thirdFlop = thirdFlopF()
        if turnCard == {} or turnCard is None:
            turnCard = turnCardF()
        if riverCard == {} or riverCard is None:
            riverCard = riverCardF()
        if firstFlop is None and secondFlop is not None:
            firstFlop = firstFlopF()
            logging.info('2nd pass 1st Flop is '+str(firstFlop))
        if secondFlop is None and thirdFlop is not None:
            secondFlop = secondFlopF()
            logging.info('2nd pass 2nd Flop is '+str(secondFlop))
        if thirdFlop is None and turnCard is not None:
            thirdFlop = thirdFlopF()
            logging.info('2nd pass 3rd Flop is '+str(thirdFlop))
        if turnCard is None and riverCard is not None:
            turnCard = turnCardF()
            logging.info('2nd pass turnCard is '+str(turnCard))
        if flopClicked == 'no':
            if firstFlop is not None and firstFlop != {}:
                if secondFlop is not None or secondFlop != {}:
                    if thirdFlop is not None or thirdFlop != {}:
                        clickAllFlopCards()
                        flopClicked = 'yes'
        if turnClicked == 'no':
            if turnCard is not None and turnCard != {}:
                clickTurn()
                turnClicked = 'yes'
        if riverClicked == 'no':
            if riverCard is not None and riverCard != {}:
                clickRiver()
                riverClicked = 'yes'
                
        if players == 0:
            myCard1 = {}
            myCard2 = {}
            firstFlop = {}
            secondFlop = {}
            thirdFlop = {}
            turnCard = {}
            riverCard = {}
            myCardsClicked = 'no'
            flopClicked = 'no'
            turnClicked = 'no'
            riverClicked = 'no'
            StartNewRound()
            time.sleep(2)
                
except KeyboardInterrupt:
    print('Closing geckodriver and firefox...')
    driver.quit()
    subprocess.call(["taskkill","/F","/IM","firefox.exe"])
    print('Done, now exiting...')
    logging.info('End of program')
    time.sleep(2)
    sys.exit()


# Golf Game #

import sys, random

#Player Name
print('What is your name?')
playerName = input()
print()
print('Welcome to Paradise Palms Golf course ' + playerName + '. For instructions please enter (I), to play please enter (P) and to quit please enter (Q). Enjoy your game!')


gameScore = 0

numberOfRounds = 0

playAgain = ''

while playAgain != ('n'):


#main
       
        print()
        print('| Golf!              |')
        print('|  Instructions  (I) |')
        print('|  Play a Hole   (P) |')
        print('|  Quit Game     (Q) |')
        print()

        while True:

                menuSlection = input()

                #Info
                if menuSlection == 'I' or menuSlection == 'i':
                        print()
                        print('This is a simple golf game in which each hole is 230m game away with par 5. You are able to choose from 3 clubs, the Driver, Iron or Putter. The Driver will hit around 100m, the Iron around 30m and the Putter around 10m. The putter is best used very close to the hole.')
                        print()
                        print('| Golf!              |')
                        print('|  Instructions  (I) |')
                        print('|  Play a Hole   (P) |')
                        print('|  Quit Game     (Q) |')
                        print()
                        continue
                
                #Quit game                        
                elif menuSlection == 'Q' or menuSlection == 'q':
                        print()
                        print('Farewell and thanks for playing ' + playerName)
                        sys.exit()
                        
                #Play
                elif menuSlection == 'P' or menuSlection == 'p':
                        break
                
                #Invalid
                else:
                        print()
                        print('Invalid menu choice entered... please select (I)nstructions, (P)lay or (Q)uit to continue.')
                        print()
                        print('| Golf!              |')
                        print('|  Instructions  (I) |')
                        print('|  Play a Hole   (P) |')
                        print('|  Quit Game     (Q) |')
                        print()
                        continue        
        
#playerSwing
        print()
        print('Welcome to the tee off, this hole is 230m par 5. Please select your club.')
        print()
        print('| Swing!             |')
        print('|  Driver ~ 100m (D) |')
        print('|  Iron   ~ 30m  (I) |')
        print('|  Putter ~ 10m  (P) |')
        print()

        distanceToHole = 230
        numberOfSwings = 0
        par = 5

        while distanceToHole > 0:

                clubSlection = input()
                shotDistance = 0
                numberOfSwings += 1
                
                #Diver
                if clubSlection == 'D' or clubSlection == 'd': 
                        print()
                        print('Driver')
                        shotDeterminant = random.randint(80, 120)
                        shotDistance = 100*(shotDeterminant/100)
                        distanceToHole = (distanceToHole) - int(shotDistance)
                        distanceToHole = abs(distanceToHole)
                        print('Your shot went ' + str(int(shotDistance)) + 'm.')
                        print('You are ' + str(distanceToHole) + ' m from the hole, after ' + str(numberOfSwings) + ' swing/s.')
                        print('Select a Club...')
                        print()
                        continue
                
                #Iron                
                elif clubSlection == 'I' or clubSlection == 'i': 
                        print()
                        print('Iron')
                        shotDeterminant = random.randint(80, 120)
                        shotDistance = 30*(shotDeterminant/100)
                        distanceToHole = (distanceToHole) - int(shotDistance)
                        distanceToHole = abs(distanceToHole)
                        print('Your shot went ' + str(int(shotDistance)) + 'm.')
                        print('You are ' + str(distanceToHole) + ' m from the hole, after ' + str(numberOfSwings) + ' swing/s.')
                        print('Select a Club...')
                        print()
                        continue

                #Putter                
                elif clubSlection == 'P' or clubSlection == 'p': 
                        print()
                        print('Putter')
                        
                        shotDeterminant = random.randint(80, 120)
                        
                        if distanceToHole > 10:
                                shotDistance = 10*(shotDeterminant/100)
                                distanceToHole = (distanceToHole) - int(shotDistance)
                                distanceToHole = abs(distanceToHole)
                                print('Your shot went ' + str(int(shotDistance)) + 'm.')
                                print('You are ' + str(distanceToHole) + ' m from the hole, after ' + str(numberOfSwings) + ' swing/s.')
                                print('Select a Club...')
                                print()
                                continue
                        else:
                                shotDistance = distanceToHole*(shotDeterminant/100)
                                
                                if shotDistance < 1:
                                        shotDistance += 1 
                                        distanceToHole = (distanceToHole) - int(shotDistance)
                                        distanceToHole = abs(distanceToHole)
                                        print('Your shot went ' + str(int(shotDistance)) + 'm.')
                                        print('You are ' + str(distanceToHole) + ' m from the hole, after ' + str(numberOfSwings) + ' swing/s.')
                                        print('Select a Club...')
                                        print()
                                        continue
                                
                                else:  
                                        distanceToHole = (distanceToHole) - int(shotDistance)
                                        distanceToHole = abs(distanceToHole)
                                        print('Your shot went ' + str(int(shotDistance)) + 'm.')
                                        print('You are ' + str(distanceToHole) + ' m from the hole, after ' + str(numberOfSwings) + ' swing/s.')
                                        print('Select a Club...')
                                        print()
                                        continue
                
                #Quit game        
                elif clubSlection == 'Q' or clubSlection == 'q': 
                        print()
                        print('Farewell and thanks for playing ' + playerName)
                        sys.exit()
                        
                #Air Swing
                else:                           
                        print()
                        print('Invalid club choice entered... AIR SWING! :(')
                        print('Your shot went ' + str(int(shotDistance)) + 'm.')
                        print('You are ' + str(distanceToHole) + ' m from the hole, after ' + str(numberOfSwings) + ' swing/s.')
                        print('Select a Club... with: D/d, I/i or P/p')
                        print()
                        continue

#displayScore
        gameScore = numberOfSwings + gameScore

        numberOfRounds += 1

   #Hole
        #Under Par                
        if numberOfSwings < 5:
                playerPar = par - numberOfSwings
                print ('Clunk… After ' + str(numberOfSwings) + ' hits your ball is in the hole! Congratulations. You are ' + str(int(playerPar)) + ' under par for this hole.')

        #On Par
        elif numberOfSwings == 5:
                print ('Clunk… After ' + str(numberOfSwings) + ' hits your ball is in the hole! Not bad. You are on par for this hole.')

        #Over Par
        else:
                playerPar = numberOfSwings - par
                print ('Clunk… After ' + str(numberOfSwings) + ' hits your ball is in the hole! Oh dear. You are ' + str(int(playerPar)) + ' over par for this hole.')

   #Game     
        print()
        print('Your current total score after ' + str(numberOfRounds) + ' hole/s is: ' + str(gameScore))

        #Under Par
        if gameScore < 5*numberOfRounds:
                numberOfSwings = par*numberOfRounds - gameScore
                print ('You\'re a Pro! scoring ' + str(int(numberOfSwings)) + ' under par for this game so far. ')

        #On Par
        elif gameScore == 5*numberOfRounds:
                print ('Not too shabby. You are on par for this game so far.')

        #Over Par
        else:
                numberOfSwings = gameScore - par*numberOfRounds
                print ('Oops... You are ' + str(int(numberOfSwings)) + ' over par for this game so far.')

        while True:
                print()
                print('Play another hole? (y)es or (n)o ')
                print()
                playAgain = input()
                
                if playAgain == 'y':
                        break

                elif playAgain == 'n':
                        break
                
                else:
                        print()
                        print('invalid menu choice entered... please select (y)es or (n)o')
                        print()

print('Farewell and thanks for playing ' + playerName)

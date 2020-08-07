from random import *

print('BATTLESHIP GAME')
print('The objective is to sink the opponent\'s ships before the opponent sinks yours.')

players=int(input('Input 1 for 1-player game or 2 for 2-player game: '))

#Position assigning in every Game Choice
#Player 1 vs CPU-Computer

if players==1:
    Player1={}
    CPU={}
    
    for i in range(1,6):
        print('Player 1 enter the position of your ship no ',i)
        possition=str(input())
        while(len(possition)!=2)or(possition in Player1)or(not(possition[0] in 'abcde')or not(possition[1] in '12345')):
            if possition in Player1:
                print('Invalid position, or position already taken. Try again: ')
                possition=str(input())
            elif not(possition[0] in 'abcde')or not(possition[1] in '12345'):
                print('Invalid position, or position already taken. Try again: ')
                possition=str(input())
            else:
                print('Invalid position, or position already taken. Try again: ')
                possition=str(input())
        Player1[possition]=1
        
    for i in range(5):
        posnum=randint(1,5)
        posletter=randint(1,5)
        if posletter==1:
            CPUpossition='a'
        elif posletter==2:
            CPUpossition='b'
        elif posletter==3:
            CPUpossition='c'
        elif posletter==4:
            CPUpossition='d'
        else:
            CPUpossition='e'
        CPUpossition=CPUpossition+str(posnum)
        while CPUpossition in CPU:
            posnum=randint(1,5)
            posletter=randint(1,5)
            if posletter==1:
                CPUpossition='a'
            elif posletter==2:
                CPUpossition='b'
            elif posletter==3:
                CPUpossition='c'
            elif posletter==4:
                CPUpossition='d'
            else:
                CPUpossition='e'
            CPUpossition=CPUpossition+str(posnum)
        CPU[CPUpossition]=1

#Player 1 vs Player 2       
        
elif players==2:
    Player1={}
    Player2={}
    
    for i in range(1,6):
        print('Player 1 enter the position of your ship no ',i)
        possition=str(input())
        while(len(possition)!=2)or(possition in Player1)or(not(possition[0] in 'abcde')or not(possition[1] in '12345')):
            if possition in Player1:
                print ('Invalid position, or position already taken. Try again: ')
                possition=str(input())
            elif not(possition[0] in 'abcde')or not(possition[1] in '12345'):
                print ('Invalid position, or position already taken. Try again: ')
                possition=str(input())
            else:
                print ('Invalid position, or position already taken. Try again: ')
                possition=str(input())
        Player1[possition]=1
        
    for i in range(38):
        print('*')
        
    for i in range(1,6):
        print('Player 2 enter the position of your ship no ',i)
        possition=str(input())
        while(len(possition)!=2)or(possition in Player2)or(not(possition[0] in 'abcde')or not(possition[1] in '12345')):
            if possition in Player2:
                print('Invalid position, or position already taken. Try again: ')
                possition=str(input())
            elif not(possition[0] in 'abcde')or not(possition[1] in '12345'):
                print('Invalid position, or position already taken. Try again: ')
                possition=str(input())
            else:
                print('Invalid position, or position already taken. Try again: ')
                possition=str(input())
        Player2[possition]=1
        
for i in range(31):
    print('*')
        
#The game starts from here
#The game between one player and the computer - CPU

FirstToPlay=randint(1,2)

if players==1:
    player1shots=[]
    CPUshots=[]
    
    Player1Chart={'a1':' ','a2':' ','a3':' ','a4':' ','a5':' ','b1':' ','b2':' ','b3':' ','b4':' ','b5':' ','c1':' ','c2':' ','c3':' ','c4':' ','c5':' ','d1':' ','d2':' ','d3':' ','d4':' ','d5':' ','e1':' ','e2':' ','e3':' ','e4':' ','e5':' '}
    
    CPUChart={'a1':' ','a2':' ','a3':' ','a4':' ','a5':' ','b1':' ','b2':' ','b3':' ','b4':' ','b5':' ','c1':' ','c2':' ','c3':' ','c4':' ','c5':' ','d1':' ','d2':' ','d3':' ','d4':' ','d5':' ','e1':' ','e2':' ','e3':' ','e4':' ','e5':' '}
    
    print('       P1             P2')
    print('   1 2 3 4 5      1 2 3 4 5')
    print('a ',Player1Chart['a1'],Player1Chart['a2'],Player1Chart['a3'],Player1Chart['a4'],Player1Chart['a5'],'  a ',CPUChart['a1'],CPUChart['a2'],CPUChart['a3'],CPUChart['a4'],CPUChart['a5'])
    print('b ',Player1Chart['b1'],Player1Chart['b2'],Player1Chart['b3'],Player1Chart['b4'],Player1Chart['b5'],'  b ',CPUChart['b1'],CPUChart['b2'],CPUChart['b3'],CPUChart['b4'],CPUChart['b5'])
    print('c ',Player1Chart['c1'],Player1Chart['c2'],Player1Chart['c3'],Player1Chart['c4'],Player1Chart['c5'],'  c ',CPUChart['c1'],CPUChart['c2'],CPUChart['c3'],CPUChart['c4'],CPUChart['c5'])
    print('d ',Player1Chart['d1'],Player1Chart['d2'],Player1Chart['d3'],Player1Chart['d4'],Player1Chart['d5'],'  d ',CPUChart['d1'],CPUChart['d2'],CPUChart['d3'],CPUChart['d4'],CPUChart['d5'])
    print('e ',Player1Chart['e1'],Player1Chart['e2'],Player1Chart['e3'],Player1Chart['e4'],Player1Chart['e5'],'  e ',CPUChart['e1'],CPUChart['e2'],CPUChart['e3'],CPUChart['e4'],CPUChart['e5'])
    
#When the first player is Player 1

    if FirstToPlay==1:     
        print ('Player 1 starts first')
        while len(Player1)!=0 and len(CPU)!=0:
            print('Player 1\'s turn ')
            missile=str(input('Player 1 enter the possition you want to throw your missile: '))
            while len(missile)>2 or not(missile[0] in 'abcde' and missile[1] in '12345'):
                missile=str(input('Invalid position, or missile already thrown there. Try again:'))
            while missile in player1shots:
                missile=str(input('Player 1 you alredy throwed a missile in that possition please enter onother one: '))
                while len(missile)>2 or not(missile[0] in 'abcde' and missile[1] in '12345'):
                    missile=str(input('Invalid position, or missile already thrown there. Try again:'))
            player1shots.append(missile)
            print('Missile thrown at ',missile)
            if missile in CPU:
                print('Target Hit!')
                del(CPU[missile])
                CPUChart[missile]='o'
            else:
                print('Target Missed!')
                CPUChart[missile]='x'
            print('       P1             P2')
            print('   1 2 3 4 5      1 2 3 4 5')
            print('a ',Player1Chart['a1'],Player1Chart['a2'],Player1Chart['a3'],Player1Chart['a4'],Player1Chart['a5'],'  a ',CPUChart['a1'],CPUChart['a2'],CPUChart['a3'],CPUChart['a4'],CPUChart['a5'])
            print('b ',Player1Chart['b1'],Player1Chart['b2'],Player1Chart['b3'],Player1Chart['b4'],Player1Chart['b5'],'  b ',CPUChart['b1'],CPUChart['b2'],CPUChart['b3'],CPUChart['b4'],CPUChart['b5'])
            print('c ',Player1Chart['c1'],Player1Chart['c2'],Player1Chart['c3'],Player1Chart['c4'],Player1Chart['c5'],'  c ',CPUChart['c1'],CPUChart['c2'],CPUChart['c3'],CPUChart['c4'],CPUChart['c5'])
            print('d ',Player1Chart['d1'],Player1Chart['d2'],Player1Chart['d3'],Player1Chart['d4'],Player1Chart['d5'],'  d ',CPUChart['d1'],CPUChart['d2'],CPUChart['d3'],CPUChart['d4'],CPUChart['d5'])
            print('e ',Player1Chart['e1'],Player1Chart['e2'],Player1Chart['e3'],Player1Chart['e4'],Player1Chart['e5'],'  e ',CPUChart['e1'],CPUChart['e2'],CPUChart['e3'],CPUChart['e4'],CPUChart['e5'])
            missile=randint(1,5)
            missileletter=randint(1,5)
            if missileletter==1:
                CPUmissile='a'
            elif missileletter==2:
                CPUmissile='b'
            elif missileletter==3:
                CPUmissile='c'
            elif missileletter==4:
                CPUmissile='d'
            else:
                CPUmissile='e'
            CPUmissile=CPUmissile+str(missile)
            while CPUmissile in CPUshots:
                missile=randint(1,5)
                missileletter=randint(1,5)
                if missileletter==1:
                    CPUmissile='a'
                elif missileletter==2:
                    CPUmissile='b'
                elif missileletter==3:
                    CPUmissile='c'
                elif missileletter==4:
                    CPUmissile='d'
                else:
                    CPUmissile='e'
                CPUmissile=CPUmissile+str(missile)
            CPUshots.append(CPUmissile)
            print ('CPU\'s turn')
            print ('Missile thrown at ',CPUmissile)
            if CPUmissile in Player1:
                print ('Target Hit!')
                del(Player1[CPUmissile])
                Player1Chart[CPUmissile]='o'
            else:
                print ('Target Missed!')
                Player1Chart[CPUmissile]='x'
            print('       P1             P2')
            print('   1 2 3 4 5      1 2 3 4 5')
            print('a ',Player1Chart['a1'],Player1Chart['a2'],Player1Chart['a3'],Player1Chart['a4'],Player1Chart['a5'],'  a ',CPUChart['a1'],CPUChart['a2'],CPUChart['a3'],CPUChart['a4'],CPUChart['a5'])
            print('b ',Player1Chart['b1'],Player1Chart['b2'],Player1Chart['b3'],Player1Chart['b4'],Player1Chart['b5'],'  b ',CPUChart['b1'],CPUChart['b2'],CPUChart['b3'],CPUChart['b4'],CPUChart['b5'])
            print('c ',Player1Chart['c1'],Player1Chart['c2'],Player1Chart['c3'],Player1Chart['c4'],Player1Chart['c5'],'  c ',CPUChart['c1'],CPUChart['c2'],CPUChart['c3'],CPUChart['c4'],CPUChart['c5'])
            print('d ',Player1Chart['d1'],Player1Chart['d2'],Player1Chart['d3'],Player1Chart['d4'],Player1Chart['d5'],'  d ',CPUChart['d1'],CPUChart['d2'],CPUChart['d3'],CPUChart['d4'],CPUChart['d5'])
            print('e ',Player1Chart['e1'],Player1Chart['e2'],Player1Chart['e3'],Player1Chart['e4'],Player1Chart['e5'],'  e ',CPUChart['e1'],CPUChart['e2'],CPUChart['e3'],CPUChart['e4'],CPUChart['e5'])
        if len(Player1)==0:
            print('GAME OVER. CPU wins')
        else:
            print('GAME OVER. PLAYER 1 wins')
            
#When the computer-CPU starts first     

    else:       
        player1shots=[]
        CPUshots=[]
        print('CPU starts first')
        while len(Player1)!=0 and len(CPU)!=0:
            print('CPU\'s turn')
            missile=randint(1,5)
            missileletter=randint(1,5)
            if missileletter==1:
                CPUmissile='a'
            elif missileletter==2:
                CPUmissile='b'
            elif missileletter==3:
                CPUmissile='c'
            elif missileletter==4:
                CPUmissile='d'
            else:
                CPUmissile='e'
            CPUmissile=CPUmissile+str(missile)
            while CPUmissile in CPUshots:
                missile=randint(1,5)
                missileletter=randint(1,5)
                if missileletter==1:
                    CPUmissile='a'
                elif missileletter==2:
                    CPUmissile='b'
                elif missileletter==3:
                    CPUmissile='c'
                elif missileletter==4:
                    CPUmissile='d'
                else:
                    CPUmissile='e'
                CPUmissile=CPUmissile+str(missile)
            CPUshots.append(CPUmissile)
            print('Missile thrown at ',CPUmissile)
            if CPUmissile in Player1:
                print('Target Hit!')
                del(Player1[CPUmissile])
                Player1Chart[CPUmissile]='o'
            else:
                print('Target Missed!')
                Player1Chart[CPUmissile]='x'
            print('       P1             P2')
            print('   1 2 3 4 5      1 2 3 4 5')
            print('a ',Player1Chart['a1'],Player1Chart['a2'],Player1Chart['a3'],Player1Chart['a4'],Player1Chart['a5'],'  a ',CPUChart['a1'],CPUChart['a2'],CPUChart['a3'],CPUChart['a4'],CPUChart['a5'])
            print('b ',Player1Chart['b1'],Player1Chart['b2'],Player1Chart['b3'],Player1Chart['b4'],Player1Chart['b5'],'  b ',CPUChart['b1'],CPUChart['b2'],CPUChart['b3'],CPUChart['b4'],CPUChart['b5'])
            print('c ',Player1Chart['c1'],Player1Chart['c2'],Player1Chart['c3'],Player1Chart['c4'],Player1Chart['c5'],'  c ',CPUChart['c1'],CPUChart['c2'],CPUChart['c3'],CPUChart['c4'],CPUChart['c5'])
            print('d ',Player1Chart['d1'],Player1Chart['d2'],Player1Chart['d3'],Player1Chart['d4'],Player1Chart['d5'],'  d ',CPUChart['d1'],CPUChart['d2'],CPUChart['d3'],CPUChart['d4'],CPUChart['d5'])
            print('e ',Player1Chart['e1'],Player1Chart['e2'],Player1Chart['e3'],Player1Chart['e4'],Player1Chart['e5'],'  e ',CPUChart['e1'],CPUChart['e2'],CPUChart['e3'],CPUChart['e4'],CPUChart['e5'])
            print('Player 1\'s turn ')
            missile=str(input('Player 1 enter the possition you want to throw your missile: '))
            while len(missile)>2 or not(missile[0] in 'abcde' and missile[1] in '12345'):
                missile=str(input('Invalid position, or missile already thrown there. Try again:'))
            while missile in player1shots:
                missile=str(input('Invalid position, or missile already thrown there. Try again: '))
                while len(missile)>2 or not(missile[0] in 'abcde' and missile[1] in '12345'):
                    missile=str(input('Invalid position, or missile already thrown there. Try again:'))
            player1shots.append(missile)
            print ('Missile thrown at ',missile)
            if missile in CPU:
                print('Target Hit!')
                del(CPU[missile])
                CPUChart[missile]='o'
            else:
                print('Target Missed!')
                CPUChart[missile]='x'
            print('       P1              P2')
            print('   1 2 3 4 5      1 2 3 4 5')
            print('a ',Player1Chart['a1'],Player1Chart['a2'],Player1Chart['a3'],Player1Chart['a4'],Player1Chart['a5'],'  a ',CPUChart['a1'],CPUChart['a2'],CPUChart['a3'],CPUChart['a4'],CPUChart['a5'])
            print('b ',Player1Chart['b1'],Player1Chart['b2'],Player1Chart['b3'],Player1Chart['b4'],Player1Chart['b5'],'  b ',CPUChart['b1'],CPUChart['b2'],CPUChart['b3'],CPUChart['b4'],CPUChart['b5'])
            print('c ',Player1Chart['c1'],Player1Chart['c2'],Player1Chart['c3'],Player1Chart['c4'],Player1Chart['c5'],'  c ',CPUChart['c1'],CPUChart['c2'],CPUChart['c3'],CPUChart['c4'],CPUChart['c5'])
            print('d ',Player1Chart['d1'],Player1Chart['d2'],Player1Chart['d3'],Player1Chart['d4'],Player1Chart['d5'],'  d ',CPUChart['d1'],CPUChart['d2'],CPUChart['d3'],CPUChart['d4'],CPUChart['d5'])
            print('e ',Player1Chart['e1'],Player1Chart['e2'],Player1Chart['e3'],Player1Chart['e4'],Player1Chart['e5'],'  e ',CPUChart['e1'],CPUChart['e2'],CPUChart['e3'],CPUChart['e4'],CPUChart['e5'])
        if len(Player1)==0:
            print('GAME OVER. CPU wins')
        else:
            print('GAME OVER. Player 1 wins')
            
#Game Between 2 individual players
        
elif players==2:
    player1shots=[]
    player2shots=[]
    
    Player1Chart={'a1':' ','a2':' ','a3':' ','a4':' ','a5':' ','b1':' ','b2':' ','b3':' ','b4':' ','b5':' ','c1':' ','c2':' ','c3':' ','c4':' ','c5':' ','d1':' ','d2':' ','d3':' ','d4':' ','d5':' ','e1':' ','e2':' ','e3':' ','e4':' ','e5':' '}
    
    Player2Chart={'a1':' ','a2':' ','a3':' ','a4':' ','a5':' ','b1':' ','b2':' ','b3':' ','b4':' ','b5':' ','c1':' ','c2':' ','c3':' ','c4':' ','c5':' ','d1':' ','d2':' ','d3':' ','d4':' ','d5':' ','e1':' ','e2':' ','e3':' ','e4':' ','e5':' '}
    
#When the player 1 starts first

    if FirstToPlay==1:     
        print('Player 1 starts first')
        print('       P1             P2')
        print('   1 2 3 4 5      1 2 3 4 5')
        print('a ',Player1Chart['a1'],Player1Chart['a2'],Player1Chart['a3'],Player1Chart['a4'],Player1Chart['a5'],'  a ',Player2Chart['a1'],Player2Chart['a2'],Player2Chart['a3'],Player2Chart['a4'],Player2Chart['a5'])
        print('b ',Player1Chart['b1'],Player1Chart['b2'],Player1Chart['b3'],Player1Chart['b4'],Player1Chart['b5'],'  b ',Player2Chart['b1'],Player2Chart['b2'],Player2Chart['b3'],Player2Chart['b4'],Player2Chart['b5'])
        print('c ',Player1Chart['c1'],Player1Chart['c2'],Player1Chart['c3'],Player1Chart['c4'],Player1Chart['c5'],'  c ',Player2Chart['c1'],Player2Chart['c2'],Player2Chart['c3'],Player2Chart['c4'],Player2Chart['c5'])
        print('d ',Player1Chart['d1'],Player1Chart['d2'],Player1Chart['d3'],Player1Chart['d4'],Player1Chart['d5'],'  d ',Player2Chart['d1'],Player2Chart['d2'],Player2Chart['d3'],Player2Chart['d4'],Player2Chart['d5'])
        print('e ',Player1Chart['e1'],Player1Chart['e2'],Player1Chart['e3'],Player1Chart['e4'],Player1Chart['e5'],'  e ',Player2Chart['e1'],Player2Chart['e2'],Player2Chart['e3'],Player2Chart['e4'],Player2Chart['e5'])
        while len(Player1)!=0 and len(Player2)!=0:
            print('Player 1\'s turn ')
            missile=str(input('Player1 enter the possition you want to throw your missile: '))
            while len(missile)>2 or not(missile[0] in 'abcde' and missile[1] in '12345'):
                missile=str(input('Invalid position, or missile already thrown there. Try again:'))
            while missile in player1shots:
                missile=str(input('Invalid position, or missile already thrown there. Try again:'))
                while len(missile)>2 or not(missile[0] in 'abcde' and missile[1] in '12345'):
                    missile=str(input('Invalid position, or missile already thrown there. Try again:'))
            player1shots.append(missile)
            print('Missile thrown at ',missile)
            if missile in Player2:
                print('Target Hit!')
                del(Player2[missile])
                Player2Chart[missile]='o'
            else:
                print('Target Missed!')
                Player2Chart[missile]='x'
            print('       P1             P2')
            print('   1 2 3 4 5      1 2 3 4 5')
            print('a ',Player1Chart['a1'],Player1Chart['a2'],Player1Chart['a3'],Player1Chart['a4'],Player1Chart['a5'],'  a ',Player2Chart['a1'],Player2Chart['a2'],Player2Chart['a3'],Player2Chart['a4'],Player2Chart['a5'])
            print ('b ',Player1Chart['b1'],Player1Chart['b2'],Player1Chart['b3'],Player1Chart['b4'],Player1Chart['b5'],'  b ',Player2Chart['b1'],Player2Chart['b2'],Player2Chart['b3'],Player2Chart['b4'],Player2Chart['b5'])
            print ('c ',Player1Chart['c1'],Player1Chart['c2'],Player1Chart['c3'],Player1Chart['c4'],Player1Chart['c5'],'  c ',Player2Chart['c1'],Player2Chart['c2'],Player2Chart['c3'],Player2Chart['c4'],Player2Chart['c5'])
            print ('d ',Player1Chart['d1'],Player1Chart['d2'],Player1Chart['d3'],Player1Chart['d4'],Player1Chart['d5'],'  d ',Player2Chart['d1'],Player2Chart['d2'],Player2Chart['d3'],Player2Chart['d4'],Player2Chart['d5'])
            print ('e ',Player1Chart['e1'],Player1Chart['e2'],Player1Chart['e3'],Player1Chart['e4'],Player1Chart['e5'],'  e ',Player2Chart['e1'],Player2Chart['e2'],Player2Chart['e3'],Player2Chart['e4'],Player2Chart['e5'])
            if len(Player2)==0:
                break
            missile=str(input('Player 2 enter the possition to throw your missile: '))
            while len(missile)>2 or not(missile[0] in 'abcde' and missile[1] in '12345'):
                missile=str(input('Invalid position, or missile already thrown there. Try again:'))
            while missile in player2shots:
                missile=str(input('Invalid position, or missile already thrown there. Try again:'))
                while len(missile)>2 or not(missile[0] in 'abcde' and missile[1] in '12345'):
                    missile=str(input('Invalid position, or missile already thrown there. Try again:'))
            player2shots.append(missile)
            print('Missile thrown at ',missile)
            if missile in Player1:
                print('Target Hit!')
                del(Player1[missile])
                Player1Chart[missile]='o'
            else:
                print('Target Missed!')
                Player1Chart[missile]='x'
            print('       P1             P2')
            print('   1 2 3 4 5      1 2 3 4 5')
            print('a ',Player1Chart['a1'],Player1Chart['a2'],Player1Chart['a3'],Player1Chart['a4'],Player1Chart['a5'],'  a ',Player2Chart['a1'],Player2Chart['a2'],Player2Chart['a3'],Player2Chart['a4'],Player2Chart['a5'])
            print('b ',Player1Chart['b1'],Player1Chart['b2'],Player1Chart['b3'],Player1Chart['b4'],Player1Chart['b5'],'  b ',Player2Chart['b1'],Player2Chart['b2'],Player2Chart['b3'],Player2Chart['b4'],Player2Chart['b5'])
            print('c ',Player1Chart['c1'],Player1Chart['c2'],Player1Chart['c3'],Player1Chart['c4'],Player1Chart['c5'],'  c ',Player2Chart['c1'],Player2Chart['c2'],Player2Chart['c3'],Player2Chart['c4'],Player2Chart['c5'])
            print('d ',Player1Chart['d1'],Player1Chart['d2'],Player1Chart['d3'],Player1Chart['d4'],Player1Chart['d5'],'  d ',Player2Chart['d1'],Player2Chart['d2'],Player2Chart['d3'],Player2Chart['d4'],Player2Chart['d5'])
            print('e ',Player1Chart['e1'],Player1Chart['e2'],Player1Chart['e3'],Player1Chart['e4'],Player1Chart['e5'],'  e ',Player2Chart['e1'],Player2Chart['e2'],Player2Chart['e3'],Player2Chart['e4'],Player2Chart['e5'])
        if len(Player1)==0:
            print('GAME OVER. Player 2 wins')
        else:
            print('GAME OVER. Player 1 wins')
   
    #when Player 2 starts first
    
    else:       
        print('Player 2\'s turn ')
        while len(Player1)!=0 and len(Player2)!=0:
            print('       P1             P2')
            print('   1 2 3 4 5      1 2 3 4 5')
            print('a ',Player1Chart['a1'],Player1Chart['a2'],Player1Chart['a3'],Player1Chart['a4'],Player1Chart['a5'],'  a ',Player2Chart['a1'],Player2Chart['a2'],Player2Chart['a3'],Player2Chart['a4'],Player2Chart['a5'])
            print('b ',Player1Chart['b1'],Player1Chart['b2'],Player1Chart['b3'],Player1Chart['b4'],Player1Chart['b5'],'  b ',Player2Chart['b1'],Player2Chart['b2'],Player2Chart['b3'],Player2Chart['b4'],Player2Chart['b5'])
            print('c ',Player1Chart['c1'],Player1Chart['c2'],Player1Chart['c3'],Player1Chart['c4'],Player1Chart['c5'],'  c ',Player2Chart['c1'],Player2Chart['c2'],Player2Chart['c3'],Player2Chart['c4'],Player2Chart['c5'])
            print('d ',Player1Chart['d1'],Player1Chart['d2'],Player1Chart['d3'],Player1Chart['d4'],Player1Chart['d5'],'  d ',Player2Chart['d1'],Player2Chart['d2'],Player2Chart['d3'],Player2Chart['d4'],Player2Chart['d5'])
            print('e ',Player1Chart['e1'],Player1Chart['e2'],Player1Chart['e3'],Player1Chart['e4'],Player1Chart['e5'],'  e ',Player2Chart['e1'],Player2Chart['e2'],Player2Chart['e3'],Player2Chart['e4'],Player2Chart['e5'])
            missile=str(input('Player2 enter the possition to throw your missile: '))
            while len(missile)>2 or not(missile[0] in 'abcde' and missile[1] in '12345'):
                missile=str(input('Invalid position, or missile already thrown there. Try again:'))
            while missile in player2shots:
                missile=str(input('Invalid position, or missile already thrown there. Try again:'))
                while len(missile)>2 or not(missile[0] in 'abcde' and missile[1] in '12345'):
                    missile=str(input('Invalid position, or position already taken. Try again: '))
            player2shots.append(missile)
            print('Missile thrown at ',missile)
            if missile in Player1:
                print('Target Hit!')
                del(Player1[missile])
                Player1Chart[missile]='o'
            else:
                print('Target Missed!')
                Player1Chart[missile]='x'
            print('       P1             P2')
            print('   1 2 3 4 5      1 2 3 4 5')
            print('a ',Player1Chart['a1'],Player1Chart['a2'],Player1Chart['a3'],Player1Chart['a4'],Player1Chart['a5'],'  a ',Player2Chart['a1'],Player2Chart['a2'],Player2Chart['a3'],Player2Chart['a4'],Player2Chart['a5'])
            print('b ',Player1Chart['b1'],Player1Chart['b2'],Player1Chart['b3'],Player1Chart['b4'],Player1Chart['b5'],'  b ',Player2Chart['b1'],Player2Chart['b2'],Player2Chart['b3'],Player2Chart['b4'],Player2Chart['b5'])
            print('c ',Player1Chart['c1'],Player1Chart['c2'],Player1Chart['c3'],Player1Chart['c4'],Player1Chart['c5'],'  c ',Player2Chart['c1'],Player2Chart['c2'],Player2Chart['c3'],Player2Chart['c4'],Player2Chart['c5'])
            print('d ',Player1Chart['d1'],Player1Chart['d2'],Player1Chart['d3'],Player1Chart['d4'],Player1Chart['d5'],'  d ',Player2Chart['d1'],Player2Chart['d2'],Player2Chart['d3'],Player2Chart['d4'],Player2Chart['d5'])
            print('e ',Player1Chart['e1'],Player1Chart['e2'],Player1Chart['e3'],Player1Chart['e4'],Player1Chart['e5'],'  e ',Player2Chart['e1'],Player2Chart['e2'],Player2Chart['e3'],Player2Chart['e4'],Player2Chart['e5'])
            
            if len(Player1)==0:
                break
            missile=str(input('Player 1 enter the possition to throw your missile: '))
            while len(missile)>2 or not(missile[0] in 'abcde' and missile[1] in '12345'):
                missile=str(input('Invalid position, or missile already thrown there. Try again: '))
            while missile in player1shots:
                missile=str(input('Invalid position, or missile already thrown there. Try again:'))
                while len(missile)>2 or not(missile[0] in 'abcde' and missile[1] in '12345'):
                    missile=str(input('Invalid position, or missile already thrown there. Try again:'))
            player1shots.append(missile)
            print('Missile thrown at ',missile)
            
            if missile in Player2:
                print('Target Hit!')
                del(Player2[missile])
                Player2Chart[missile]='o'
            else:
                print('Target Missed!')
                Player2Chart[missile]='x'
            
            print('       P1             P2')
            print('   1 2 3 4 5      1 2 3 4 5')
            print('a ',Player1Chart['a1'],Player1Chart['a2'],Player1Chart['a3'],Player1Chart['a4'],Player1Chart['a5'],'  a ',Player2Chart['a1'],Player2Chart['a2'],Player2Chart['a3'],Player2Chart['a4'],Player2Chart['a5'])
            print('b ',Player1Chart['b1'],Player1Chart['b2'],Player1Chart['b3'],Player1Chart['b4'],Player1Chart['b5'],'  b ',Player2Chart['b1'],Player2Chart['b2'],Player2Chart['b3'],Player2Chart['b4'],Player2Chart['b5'])
            print('c ',Player1Chart['c1'],Player1Chart['c2'],Player1Chart['c3'],Player1Chart['c4'],Player1Chart['c5'],'  c ',Player2Chart['c1'],Player2Chart['c2'],Player2Chart['c3'],Player2Chart['c4'],Player2Chart['c5'])
            print('d ',Player1Chart['d1'],Player1Chart['d2'],Player1Chart['d3'],Player1Chart['d4'],Player1Chart['d5'],'  d ',Player2Chart['d1'],Player2Chart['d2'],Player2Chart['d3'],Player2Chart['d4'],Player2Chart['d5'])
            print('e ',Player1Chart['e1'],Player1Chart['e2'],Player1Chart['e3'],Player1Chart['e4'],Player1Chart['e5'],'  e ',Player2Chart['e1'],Player2Chart['e2'],Player2Chart['e3'],Player2Chart['e4'],Player2Chart['e5'])
        
        if len(Player1)==0:
            print('GAME OVER. Player 2 wins')
        else:
            print('GAME OVER. Player 1 wins')
            

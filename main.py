print('''     / \     { _____}      / \     
   /  |  \___/*******\___/  |  \   
  (   I  /   ~   '   ~   \  I   )  
   \  |  |   0       0   |  |  /   
     \   |       A       |   /     
       \__    _______    __/       
          \_____________/          
    _-------*         *-------_    
   /  /---               ---\  \   
 /  /     (             )     \  \ 
{  (     (               )     )  }
 \  \    |               |    /  / 
   \  \  |               |  /  /   
    **** |               | ****    
   //|\\  \_____________/  //|\\    ''')


print('Welcome to the treasure Island!')
print('Our mission is to find the treasure.')

choice1 = input('You Are at a crossroad, where do you want to go? Type "left" or "right".').lower()

if  choice1 == "left":
    choice2 = input('You have come to a lake. There is an island in the middle of the lake. Type "wait" for wait for a boat or type "swim" for swim across').lower()
    
    if choice2 == "wait":
        choice3 = input("You have three doors in front of you. Choose 'Red','Yellow', 'Blue'").lower()
    else:
        print('''
                                (..       \_    ,  |\  /|
                    \       O  \  /|  \ \/ /
                    \______    \/ |   \  / 
                        vvvv\    \ |   /  |
                        \^^^^  ==   \_/   |
                        `\_   ===    \.  |
                        / /\_   \ /      |
                        |/   \_  \|      /
                    snd         \________/
                                
              A fish ate you!
   __________
       /          \                                             (
      /____________\                                           (\)
       |:_:_:_:_:_|                                             ))
       |_:_,--.:_:|                                          (\//   )
       |:_:|__|_:_|                         _               ) ))   ((
    _  |_   _  :_:|   _   _   _            (_)             ((((   /)\`
   | |_| |_| |   _|  | |_| |_| |             o              \\)) (( (
    \_:_:_:_:/|_|_|_|\:_:_:_:_/             .                ((   ))))
     |_,-._:_:_:_:_:_:_:_.-,_|                                )) ((//
     |:|_|:_:_:,---,:_:_:|_|:|                               ,-.  )/
     |_:_:_:_,'     `,_:_:_:_|           _  o               ,;'))((
     |:_:_:_/  _ | _  \_:_:_:|          (_O                   ((  ))
_____|_:_:_|  (o)-(o)  |_:_:_|--'`-.     ,--.                (((\'/
 ', ;|:_:_:| -( .-. )- |:_:_:| ', ; `--._\  /,---.~           \`))
.  ` |_:_:_|   \`-'/   |_:_:_|.  ` .  `  /()\.__( ) .,-----'`-\((
 ', ;|:_:_:|    `-'    |:_:_:| ', ; ', ; `--'|   \ ', ; ', ; ',')).,--
.  ` MJP ` .  ` .  ` .  ` .  ` .  ` .  ` .    .  ` .  ` .  ` .  ` .  `
 ', ; ', ; ', ; ', ; ', ; ', ; ', ; ', ; ', ; ', ; ', ; ', ; ', ; ', ;             
              A fish ate you! you are done
              
              ''')
else:
    print('''
           |\---/|
                       /  , , |
                  __.-'|  / \ /
         __ ___.-'        ._O|
      .-'  '        :      _/
     / ,    .        .     |
    :  ;    :        :   _/
    |  |   .'     __:   /
    |  :   /'----'| \  |
    \  |\  |      | /| |
     '.'| /       || \ |
     | /|.'       '.l \\_
     
     Ops! You are dead! He ate you.
          ''')    
    







chambers=input("COMRADE, plz enter the number of chambers you want: ")

if not chambers:
    chambers=5
    
elif not chambers.isdigit():
    quit("Invalid number of chambers!")
    
kill_bullet=random.randint(1,int(chambers)+1)

for x in range(1,int(chambers)+1):
    input("Press ENTER to pull the trigger!")
    
    if x==kill_bullet:
        print("Sorry comrade, you lost the game")
        print("GAME OVER!!")
        
        start_again=input("Do you want to play again?(y/n): ")
        if start_again=="y":
            os.execv(sys.executable, [sys.executable] + sys.argv)
        else:
            break
            
    print("Congrats, you live to see another day!")        
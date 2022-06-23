def ticketMachine():
    print("Welcome to LRT service")
    print("Select a place what would you like to go" )
    print("1.Kuala Lumpur 2.Selangor 3.Melaka 4.Johor 5.Penang ")
    place=input()
    print("Thank you!The total is RM10. Please insert your cash")
    
    cash=int(cash)
    cashRemaing=int(cashRemaing)
    while (True):
        cash=input()
        
        
    
        if(cash<10):
            cashRemaing=10-cash
            print(" %d left.You have insert more %d"  % (cashRemaing,cashRemaing))
            
           
            
            
            
        elif(cash==10):
            print("Completed. Please take your ticket.")
            break
                
        elif(cash>10):
            print("Completed. Here is your change RM %d and take your ticket" % (cash-10))
            break
                
                
              
            
            
            
ticketMachine()
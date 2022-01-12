print("Welcome to Mitashi's Bank:")
restart=('Y')
chances= 3
balance=67.14
while chances >=0:
  pin = int(input('please enter you 4 digit pin :'))
  if pin ==2501:
    print('you entered the correct pin \n')
    while restart not in ('n','NO','no','N'):
      print("please press 1 for your balance \n")
      print("please press 2  to make withdrawl  \n")
      print("please press 3 to pay \n")
      print("please press 4 to return card  \n")
      option = int(input('what would you like to choose :'))
      if option ==1 :
        print('your current balance $',balance ,'\n')
        restart= input('would u like to go back')
        if restart in ('n','NO','no','N'):
          print('THANK YOU :)')
          break

      elif option ==2:
          option2=('y')
          withdrawl= float(input('how much you want to withdrawl?\n$10/$20/$40/$60/$80/$100 for other enter 1: '))
          if withdrawl in [10,20,40,60,80,100]:
            balance=balance-withdrawl
            print('\n your current balance is now $',balance)
            restart=input('\n would you like to go back?\n')
            if restart in ('n','NO','no','N'):
             print('THANK YOU :)')
             break
          elif withdrawl != [10,20,40,60,80,100]: 
            print('\n invalid amount,please retry\n')
            restart=('y')
          elif withdrawl ==1:
            withdrawl =float(input('please enter the desired amount:'))

      elif option==3 :
        pay_in= float(input('how much would you like to pay in ?'))
        balance= balance + pay_in
        print('your current balance $',balance ,'\n')
        restart= input('would u like to go back')
        if restart in ('n','NO','no','N'):
          print('THANK YOU :)')
          break

      elif option==4:
        print('please wait while your card is returned.. ')
        print('\n Thank you for your service')
        break
      
      else :
        print('please enter the correct number')
        restart=('y')
        
  elif pin!=('2501'):
    print('please enter the correct pin')
    chances-= 1
    if chances ==0:
      print('no more tries u donont belong here:(')
      break

list=[['🤣','😂','😁'],['😁','😀','😀'],['😃','🤣','😂']]
print(f"{list[0] }\n{list[1]} \n{list[2]}")
position=int(input("Enter the positoion of row:"))
position1=int(input("enter the postion of the column:"))
list[position-1][position1-1]="X "
print("after the value")
print(f"{list[0] }\n{list[1]} \n{list[2]}")

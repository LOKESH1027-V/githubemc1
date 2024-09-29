marks={
    "loki":97,
    "tobi":87,
    "obito":78,
    "lucy":67,
    "ajay":56,
    "lokesh":45
}
for i in marks:
    if marks[i]>91:
        marks[i]="A"
    elif marks[i]>90:    
        marks[i]="B"
    elif marks[i]>80:
        marks[i]="C" 
    elif marks[i]>70:
        marks[i]="D"
    elif marks[i]>60:  
        marks[i]="E"
    elif marks[i]>50: 
        marks[i]="F"
    else:
        marks[i]="Fail"
for i in marks:
    print(f"{i}:{marks[i]}")                        
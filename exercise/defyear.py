def years(year,month):
    months=["january","febrary","march","april","may","june","july","agust","september","october","november","december"]
    if year%4==0 and year%100 !=0:
        if month==2:
            print(f"Number of days in {months[month-1]} is 29")
        elif month%2==1:
            print(f"Number of days in {months[month-1]} is 31")
        else:
            print(f"Number of days in {months[month-1]} is 30")     
    else:
        if month==2:
            print(f"Number of days in {months[month-1]} is 28")
        elif month%2==1:
            print(f"Number of days in {months[month-1]} is 31")
        else:
            print(f"Number of days in {months[month-1]} is 30")     
year=int(input("Enter the year:"))
month=int(input("Enter the month in number:"))
y=years
y(year,month)              


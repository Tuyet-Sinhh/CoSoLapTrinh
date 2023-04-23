def Monqua(day):
    if day == 1:
        return "A partridge in a pear tree."+"\n"
    elif day == 2:
        return "Two turtle doves," + "\n"+ "And a partridge in a pear tree." + "\n"
    elif day == 3:
        return "Three French hens," +"\n"+ Monqua(day-1)
    elif day == 4:
        return "Four calling birds," +"\n"+ Monqua(day-1)
    elif day == 5:
        return "Five golden rings,"+"\n" + Monqua(day-1)
    elif day == 6:
        return "Six geese a-laying,"+"\n" + Monqua(day-1)
    elif day == 7:
        return "Seven swans a-swimming,"+"\n"+ Monqua(day-1)
    elif day == 8:
        return "Eight maids a-milking,"+"\n" + Monqua(day-1)
    elif day == 9:
        return "Nine ladies dancing,"+"\n" + Monqua(day-1)
    elif day == 10:
        return "Ten lords a-leaping,"+"\n"+ Monqua(day-1)
    elif day == 11:
        return "Eleven pipers piping,"+"\n" + Monqua(day-1)
    elif day == 12:
        return "Twelve drummers drumming,"+"\n" + Monqua(day-1)
def Day():
    for i in range(1,13):
        print("On the", end=" ")
        if i ==1: print("first",end=" ")
        elif i==2: print("second",end=" ")
        elif i==3: print("third",end=" ")
        elif i==4: print("fourth",end=" ")
        elif i==5: print("fifth",end=" ")
        elif i==6: print("sixth",end=" ")
        elif i==7: print("seventh",end=" ")
        elif i==8: print("eighth",end=" ")
        elif i==9: print("ninth",end=" ")
        elif i==10: print("tenth",end=" ")
        elif i==11: print("eleventh",end=" ")
        elif i==12: print("twelfth",end=" ")
        print("day of Christmas,","\nmy true love sent to me:")
        print(Monqua(i))
        print()
Day()
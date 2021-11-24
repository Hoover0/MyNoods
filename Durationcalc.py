hour = int(input("Starting time (hours): ")) #Event start hour
mins = int(input("Starting time (minutes): ")) #Event start minute
dura = int(input("Event duration (minutes): ")) #Event duration

endM = int((dura+mins) % 60) #Calculates the minute the event ends
endH = hour + ((mins+dura) // 60) #Calculates the hour the event ends

#Makes sure the output stays in proper 24-hour time format
while endH > 24:
    endH -= 24
print(endH, endM, sep=':')
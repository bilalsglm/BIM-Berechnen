
# Schreibe ein Program mit einer Funktion, die zwei übergabeparameter akzeptirt.
# groesa als float
# gewicht als float
# Die Funktion soll den BMI berechnen und ausgeben, ob dei Person untergewicht,
# normalgewicht oder übergewicht hat.

def BMIBerechnen(groese, gewicht):

    bmi = gewicht / (groese * groese)
    bmi = round(bmi,2)

    result = " "

    if bmi <=18.4:
        result = "untergewicht"
    elif 18.4 < bmi < 25:
        result = "normalgewicht"
    elif 25 <= bmi <=29.9:
        result = "übergewicht"
    else :
        result = "du bist krank"
    return result

groese = float(input("Große eingeben:"))
gewicht = float(input("Gewicht eingeben:"))

print(BMIBerechnen(groese, gewicht))

#print(BMIBerechnen(1.60 , 100))




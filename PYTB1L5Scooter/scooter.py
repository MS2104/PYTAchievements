verzekering_per_maand = 23
benzine_kosten_per_liter = 1.54
liter_per_kilometer = 0.2 

def bereken_maandkosten():
    km_per_maand = float(input("Hoeveel kilometers rij je per maand? "))
    maandkosten = (km_per_maand * liter_per_kilometer * benzine_kosten_per_liter) + verzekering_per_maand
    print("De kosten zijn ", maandkosten, ' euro per maand.')

bereken_maandkosten()
import matplotlib.pyplot as plt
summe = 0
feldListe = []

for feld in range(64):
    reiskorn = 2**feld
    feldListe.append(reiskorn)
    summe += reiskorn
    print(f"Feld {feld+1}. = {reiskorn:>27,} Reiskörner und damit insgesamt {summe:>27,} Reiskörner")
gewicht = summe * 0.02 /1000 / 1000          
print()
print("Wenn ein Reiskorn 0.02 Gramm wiegt, wiegen alle "\
      f"Reiskörner zusammen {gewicht:,.0f} Tonnen")
plt.plot(feldListe)
plt.show()      
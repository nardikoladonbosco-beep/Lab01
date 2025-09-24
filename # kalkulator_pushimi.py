# kalkulator_pushimi.py


byrek = int(input("Sa byrekë do të blesh? (≥ 0): "))


leng = int(input("Sa lëngje do të blesh? (≥ 0): "))

karta = input("Ke kartë studenti? (po/jo): ").strip().lower()


cmimi_byrek = 120
cmimi_leng = 80
nën_total = byrek * cmimi_byrek + leng * cmimi_leng


if karta == "po":
    zbritja = nën_total * 0.10
else:
    zbritja = 0


total = nën_total - zbritja


print("\n--- Përmbledhje ---")
print(f"Nën-total: {nën_total:.2f} Lek")
print(f"Zbritja: {zbritja:.2f} Lek")
print(f"Totali për pagesë: {total:.2f} Lek")

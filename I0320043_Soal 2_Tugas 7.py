angka = [ 1,20,43,55,21,56,22,98,7,7,5]
print(angka)

#fungsi maksimum dan minimum
print("Nilai maksimum: ", max(angka))
print("Nilai minimum: ", min(angka))

print("                            ")
#fungsi random
import random
print("Nilai random: ")
print(random.choice(angka))
print(random.choice(angka))
print(random.choice(angka))

print("                             ")
#fungsi sort
angka.sort()
print("Urutan angka yang benar adalah sebagai berikut:\n", angka)
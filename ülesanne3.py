paaris_arv = 0
paaritu_arv = 0

print("5-ga jaguvad arvud 1 kuni 100 koos paaris/paaritu infoga:")

for i in range(1, 101):
if i % 5 == 0:
if i % 2 == 0:
print(f"{i} - paaris")
paaris_arv += 1
else:
print(f"{i} - paaritu")
paaritu_arv += 1

print("\nKokkuvõte:")
print(f"Paaris arvude arv: {paaris_arv}")
print(f"Paaritute arvude arv: {paaritu_arv}")

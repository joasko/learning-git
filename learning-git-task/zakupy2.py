sklepy = {
    "warzywniak": ["marchew", "seler", "rukola"],
    "piekarnia": ["chleb", "pączek", "bułki"]
}
count = 0

for sklep, produkty in sklepy.items():
    count+= len(produkty)
    print(f"Idę do {sklep.capitalize()} i kupuję {str(produkty).title()}")
print(f"W sumie: {count}")
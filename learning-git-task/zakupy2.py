sklepy = {
    "warzywniak": ["marchew", "seler", "rukola"],
    "piekarnia": ["chleb", "pączek", "bułki"],
    "ogrodniczy": ["grabie", "ziemia", "nawóz"]
}
count = 0

for sklep, produkty in sklepy.items():
    count+= len(produkty)
    print(f"Idę do {sklep.capitalize()} i kupuję {str(produkty).title()}")
print(f"W sumie: {count}")

Print("Zakupy wykonane")


Print("sporządzić kolejną listę zakupów na nowy tydzień")
    
 
    

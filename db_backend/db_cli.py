import product_handle as ph
from logger import Logger
Log = Logger("cli")

def menu():
    while True:
        print("[1] Produkt hinzufügen")
        print("[2] Produkt abrufen (GTIN)")
        print("[99] Beenden")
        
        choice = input("Auswahl: ")
        
        if choice == "1":
            gtin = int(input("GTIN: "))
            if ph.check_gtin(gtin):
            
                pro = ph.get_product(int(gtin))
                
                if pro is None:
                    name = input("Name: ")
                    amount = float(input("Menge: "))
                    unit = input("Einheit: ")
                    manufacturer = input("Hersteller: ")
                
                    ph.create_product(gtin, name, amount, unit, manufacturer)
                else:
                    Log.log("Produkt existiert bereits.", "warning")
            else:
                Log.log("Ungültige GTIN.", "warning")
            
        if choice == "2":
            Log.log(ph.get_product(int(input("GTIN: "))))
        
        elif choice == "99":
            break
        
if __name__ == "__main__":
    menu()
    print("Programm beendet.")
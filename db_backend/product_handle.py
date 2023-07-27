import data_handle as dh
from logger import Logger

Log = Logger("product_handle")
db = dh.Database("products")

def create_product(gtin: int, name: str, amount: float, unit: str, manufacturer: str):
    """Fügt ein neues Produkt in die Datenbank ein."""
    if not db.does_exist(str(gtin)):
        product = {
            "name": name,
            "amount": amount,
            "unit": unit,
            "manufacturer": manufacturer,
        }
        
        Log.log(f"Erstelle Produkt '{gtin} - {manufacturer}: {name}'", "info")
        
        db.set(str(gtin), product)
    
    else:
        Log.log(f"Produkt mit GTIN '{gtin}' existiert bereits.", "warning")

def set_product():
    pass

        
def get_product(gtin: int):
    """Holt ein Produkt aus der Datenbank."""
    product = db.get_value(str(gtin))
    if product:
        return product
    else:
        Log.log(f"Produkt mit GTIN '{gtin}' existiert nicht.", "warning")
        return None
    
def check_gtin(gtin: int):
    length = len(str(gtin))
    
    if length == 8:
        return True, "GTIN-8"
    elif length == 12:
        return True, "GTIN-12"
    elif length == 13:
        return True, "GTIN-13"
    elif length == 14:
        return True, "GTIN-14"
    else:
        return False, "Ungültige GTIN-Länge"

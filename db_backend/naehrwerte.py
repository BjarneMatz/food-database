def add(ean: str, fett: str = "", ges_fettsäuren: str = "", kohlenhydrate: str = "", zucker: str = "", ballaststoffe: str = "", eiweiß: str = "", salz: str = "", kcal: str = "", kj: str = ""):
    """Fügt ein neues Produkt in die Datenbank ein."""
    
    product = {
        "fett": fett,
        "ges_fettsäuren": ges_fettsäuren,
        "kohlenhydrate": kohlenhydrate,
        "zucker": zucker,
        "ballaststoffe": ballaststoffe,
        "eiweiß": eiweiß,
        "salz": salz,
        "kcal": kcal,
        "kj": kj
    }
    
    Log.log(f"Erstelle Produkt {ean} - {name}")
    
    db.set(str(ean), product)
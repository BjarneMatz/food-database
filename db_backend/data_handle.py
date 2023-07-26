"""Der Datahandle kümmert sich um die Kommunikation zwischen JSON-Datei und API."""

# Import benötigter Module
import json
from typing import Union, Any
import os

# Pfad Präfix der für die relative Pfadangabe benötigt wird
ROOT_DIR = ""

class Database:
    def __init__(self, database_name: str) -> None:
        #Datenbanknamen an Klasse übergeben
        self.database_name = database_name
        
        #Datenbankpfad erstellen
        self.database_path = f"{ROOT_DIR}databases/{self.database_name}.json"
        
        #Datenbankdatei erstellen, falls nicht vorhanden
        try:
            self._read()
        except FileNotFoundError:
            self._write({})
        
    def _read(self) -> dict:
        """Interne Funktion zum Lesen der Datenbankdatei.
        
        Returns:
            dict: Datenbankinhalt
        """
        with open(self.database_path, "r") as file_data:
            return json.load(file_data)
        
    def _write(self, data: dict) -> None:
        """Interne Funktion zum Schreiben der Datenbankdatei.
        
        Args:
            data (dict): Datenbankinhalt
        """
        with open(self.database_path, "w") as file_data:
            json.dump(data, file_data, indent=4)
        
    def get_value(self, key: str) -> Union[Any, None]:
        """Holt den Wert des gegebenen Schlüssels aus der Datenbank"""
        data = self._read()
        try:
            value = data[key]
        except KeyError:
            value = None
        return value
    
    def set(self, key: str, value: Any) -> None:
        """Fügt ein Schlüssel-Wert-Paar in die Datenbank ein.
        
        Args:
            key (str): Schlüssel
            value (any): Wert
        """
        data = self._read()
        data[key] = value
        self._write(data)
    
    def get_keys(self) -> list:
        """Holt alle Schlüssel aus der Datenbank."""
        keys = self._read().keys()
        return list(keys)
    
    def get_all(self) -> dict:
        """Holt alle Rohdaten aus der Datenbank."""
        return self._read()
    
    def set_all(self, data):
        """Setzt alle Rohdaten in die Datenbank."""
        self._write(data)
    
    def delete_key(self, key: str):
        """Löscht den gegebenen Schlüssel aus der Datenbank."""
        data = self._read()
        try:
            del data[key]
            self._write(data)
        except KeyError:
            raise KeyError(f"Der Schlüssel {key} existiert nicht in der Datenbank.")
        
    def delete_db(self, confirm: bool = False):
        """Löscht die Datenbank-Datei und alle Daten vom System."""
        if confirm:
            os.remove(self.database_path)
        else:
            raise PermissionError("Die Datenbank kann nur mit dem Parameter confirm=True gelöscht werden.")
    
    def does_exist(self, key: str) -> bool:
        """Prüft ob der gegebene Schlüssel in der Datenbank existiert."""
        data = self._read()
        if key in data.keys():
            return True
        else:
            return False
    
        
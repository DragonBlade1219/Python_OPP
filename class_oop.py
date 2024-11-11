# Python Code for FACTORY method 
# it comes under the creational 
# Design Pattern

class FrenchLocalizer:

    """ it simply returns the french version """

    def __init__(self):

        self.translations = {"car": "voiture", 
                             "bike": "bicyclette",
                             "cycle":"cyclette"}

    def localize(self, msg):

        """change the message using translations"""
        return self.translations.get(msg, msg)

class SpanishLocalizer:
    """it simply returns the spanish version"""

    def __init__(self):
        self.translations = {"car": "coche", 
                             "bike": "bicicleta",
                             "cycle":"ciclo"}

    def localize(self, msg):

        """change the message using translations"""
        return self.translations.get(msg, msg)

class EnglishLocalizer:
    """Simply return the same message"""

    def localize(self, msg):
        return msg

def Factory(language="English"):

    """Factory Method"""
    localizers = {
        "French": FrenchLocalizer,
        "English": EnglishLocalizer,
        "Spanish": SpanishLocalizer,
    }

    return localizers[language]()

if __name__ == "__main__":

    french = Factory("French")
    english = Factory("English")
    spanish = Factory("Spanish")

    message = ["car", "bike", "cycle"]

    print(("/"*10) + " - Translations - " + ("/"*10) )

    for msg in message:
        print(("-"*10) + "Translations" + ("-"*10) )
        print("\n")
        print(french.localize(msg))
        print(english.localize(msg))
        print(spanish.localize(msg))

class BankAPI:
    def __init__(self):
        self.card_pin = {}  # {card_number: pin}
        self.card_db = {}  # {card_number: Card}

    def register_card(self, card, pin):
        """Registers a card with a PIN."""
        self.card_pin[card.card_number] = pin
        self.card_db[card.card_number] = card

    def card_registered(self, card_number):
        """Checks if the card is registered."""
        return card_number in self.card_pin

    def verify_pin(self, card, entered_pin):
        """Verifies if the entered PIN is correct for the card."""
        return self.card_pin.get(card.card_number) == entered_pin
    
    def get_card(self, card_number):
        return self.card_db.get(card_number)
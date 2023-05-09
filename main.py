import anki

deck = anki.make_deck("example_deck")
note = anki.make_note("front", "back")
deck.add_note(note)
anki.generate_anki(deck, "output.apkg")

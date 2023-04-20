# Начнем с создания карты
import random


class Card:
    HEARTS = "Hearts"
    DIAMONDS = "Diamonds"
    CLUBS = "Clubs"
    SPADES = "Spades"

    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def __str__(self):
        # TODO-1: метод возвращает строковое представление карты в виде: 10♥ и A♦
        return f'{self.value}{self.__suit_icon_mapping[self.suit]}'

    __suit_icon_mapping = {
        'Diamonds': '\u2666',
        'Hearts': '\u2665',
        'Spades': '\u2660',
        'Clubs': '\u2663'
    }

    def equal_suit(self, other_card) -> bool:
        # TODO-1: метод возвращает True - если масти карт равны или False - если нет
        return self.suit == other_card.suit

    # TODO-1: реализуем новые методы
    __suit_value_mapping = {
        'Spades': 0,
        'Clubs': 1,
        'Diamonds': 2,
        'Hearts': 4
    }
    __suit_mapping = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14
    }

    def __gt__(self, other_card) -> bool:
        if self.value == other_card.value:
            return self.__suit_value_mapping[self.suit] > self.__suit_value_mapping[other_card.suit]
        else:
            return self.__suit_mapping[self.value] > self.__suit_mapping[other_card.value]

    def __lt__(self, other_card) -> bool:
        return not self.__gt__(other_card)


class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
        self.cards = []
        # TODO-1: конструктор добавляет в список self.cards все(52) карты
        for suit in suits:
            for value in values:
                self.cards.append(Card(value, suit))

    def __str__(self):
        # TODO-2: Принцип работы данного метода прописан в 00_task_deck.md
        cards_str = []
        for card in self.cards:
            cards_str.append(str(card))
        return f"cards[{len(self.cards)}]:" + ", ".join(cards_str)

    def draw(self, x) -> list:
        # TODO-1: Принцип работы данного метода прописан в 00_task_deck.md
        hand_deck = self.cards[:x]
        self.cards = self.cards[x:]
        return hand_deck

    def shuffle(self):
        # TODO-2: Принцип работы данного метода прописан в 00_task_deck.md
        #   Подсказка: https://www.w3schools.com/python/ref_random_shuffle.asp
        random.shuffle(self.cards)

    def shift(self, num_card):
        # TODO-1: реализуем новый метод "сдвиг"
        #  Принцип работы: перемещает num_card с верха колоды под низ
        shifted_card = self.cards[:num_card]
        del self.cards[:num_card]
        self.cards.extend(shifted_card)

    def __getitem__(self, index):
        return self.cards[index]

    def __iter__(self):
        self.next_card_index = 0
        return self

    def __next__(self):
        try:
            card = self.cards[self.next_card_index]
        except IndexError:
            raise StopIteration
        self.next_card_index += 1
        return card


card = Card("10", Card.SPADES)
print(card)

deck = Deck()

# 1. Вывод колоды в терминал:
print(deck)  # вместо print(deck.show())
# print(obj) --> str(obj) --> obj.__str__() # magic-method
deck.shuffle()
card1, card2 = deck.draw(2)
# 2. Вывод карты в терминал:
print(card1)  # вместо print(card1.to_str())
#
# 3. Сравнение карт:
if card1 > card2:
    print(f"{card1} больше {card2}")
if card1 < card2:
    print(f"{card1} меньше {card2}")
# obj1 > obj2  -> obj1.__gt__(obj2)
# obj1 < obj2  -> obj1.__lt__(obj2)
# obj1 == obj2  -> obj1.__eq__(obj2)
# 4. Итерация по колоде:
for card in deck:
    print(card)
#
print(deck)
# 5. Просмотр карты в колоде по ее индексу:
print(deck[6])
# obj[index] --> obj.__getitem__(index)

# Список ВСЕХ magic-методов см. тут: http://pythonworld.ru/osnovy/peregruzka-operatorov.html

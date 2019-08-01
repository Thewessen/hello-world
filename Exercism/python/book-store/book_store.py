def disc_group(basket: list) -> iter:
    """Groups sets of unique books in basket."""
    b = basket.copy()
    while len(b) > 0:
        s = set(b)
        yield s
        for book in s:
            b.remove(book)


def price_group(book_set: set) -> int:
    """Calculates the price of a unique set of books."""
    prices = [0, 800, 0.95 * 800, 0.9 * 800, 0.8 * 800, 0.75 * 800]
    total = len(book_set)
    return total * prices[total]


def total(basket: list) -> int:
    """Calculates the total price of a basket of books."""
    price = sum(price_group(book_set)
                for book_set in disc_group(basket))
    # Adjust price for better suited (4+4 iso 5+3) group.
    if len(basket) % 8 == 0:
        price -= 5 * len(basket)
    return price

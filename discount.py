def calculate_discounted_price(price: float, discount_percent: float) -> float:
    """
    Рассчитывает итоговую цену товара с учётом скидки.

    Аргументы:
        price (float): исходная цена товара (должна быть >= 0).
        discount_percent (float): процент скидки (от 0 до 100 включительно).

    Возвращает:
        float: цена со скидкой.

    Исключения:
        ValueError: если цена < 0 или скидка вне диапазона [0, 100].
    """
    if price < 0:
        raise ValueError("Цена не может быть отрицательной")
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Процент скидки должен быть в диапазоне от 0 до 100")

    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    return round(final_price, 2)

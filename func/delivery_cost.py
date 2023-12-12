from typing import Optional


def calculate_delivery_cost(distance: int, dimensions: str, fragile: bool, busy_factor: Optional[str]):
    """
    Расчет стоимости доставки
    :param distance: расстояние до пункта назначения
    :param dimensions: габариты ("large", "small")
    :param fragile: информация о хрупкости
    :param busy_factor: загруженность службы доставки
    :return:
    """
    base_cost = 0

    # Стоимость в зависимости от расстояния
    if distance < 0:
        raise ValueError(f"Передано отрицательное значение расстояния: {distance}")
    elif distance < 2:
        base_cost += 50
    elif distance < 10:
        base_cost += 100
    elif distance < 30:
        base_cost += 200
    else:
        base_cost += 300

    # Стоимость в зависимости от габаритов
    if dimensions == "large":
        base_cost += 200
    else:
        base_cost += 100

    # Стоимость в зависимости от хрупкости груза
    if fragile:
        if distance <= 30:
            base_cost += 300
        else:
            raise Exception("Невозможно доставить груз на расстояние более 30 км")

    # Умножение на коэффициент загруженности
    if busy_factor == "very high busy":
        base_cost *= 1.6
    elif busy_factor == "high busy":
        base_cost *= 1.4
    elif busy_factor == "increased busy":
        base_cost *= 1.2

    # Минимальная стоимость
    if base_cost < 400:
        return 400
    else:
        return int(base_cost)


if __name__ == '__main__':
    print(calculate_delivery_cost(60, "small", False, "very high busy"))


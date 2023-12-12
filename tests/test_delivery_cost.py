import pytest
from func.delivery_cost import calculate_delivery_cost


class TestDeliveryCost:
    """Проверка расчета стоимости доставки"""

    @pytest.mark.parametrize('distance, cost', [(60, 800), (30, 800), (29, 640), (20, 640), (10, 640),
                                                (9, 480), (6, 480), (2, 480), (1, 400)])
    def test_01_check_cost_on_distance(self, distance, cost):
        """Проверка стоимости доставки в зависимости от расстояния"""
        delivery_cost = calculate_delivery_cost(distance, 'large', False, 'very high busy')
        assert delivery_cost == cost, f'Стоимость доставки не равна {cost}'

    @pytest.mark.parametrize('busy_factor, cost', [('very high busy', 800), ('high busy', 700),
                                                  ('increased busy', 600), (None, 500)])
    def test_02_check_cost_on_busy_factor(self, busy_factor, cost):
        """Проверка стоимости доставки в зависимости от загруженности"""
        delivery_cost = calculate_delivery_cost(30, 'large', False, busy_factor)
        assert delivery_cost == cost, f'Стоимость доставки не равна {cost}'

    @pytest.mark.parametrize('dimensions, cost', [('large', 500), ('small', 400)])
    def test_03_check_cost_on_dimensions(self, dimensions, cost):
        """Проверка стоимости доставки в зависимости от габаритов посылки"""
        delivery_cost = calculate_delivery_cost(30, dimensions, False, None)
        assert delivery_cost == cost, f'Стоимость доставки не равна {cost}'

    @pytest.mark.parametrize('fragile, cost', [(True, 700), (False, 400)])
    def test_04_check_cost_on_fragile(self, fragile, cost):
        """Проверка стоимости доставки в зависимости от хрупкости посылки"""
        delivery_cost = calculate_delivery_cost(20, 'large', fragile, None)
        assert delivery_cost == cost, f'Стоимость доставки не равна {cost}'

    def test_05_check_min_cost(self):
        """Проверка расчета минимальной стоимости доставки"""
        delivery_cost = calculate_delivery_cost(1, 'small', False, None)
        assert delivery_cost == 400, f'Стоимость доставки не равна 400'

    def test_06_error_distance(self):
        """Проверка ошибки при отрицательном расстоянии"""
        with pytest.raises(ValueError, match=r"Передано отрицательное значение расстояния"):
            calculate_delivery_cost(-1, 'small', False, None)

    def test_07_error_fragile(self):
        """Проверка ошибки при доставке хрупкого груза дальше 30 км"""
        with pytest.raises(Exception, match=r"Невозможно доставить груз на расстояние более 30 км"):
            calculate_delivery_cost(31, 'small', True, None)
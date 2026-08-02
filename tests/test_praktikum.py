from unittest.mock import patch, MagicMock
from praktikum import praktikum as praktikum_module


def test_main_runs_without_error():
    with patch('praktikum.praktikum.Database') as mock_db_cls, \
         patch('praktikum.praktikum.Burger') as mock_burger_cls, \
         patch('builtins.print') as mock_print:
        mock_db = MagicMock()
        mock_db.available_buns.return_value = [MagicMock()]
        mock_db.available_ingredients.return_value = [MagicMock()] * 6
        mock_db_cls.return_value = mock_db

        mock_burger = MagicMock()
        mock_burger_cls.return_value = mock_burger
        mock_burger.get_receipt.return_value = "test receipt"

        praktikum_module.main()
        mock_print.assert_called_once_with("test receipt")

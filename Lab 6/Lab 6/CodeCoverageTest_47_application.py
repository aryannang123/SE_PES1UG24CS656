
import pytest
from fuel_station import fuel_bill, pump_allowed, session_status


# Fuel bill tests
def test_fuel_bill_regular():
    assert fuel_bill("regular", 20, "silver") == 1050


def test_fuel_bill_diesel():
    assert fuel_bill("diesel", 25, "silver") == 450


def test_fuel_bill_premium_gold():
    assert fuel_bill("premium", 10, "gold") == 0


def test_fuel_bill_unknown_grade():
    with pytest.raises(ValueError):
        fuel_bill("kerosene", 10, "silver")


def test_fuel_bill_negative_litres():
    with pytest.raises(ValueError):
        fuel_bill("regular", -5, "silver")


def test_fuel_bill_gold_diesel():
    assert fuel_bill("diesel", 25, "gold") == 450


def test_fuel_bill_extra_over_30_silver():
    assert fuel_bill("regular", 50, "silver") == 3960


def test_fuel_bill_extra_over_30_gold():
    assert fuel_bill("regular", 50, "gold") == 35 * 95


def test_fuel_bill_diesel_large_extra():
    assert fuel_bill("diesel", 60, "silver") == 40 * 84


# Pump tests
def test_pump_fleet_allowed():
    assert pump_allowed(200, 4, True) is True


def test_pump_fleet_exceeds_limit():
    assert pump_allowed(201, 4, True) is False


def test_pump_non_fleet_allowed():
    assert pump_allowed(50, 1, False) is True


def test_pump_non_fleet_exceeds_limit():
    assert pump_allowed(61, 1, False) is False


def test_pump_multiple_containers():
    assert pump_allowed(50, 2, False) is False


# Session tests
def test_session_card_active():
    assert session_status(60, True, False) == "active"


def test_session_cash_active():
    assert session_status(30, False, False) == "active"


def test_session_night_active():
    assert session_status(90, True, True) == "active"


def test_session_card_warning():
    assert session_status(45, True, False) == "warning"


def test_session_cash_warning():
    assert session_status(15, False, False) == "warning"


def test_session_night_warning():
    assert session_status(75, True, True) == "warning"


def test_session_card_timeout():
    assert session_status(44, True, False) == "timed_out"


def test_session_cash_timeout():
    assert session_status(14, False, False) == "timed_out"


def test_session_night_timeout():
    assert session_status(74, True, True) == "timed_out"

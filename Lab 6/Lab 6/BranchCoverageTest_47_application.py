
import pytest
from fuel_station import fuel_bill, pump_allowed, session_status


def test_fuel_bill_all_grade_and_validation_branches():
    with pytest.raises(ValueError):
        fuel_bill("kerosene", 10, "silver")
    with pytest.raises(ValueError):
        fuel_bill("regular", -2, "silver")


def test_fuel_bill_gold_non_diesel_and_no_extra():
    assert fuel_bill("regular", 15, "gold") == 0


def test_fuel_bill_silver_regular_extra_not_over_30():
    assert fuel_bill("regular", 20, "silver") == 1050


def test_fuel_bill_diesel_rate():
    assert fuel_bill("diesel", 25, "silver") == 450


def test_fuel_bill_large_extra_silver_discount():
    assert fuel_bill("premium", 50, "silver") == 35 * 99


def test_fuel_bill_large_extra_gold_discount():
    assert fuel_bill("regular", 50, "gold") == 35 * 95


def test_fuel_bill_gold_diesel():
    assert fuel_bill("diesel", 21, "gold") == 90


def test_pump_allowed_fleet():
    assert pump_allowed(200, 4, True) is True
    assert pump_allowed(201, 1, True) is False


def test_pump_allowed_non_fleet_limit():
    assert pump_allowed(60, 1, False) is True
    assert pump_allowed(61, 1, False) is False


def test_pump_allowed_containers():
    assert pump_allowed(30, 1, False) is True
    assert pump_allowed(30, 2, False) is False


def test_session_status_cutoffs():
    assert session_status(60, True, False) == "active"
    assert session_status(30, False, False) == "active"


def test_session_status_night_cutoff():
    assert session_status(90, True, True) == "active"
    assert session_status(60, False, True) == "active"


def test_session_status_warning():
    assert session_status(45, True, False) == "warning"
    assert session_status(15, False, False) == "warning"


def test_session_status_timed_out():
    assert session_status(44, True, False) == "timed_out"
    assert session_status(14, False, False) == "timed_out"


def test_session_status_night_warning_and_timeout():
    assert session_status(75, True, True) == "warning"
    assert session_status(74, True, True) == "timed_out"
    assert session_status(44, True, True) == "timed_out"


from hypothesis import given, strategies as st
from fuel_station import parse_purchase, volume_average, payable_bill


# Test parse_purchase with random strings and None
@given(st.text() | st.none())
def test_parse_purchase_no_crash(s):
    try:
        result = parse_purchase(s)
        assert result is None or (
            isinstance(result, tuple)
            and len(result) == 2
        )
    except Exception as e:
        assert False, f"parse_purchase crashed with {s!r}: {e}"


# Test volume_average with random strings and None
@given(st.text() | st.none())
def test_volume_average_no_crash(s):
    try:
        result = volume_average(s)
        assert result is None or isinstance(result, int)
    except Exception as e:
        assert False, f"volume_average crashed with {s!r}: {e}"


# Test payable_bill with random strings and None
@given(st.text() | st.none())
def test_payable_bill_no_crash(s):
    try:
        result = payable_bill(s)
        assert result is None or isinstance(result, float)
    except Exception as e:
        assert False, f"payable_bill crashed with {s!r}: {e}"

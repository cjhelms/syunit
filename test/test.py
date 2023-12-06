from syunit.unit import Meters, Seconds, Divide


def test_meters_divided_by_seconds_returns_value_in_meters_per_second():
    m = Meters(8.0)
    s = Seconds(2.0)
    expected_result = 4.0
    result = m / s
    assert float(result) == expected_result
    assert type(result) == Divide[Meters, Seconds]

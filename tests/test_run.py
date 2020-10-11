from run import convert_case_sensitive_argument


def test_convert_case_sensitive_argument():
    """Test if the possible values for the case_sensitive parameter return the proper value."""
    expected_outcomes = {
        "0": False,
        "false": False,
        "False": False,
        "no": False,
        "n": False,
        "1": True,
        "true": True,
        "True": True,
        "yes": True,
        "y": True
    }
    for parameter_val, expected_output in expected_outcomes.items():
        received_output = convert_case_sensitive_argument(parameter_val)
        assert expected_output == received_output

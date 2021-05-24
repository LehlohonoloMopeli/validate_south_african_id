from validate_sa_id.validate_id.validate_sa_id import ValidateSouthAfricanID

        
def test_is_id_valid():
    assert ValidateSouthAfricanID("9904285394080", "Male", "South Africa").is_id_number_valid() == "ID is valid!"
    assert ValidateSouthAfricanID("2001014800086", "Female", "South Africa").is_id_number_valid() == "ID is valid!"
    assert ValidateSouthAfricanID("9904285394080", "Female", "South Africa").is_id_number_valid() == "Invalid ID!"
    assert ValidateSouthAfricanID("990428539408", "Male", "South Africa").is_id_number_valid() == "Invalid ID!"
    assert ValidateSouthAfricanID("99A428539408Z", "Male", "South Africa").is_id_number_valid() == "Invalid ID!"
    assert ValidateSouthAfricanID("9904335394080", "Male", "South Africa").is_id_number_valid() == "Invalid ID!"
    assert ValidateSouthAfricanID("9904285394080", "Male", "Namibia").is_id_number_valid() == "Invalid ID!"
    assert ValidateSouthAfricanID("9904285394088", "Male", "South Africa").is_id_number_valid() == "Invalid ID!"

    
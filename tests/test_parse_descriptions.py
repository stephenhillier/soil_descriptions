import pytest
from soil_descriptions import Description, parse_description


@pytest.mark.parametrize("original, expected", [
    ("wet gravel", Description(original="wet gravel", primary="gravel",
                               moisture="wet", ordered=["gravel"])),
    ("compact silty sand, some clay, wet", Description(original="compact silty sand, some clay, wet", primary="sand", secondary="silt",
                                                       consistency="compact", moisture="wet", ordered=["sand", "silt", "clay"])),
    ("water bearing sands, trace gravel, loose", Description(original="water bearing sands, trace gravel, loose", primary="sand",
                                                             secondary="gravel", consistency="loose", moisture="wet", ordered=["sand", "gravel"])),

    # note: this is a poor description.  silty should come last.  here we just make sure it is handled as if silty came after gravel
    ("silty sand and gravel", Description(original="silty sand and gravel", primary="sand",
                                          secondary="gravel", ordered=["sand", "gravel", "silt"])),
    ("sand and gravel, silty", Description(original="sand and gravel, silty", primary="sand",
                                           secondary="gravel", ordered=["sand", "gravel", "silt"])),

])
def test_parse_description(original, expected):
    parsed = parse_description(original)
    assert parsed.primary == expected.primary

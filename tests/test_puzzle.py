import unittest.mock
from unittest.mock import Mock
import pytest
import random
from typing import Any, Dict, List, Tuple

from puzzle import check


API_TOKEN = 'a_token_string'


@pytest.mark.parametrize('puzzle', [
    {
        "data": ["qwer", "asdf", "zcvf", "erty", "jhgf", "polk", "gthu", "uhgt"],
        "chunkSize": 4,
        "length": 32
    },
    {
        "data": ["f319", "46ec", "c1c7", "3720", "c7df", "c4ea", "4e3e", "80fd"],
        "chunkSize": 4,
        "length": 32
    },
    {
        "data": [
            "9aMLoJMDZYpfjniRvW1kTRPpagSGHkkSVqVTUGXBA5ZrbXsFtau9hKSHhygNAEGXdW6SNRXuZcbQhpAkfCBmFI2gWnpxLpsG4cOn",
            "rFvzVSMriWbzCVcwFzHH2rXO1UgfqWsbQpSxZqeSqW0oBm9voRKhvpYs9zhLHSmlZXA458RDR3uohy14my9Gwy57UTDS06yEQMet",
            "7L4C13DJsxai8KdpNe2P9Iw5IgAX9BOqe48Hui9ab4ZFrQVox15WiD69TFHh38O6DJOpjcWC5hYnI3UnsAoadMyG9MtP2rYEoizI",
            "V6fenVSeFntA3tWj476OZnKey0mDLA2ReOvNQfboUiJQv6rs66MOWw0c0NnoHufoSOcgD0BDqTvtbMERM4wCcMYBsdXwzNK2cUmp",
            "gNIIkMmL1Qnq0j9FPgrfo3BzlGJKRYwJ0UOyWELlpbM0Tx7qXa2o1E911lZrkp7S65afSKcLWFJBh8cVlXEEL9CD0y4MkIhhtCN1",
            "rvJ36RFMnNjvIUiAkCFUzJNrykOU2RvFQx7NlYuCGeLmUiTzaiIEf2YVUA7qC5Tela1rf70zO7F9BIZI0QeQooGgjhjkMNkWIpvv",
            "ulU4lYsagzMUJSccMowaF4X1IwqZIoUFUGL3yTZTJKOGNMoEd64ItNNjraUvzVyWMrkWGDhcFcCEetpVXgBA84GYqD6DB4ycbjWk",
            "YGLyUMfy7EqMZESHTl2yLHYZDPw0Gx6gdF2a6C5RuJDfnDLaAPqRsq44lNgxtozuvew60d5U9mqcMPyGjweHtZgLhRvsHd4l2ci1",
            "G6wyVR7aWboqPtqMhpRZjii2pBfe5uuBfpvex4fAsr4JTtWxNfxa5Jgev9wEq9HtyEJgC6BdgYFz4zUQaeZbKRgqytpBnvXrWa7a"
        ],
        "chunkSize":100,
        "length":900
    },
    {
        "data": [
            "eJdYk6olWJB1oa3ra88KMK0POGVD1WO920WI16kXq5TXaNlO7Wgv6NGEnBu4Uq6lmg6XYTnoo7Zpzy4nc1RJAafWqJdR8pw0BVQG",
            "A3QEVz9jWlXtZGuh0rrD5rj6Bqqn0aYa5XNtvcISmbngdNuAEqHq4wZus9VsUxHCDl5FzwGU62kz4BKmzq7lxEuXZUKeQUrAqvVo",
            "FsX2vWTKWwS2qDiSkFpV11PCzifHouYqHHZLzkEknWdj4Jc4hH3URkaxYztM6TIFIK92IZ9uxxjdVehram90jKSqjmtBeb66QWxO",
            "WcSvf7ZilgfwrodeVZ2SLtbNGtjFjRBE1tL8GX0kIJmPLXxNB6dAmTcHuzCLcrWyAowrECCbT5wIe777ejP2Ool0BQIzBd0kT11r",
            "D1Rt5sV9jELFE62uWjoKsXSwyizVC1xfu4WMbP8F614b12rshAjKnRTmlSE0tBRQijenV3HbjeQmw5z8bV9ARytLQZXSQ5QznVoG",
            "xqO41N89VPXBCvjIpHBrLdvgWZEN9uTVFS6L4HvLrMqhkVMDd9KO5jSzOe8kt6DHgBZSvxglHsqUoF0rosOI72vnPZ1AEI7MQQEh",
            "noqrAF1cu1nmtqGOExD8fIeWyxX3ShTMmUvbrBqhLTEZFHSJjPsHyko8YnuVRlx2l8J2C9g0nZVXW3dVlg46fqZhLMzlq27NlfqS",
            "vs48543Sh5bjpzDtCqrO54GRhKCe3SbSmFe4o75MXS5SGyq2HsVUCry74Lko8T5n2X4hcadXVOeoAsfkSSdDu3mGGTaMtyGyVaEG",
            "BAjC6GSZRaLUuoGWmfj3CdIpPETIQqwFFoYiWioHVobmAknXwgQCRucXSRvdpDawUSB1lBFrJM6RMnQKjoanp7l2QKjyXl8RjUKB"
        ],
        "chunkSize":100,
        "length":900
    }
])
def test_check(puzzle: Dict[str, Any], mocker: unittest.mock):
    """
        UnitTest: check method from puzzle module
            It assumes {puzzle} samples are ordered so it shuffles
            each them before battletesting the method
    """
    data: List[str] = puzzle['data']
    shuffled_data = data[1:].copy()
    random.shuffle(shuffled_data)
    shuffled_data = [data[0]] + shuffled_data
    # print('Input', shuffled_data)
    # shuffled_data = data.copy()
    assert len(shuffled_data) == len(data)
    assert shuffled_data[0] == data[0] # Assumption: 1st element is always in-place

    def mock_block_checker(*args, **kwargs) -> Dict[str, bool]:
        """
            Mocks the API check blocks endpoint
        """
        json_data = kwargs['json']
        # print(data)
        # print(json_data)
        pair: Tuple[str, str] = json_data['blocks']
        return Mock(ok=True, json=lambda: {
            'message': data.index(pair[1]) - data.index(pair[0]) == 1
        })

    mock_api = mocker.patch('api.requests.post')
    mock_api.side_effect = mock_block_checker
    ordered_blocks = check(shuffled_data.copy(), API_TOKEN)
    assert data == ordered_blocks


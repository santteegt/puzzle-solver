import pytest
from typing import Any, Dict
import unittest.mock

from api import BASE_URL
from  api import fetch_api_key, fetch_puzzle_by_email
from api import check_blocks, check_puzzle


EMAIL = 'mail@mail.com'
API_TOKEN = 'a_token_string'


def test_fetch_api_key(mocker: unittest.mock):
    """
        UnitTest: fetch_api_key by email
    """
    mock_api = mocker.patch('api.get_api', return_value={'token': API_TOKEN})
    api_token = fetch_api_key(email=EMAIL)
    assert api_token == API_TOKEN


@pytest.mark.parametrize('sample_data', [
    {
        "data": ["qwer", "asdf", "zcvf", "erty", "jhgf", "polk", "gthu", "uhgt"],
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
    }
])
def test_fetch_puzzle_by_email(sample_data: Dict[str, Any], mocker: unittest.mock):
    """
        UnitTest: fetch_puzzle_by_email
            Mocks puzzle requests as {sample_data}
    """
    mock_api_key = mocker.patch('api.fetch_api_key', return_value=API_TOKEN)
    mock_api = mocker.patch('api.get_api', return_value=sample_data)
    puzzle = fetch_puzzle_by_email(email=EMAIL)
    mock_api_key.assert_called_once_with(EMAIL)
    mock_api.assert_called_once_with('blocks', params={'token': API_TOKEN})
    assert 'chunkSize' in puzzle
    assert type(puzzle['chunkSize']) == int
    assert 'length' in puzzle
    assert type(puzzle['length']) == int
    assert 'data' in puzzle
    assert type(puzzle['data']) == list
    assert len(puzzle['data']) == puzzle['length'] / puzzle['chunkSize']
    assert 'api_token' in puzzle
    assert puzzle['api_token'] == API_TOKEN


def test_check_blocks(mocker: unittest.mock):
    """
        UnitTest: tests check_blocks endpoint
    """
    sample_pair = ('abc' 'def')
    mock_api = mocker.patch('api.post_api', return_value={'message': False})
    together = check_blocks(sample_pair, API_TOKEN)
    mock_api.assert_called_once_with(
        'check',
        json_data={'blocks': list(sample_pair)},
        params={'token': API_TOKEN},
    )
    assert together == False


def test_check_blocks_failed_request(mocker: unittest.mock):
    """
        UnitTest: test check blockd endpoint with call exception
    """
    sample_pair = ('abc' 'def')
    mock_requests = mocker.patch('api.requests.post')
    mock_requests.return_value.ok = False
    with pytest.raises(Exception, match=r'Failed to check blocks'):
        check_blocks(sample_pair, API_TOKEN)


def test_check_blocks_maximum_requests(mocker: unittest.mock):
    """
        UnitTest: test exception if maximum No of requests is reached
    """
    sample_pair = ('abc' 'def')
    mock_requests = mocker.patch('api.requests.post')
    mock_requests.return_value.ok = False
    mock_requests.return_value.status_code = 429
    with pytest.raises(Exception, match=r'Maximum # of requests reached!'):
        check_blocks(sample_pair, API_TOKEN)


def test_check_puzzle(mocker: unittest.mock):
    """
        UnitTest: test check_encoded puzzle endpoint
    """
    answer = 'a sorted puzzle'
    mock_requests = mocker.patch('api.requests.post')
    mock_requests.return_value.ok = True
    mock_requests.return_value.json = lambda: {'message': True}
    solved = check_puzzle(answer, API_TOKEN)
    mock_requests.assert_called_once_with(
        f'{BASE_URL}/check',
        json={'encoded': answer},
        params={'token': API_TOKEN},
    )
    assert solved == True


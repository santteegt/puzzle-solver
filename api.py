
import logging
import requests
from typing import Any, Dict, Tuple, Union


BASE_URL = 'https://rooftop-career-switch.herokuapp.com'
REQ_COUNTER = 0


def counter():
    """
        Global Counter variable
    """
    global REQ_COUNTER
    REQ_COUNTER += 1


def get_api(endpoint: str, params: Dict[str, str]) -> Dict[str, Any]:
    """
        GET API
    """
    rs = requests.get(f'{BASE_URL}/{endpoint}', params=params)
    # counter()
    if rs.ok:
        return rs.json()
    else:
        logging.info(f'Failed to fetch API Token: {rs.reason}')


def post_api(endpoint: str, json_data: Dict, params: Union[Dict[str, str], None]=None) -> Dict[str, Any]:
    """
        POST API
    """
    rs = requests.post(f'{BASE_URL}/{endpoint}', json=json_data, params=params)
    counter()
    if rs.ok:
        return rs.json()
    if rs.status_code == 429:
        logging.info('Reahed maximum # of requests!')
        raise Exception('Maximum # of requests reached!')
    else:
        logging.info(f'Failed to fetch API Token: {rs.reason}')


def fetch_api_key(email: str) -> str:
    """
        Fetch API Key by {email}
    """
    data = get_api('token', {'email': email})
    return data['token'] if data is not None else ''


def fetch_puzzle_by_email(email: str) -> Dict[str, Any]:
    """
        Fetch a Puzzle from the API by {email}
    """
    api_token = fetch_api_key(email)
    if api_token is not None:
        data = get_api('blocks', params={'token': api_token})
        data['api_token'] = api_token
        return data

    raise Exception('Something went wrong. Check the Logs')


def check_blocks(pair: Tuple[str, str], api_token: str) -> bool:
    """
        Checks if two puzzle blocks are together
    """
    data = post_api('check', json_data={'blocks': list(pair)}, params={'token': api_token})
    if data is not None:
        return bool(data['message'])
    
    raise Exception('Failed to check blocks. Check the Logs')


def check_puzzle(puzzle: str, api_token: str) -> bool:
    """
        Verify if a puzzle was solved correctly
    """
    data = post_api('check', json_data={'encoded': puzzle}, params={'token': api_token})
    if data is not None:
        return bool(data['message'])
    
    raise Exception('Failed to verify puzzle. Check the Logs')


def request_counter() -> int:
    """
        Stats function to return the total No of requests used by a puzzle solver
    """
    global REQ_COUNTER
    return REQ_COUNTER


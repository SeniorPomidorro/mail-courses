import pytest


def make_list(a):
    return a.split(',')


def update_dict(a, b):
    a.update(b)
    return a


@pytest.mark.parametrize('test_input, expected',
                         [('a,b,c,d', ['a', 'b', 'c', 'd']), ('aaa', ['aaa']),
                          ('Hello, World!', ['Hello', ' World!'])])
def test_make_list(test_input, expected):
    assert make_list(test_input) == expected


def test_make_list_error():
    try:
        assert make_list({'a', 1})
    except AttributeError:
        pass


def test_make_list_type():
    assert isinstance(make_list('aaa'), list)


@pytest.mark.parametrize('test_input1, test_input2, expected',
                         [({'a': 1}, {'b': 2}, {'a': 1, 'b': 2}),
                          ({'a': 1, 'b': 'b'}, {'d': -111}, {'a': 1, 'b': 'b', 'd': -111}),
                          ({'a': 1}, {'a': 2}, {'a': 2})])
def test_update_dict(test_input1, test_input2, expected):
    assert update_dict(test_input1, test_input2) == expected


def test_update_dict_error():
    try:
        assert update_dict({'a', 1}, 2)
    except TypeError:
        pass


def test_update_dict_type():
    assert isinstance(update_dict({'a': 1}, {'a': -5451}), dict)


import random

import pytest

from base.exceptions import NullElementException

from stacks.stack import Stack


@pytest.fixture()
def stack():
    data_structure = Stack()
    yield data_structure
    data_structure = None


@pytest.fixture()
def none_data():
    return None


@pytest.fixture()
def static_data():
    return 1401


@pytest.fixture()
def dynamic_data():
    return random.randint(1, 1000)


# test adding an item to the stack

def test_add_a_none_element_to_stack(stack: Stack, none_data):
    with pytest.raises(NullElementException):
        stack.push(none_data)


def test_add_an_item_to_stack(stack: Stack, static_data):
    assert stack.push(static_data) == static_data


def test_add_an_zero_value_to_stack(stack: Stack):
    assert stack.push(0) == 0


# test getting length of the stack

def test_get_length_of_a_empty_stack(stack: Stack):
    assert stack.size() == 0


def test_get_length_of_a_non_empty_stack(stack: Stack, dynamic_data, static_data):
    # Arrange
    stack.push(dynamic_data)
    stack.push(static_data)

    # Act
    length = stack.size()

    # Assert
    assert length == 2
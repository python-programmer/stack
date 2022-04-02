import random

import pytest

from base.exceptions import NullElementException, EmptyStackException

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


# testing add an item to the stack

def test_add_a_none_element_to_stack(stack: Stack, none_data):
    # Act, Assert
    with pytest.raises(NullElementException):
        stack.push(none_data)


def test_add_an_item_to_stack(stack: Stack, static_data):
    # Act, Assert
    assert stack.push(static_data) == static_data


def test_add_an_zero_value_to_stack(stack: Stack):
    assert stack.push(0) == 0


# testing get length of the stack

def test_get_length_of_a_empty_stack(stack: Stack):
    # Act, Assert
    assert stack.size() == 0


def test_get_length_of_a_non_empty_stack(stack: Stack, dynamic_data, static_data):
    # Arrange
    stack.push(dynamic_data)
    stack.push(static_data)

    # Act
    length = stack.size()

    # Assert
    assert length == 2


# testing pop an item from the stack

def test_pop_from_empty_stack(stack: Stack):
    # Act, Assert
    with pytest.raises(EmptyStackException):
        stack.pop()


def test_pop_from_stack(stack: Stack, dynamic_data, static_data):
     # Arrange
    stack.push(dynamic_data)
    stack.push(static_data)

    # Act
    data = stack.pop()
    length = stack.size()

    # Assert
    assert length == 1
    assert data == static_data


# testing peek an item from the stack

def test_peek_from_empty_stack(stack: Stack):
    # Act, Assert
    with pytest.raises(EmptyStackException):
        stack.pop()


def test_peek_from_stack(stack: Stack, dynamic_data, static_data):
     # Arrange
    stack.push(dynamic_data)
    stack.push(static_data)

    # Act
    data = stack.peek()
    length = stack.size()

    # Assert
    assert length == 2
    assert data == static_data


# testing empty stack

def test_check_empty_stack(stack: Stack):
    # Act, Assert
    assert stack.empty()


def test_check_none_empty_stack(stack: Stack, dynamic_data, static_data):
     # Arrange
    stack.push(dynamic_data)
    stack.push(static_data)

    # Act
    is_empty = stack.empty()
    length = stack.size()

    # Assert
    assert length == 2
    assert is_empty == False

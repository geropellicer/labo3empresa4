import math
from empresa4.core import (
    calculate_error,
    get_clientes_importantes,
    get_productos_importantes,
    filter_clientes_importantes,
)
from empresa4.datasets import get_dataset

def test_calculate_error():
    predicted = [1, 2, 3, 4, 5]
    real_values = [1, 2, 3, 4, 5]
    expected_error = 0
    assert math.isclose(
        calculate_error(predicted, real_values), expected_error, rel_tol=1e-9
    )

    predicted = [1, 2, 3, 4, 5]
    real_values = [2, 4, 6, 8, 10]
    expected_error = 0.5
    assert math.isclose(
        calculate_error(predicted, real_values), expected_error, rel_tol=1e-9
    )

    predicted = [1, 2, 3, 4, 5]
    real_values = [0.5, 1, 1.5, 2, 2.5]
    expected_error = 1
    assert math.isclose(
        calculate_error(predicted, real_values), expected_error, rel_tol=1e-9
    )

    predicted = [10, 100, 10, 100, 10]
    real_values = [15, 150, 15, 150, 15]
    expected_error = 0.3333333333333333
    assert math.isclose(
        calculate_error(predicted, real_values), expected_error, rel_tol=1e-9
    )


def test_get_clientes_importantes():
    assert len(get_clientes_importantes()) == 12


def test_get_productos_importantes():
    assert len(get_productos_importantes()) == 10

def test_filter_clientes_importantes():
    # Load the original dataset
    df = get_dataset("01_original")

    # Filter the dataset using the function
    filtered_df = filter_clientes_importantes(df)

    # Check that the length of unique customer_id values is 12
    assert len(filtered_df["customer_id"].unique()) == 12

    # Check that all customer_id values are in get_clientes_importantes
    assert all(
        customer_id in get_clientes_importantes() for customer_id in filtered_df["customer_id"].unique()
    )
    
def test_filter_productos_importantes():
    # Load the original dataset
    df = get_dataset("01_original")

    # Filter the dataset using the function
    filtered_df = filter_productos_importantes(df)

    # Check that the length of unique id_producto values is 10
    assert len(filtered_df["id_producto"].unique()) == 10

    # Check that all id_producto values are in get_productos_importantes
    assert all(
        id_producto in get_productos_importantes() for id_producto in filtered_df["id_producto"].unique()
    )
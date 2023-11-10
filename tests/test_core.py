import math
from empresa4.core import (
    calculate_error,
    calculate_error_2,
    get_clientes_importantes,
    get_productos_importantes,
    filter_clientes_importantes,
    filter_productos_importantes,
)
from empresa4.datasets import get_dataset
import pandas as pd
import pkg_resources


def test_calculate_error_2():
    filepath = pkg_resources.resource_filename(
        "tests", "calculate_error_2_test_data.csv"
    )
    df = pd.read_csv(filepath)
    prediction_1 = calculate_error(
        df["prediction"].to_list(), df["actual_tn_for_201904"].to_list()
    )
    prediction_2 = calculate_error_2(df, 201904)
    assert math.isclose(prediction_1, prediction_2, rel_tol=1e-9)

    rows = [
        {"product_id": 20001, "prediction": 1647.6384799999998},
        {"product_id": 20002, "prediction": 1287.62346},
        {"product_id": 20003, "prediction": 565.33774},
        {"product_id": 20004, "prediction": 466.70901},
        {"product_id": 20005, "prediction": 624.9988},
        {"product_id": 20006, "prediction": 835.47883},
        {"product_id": 20007, "prediction": 511.54995},
        {"product_id": 20008, "prediction": 403.69191},
    ]
    df_2 = pd.DataFrame(rows)
    prediction_3 = calculate_error_2(df_2, 201904)
    assert math.isclose(prediction_3, 0.0, rel_tol=1e-9)

    df_3 = pd.DataFrame(rows)
    df_3["prediction"] = df_3["prediction"] / 2
    prediction_4 = calculate_error_2(df_3, 201904)
    assert math.isclose(prediction_4, 0.5, rel_tol=1e-9)

def test_calculate_error_2_raises_exceptions():
    rows = [
        {"product_id": 20001, "prediction": 1647.6384799999998},
        {"product_id": 20002, "prediction": 1287.62346},
        {"product_id": 20003, "prediction": 565.33774},
        {"product_id": 20004, "prediction": 466.70901},
        {"product_id": 20005, "prediction": 624.9988},
        {"product_id": 20006, "prediction": 835.47883},
        {"product_id": 20007, "prediction": 511.54995},
        {"product_id": 20008, "prediction": 403.69191},
    ]
    df = pd.DataFrame(rows)
    df.rename(columns={"prediction": "prediction_2"}, inplace=True)
    # assert that this raises a ValueError
    try:
        calculate_error_2(df, 201904)
        assert False
    except ValueError:
        assert True

    df_2 = pd.DataFrame(rows)
    df_2.rename(columns={"product_id": "product_id_2"}, inplace=True)
    try:
        calculate_error_2(df, 201904)
        assert False
    except ValueError:
        assert True

    df_3 = pd.DataFrame(rows)
    df_3 = pd.concat([df_3, df_3])
    try:
        calculate_error_2(df, 201904)
        assert False
    except ValueError:
        assert True



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
        customer_id in get_clientes_importantes()
        for customer_id in filtered_df["customer_id"].unique()
    )


def test_filter_productos_importantes():
    # Load the original dataset
    df = get_dataset("01_original")

    # Filter the dataset using the function
    filtered_df = filter_productos_importantes(df)

    # Check that the length of unique id_producto values is 10
    assert len(filtered_df["product_id"].unique()) == 10

    # Check that all id_producto values are in get_productos_importantes
    assert all(
        id_producto in get_productos_importantes()
        for id_producto in filtered_df["product_id"].unique()
    )

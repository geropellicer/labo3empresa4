import pandas as pd
from empresa4.datasets import get_dataset, nombres_datasets


def test_get_dataset_01_producto_estrella():
    expected_columns = [
        "periodo",
        "product_id",
        "cust_request_qty",
        "cust_request_tn",
        "tn",
        "product_category",
    ]
    expected_shape = (36, len(expected_columns))
    dataset_name = "01_producto_estrella"
    df = get_dataset(dataset_name)
    assert isinstance(df, pd.DataFrame)
    assert set(df.columns) == set(expected_columns)
    assert df.shape == expected_shape


def test_get_dataset_01_productos_todos():
    expected_columns = [
        "periodo",
        "product_id",
        "cust_request_qty",
        "cust_request_tn",
        "tn",
        "product_category",
    ]
    expected_shape = (31243, len(expected_columns))
    dataset_name = "01_productos_todos"
    df = get_dataset(dataset_name)
    assert isinstance(df, pd.DataFrame)
    assert set(df.columns) == set(expected_columns)
    assert df.shape == expected_shape


def test_get_dataset_01_por_cliente():
    expected_columns = [
        "periodo",
        "customer_id",
        "cust_request_qty",
        "cust_request_tn",
        "tn",
    ]
    expected_shape = (16492, len(expected_columns))
    dataset_name = "01_por_cliente"
    df = get_dataset(dataset_name)
    assert isinstance(df, pd.DataFrame)
    assert set(df.columns) == set(expected_columns)
    assert df.shape == expected_shape

    # get the dataset 01_original, the the unique values of the column customer_id and compare with the unique values of the column customer_id of the dataset 01_por_cliente
    df_original = get_dataset("01_original")
    assert set(df_original["customer_id"].unique()) == set(df["customer_id"].unique())


def test_get_dataset_01_original():
    expected_columns = [
        "periodo",
        "customer_id",
        "product_id",
        "cust_request_qty",
        "cust_request_tn",
        "tn",
    ]
    expected_shape = (2945818, len(expected_columns))
    dataset_name = "01_original"
    df = get_dataset(dataset_name)
    assert isinstance(df, pd.DataFrame)
    assert set(df.columns) == set(expected_columns)
    assert df.shape == expected_shape


def test_get_dataset_maestro_productos():
    expected_columns = ["cat1", "cat2", "cat3", "brand", "sku_size", "product_id"]
    expected_shape = (1251, len(expected_columns))
    dataset_name = "maestro_productos"
    df = get_dataset(dataset_name)
    assert isinstance(df, pd.DataFrame)
    assert set(df.columns) == set(expected_columns)
    assert df.shape == expected_shape


def test_get_dataset_raises_exception():
    dataset_name = "invalid_dataset_name"
    try:
        get_dataset(dataset_name)
    except ValueError as e:
        assert (
            str(e)
            == f"Dataset not found. Usar uno de los siguientes: {nombres_datasets}"
        )


# test that each of the columns "cust_request_qty", "cust_request_tn" and "tn" sums the same in each of the datasets 01_por_cliente, 01_productos_todos and 01_original
def test_columns_sum():
    datasets = ["01_original", "01_por_cliente", "01_productos_todos"] 
    columns = ["cust_request_qty", "cust_request_tn", "tn"]
    dfs = [get_dataset(dataset) for dataset in datasets]

    #597 1233 36
    assert dfs[1]["customer_id"].nunique() == 597
    assert dfs[0]["product_id"].nunique() == 1233
    assert dfs[2]["product_id"].nunique() == 1233
    assert dfs[0]["periodo"].nunique() == 36
    assert dfs[1]["periodo"].nunique() == 36
    assert dfs[2]["periodo"].nunique() == 36


    # 6329834.0 1353074.0208099994 1324988.5884099994
    for column in columns:
        print(column)
        assert (
            round(dfs[0][column].sum(), 2)
            == round(dfs[1][column].sum(), 2)
            == round(dfs[2][column].sum(), 2)
        )

import pandas as pd
from empresa4.datasets import get_dataset, nombres_datasets
from empresa4.core import get_clientes_importantes, get_productos_importantes


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
    expected_rows = 46656
    expected_shape = (expected_rows, len(expected_columns))
    assert expected_rows % 36 == 0
    dataset_name = "01_productos_todos"
    df = get_dataset(dataset_name)
    assert isinstance(df, pd.DataFrame)
    assert set(df.columns) == set(expected_columns)
    assert df.shape == expected_shape


def test_get_dataset_01_120():
    expected_columns = [
        "periodo",
        "customer_id",
        "product_id",
        "cust_request_qty",
        "cust_request_tn",
        "tn",
        "product_category",
    ]
    expected_rows = 120 * 36
    expected_shape = (expected_rows, len(expected_columns))
    assert expected_rows % 36 == 0
    dataset_name = "01_120"
    df = get_dataset(dataset_name)
    assert isinstance(df, pd.DataFrame)
    assert set(df.columns) == set(expected_columns)
    assert df.shape == expected_shape

    assert set(df["customer_id"].unique()) == set(get_clientes_importantes())
    assert set(df["product_id"].unique()) == set(get_productos_importantes())


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

def test_get_dataset_02_producto_estrella():
    expected_columns = [
        "periodo",
        "product_id",
        "cust_request_qty",
        "cust_request_tn",
        "tn",
        "product_category",
        "cat2",
        "sku_size",
        "plan_precios_cuidados"
    ]
    expected_shape = (36, len(expected_columns))
    dataset_name = "02_producto_estrella"
    df = get_dataset(dataset_name)
    assert isinstance(df, pd.DataFrame)
    assert set(df.columns) == set(expected_columns)
    assert df.shape == expected_shape


def test_get_dataset_02_productos_todos():
    expected_columns = [
        "periodo",
        "product_id",
        "cust_request_qty",
        "cust_request_tn",
        "tn",
        "product_category",
        "cat2",
        "sku_size",
        "plan_precios_cuidados"
    ]
    expected_rows = 46656
    expected_shape = (expected_rows, len(expected_columns))
    assert expected_rows % 36 == 0
    dataset_name = "02_productos_todos"
    df = get_dataset(dataset_name)
    assert isinstance(df, pd.DataFrame)
    assert set(df.columns) == set(expected_columns)
    assert df.shape == expected_shape


def test_get_dataset_02_120():
    expected_columns = [
        "periodo",
        "customer_id",
        "product_id",
        "cust_request_qty",
        "cust_request_tn",
        "tn",
        "product_category",
        "cat2",
        "sku_size",
        "plan_precios_cuidados"
    ]
    expected_rows = 120 * 36
    expected_shape = (expected_rows, len(expected_columns))
    assert expected_rows % 36 == 0
    dataset_name = "02_120"
    df = get_dataset(dataset_name)
    assert isinstance(df, pd.DataFrame)
    assert set(df.columns) == set(expected_columns)
    assert df.shape == expected_shape

    assert set(df["customer_id"].unique()) == set(get_clientes_importantes())
    assert set(df["product_id"].unique()) == set(get_productos_importantes())


def test_get_dataset_02_original():
    expected_columns = [
        "periodo",
        "customer_id",
        "product_id",
        "cust_request_qty",
        "cust_request_tn",
        "tn",
        "plan_precios_cuidados"
    ]
    expected_shape = (2945818, len(expected_columns))
    dataset_name = "02_original"
    df = get_dataset(dataset_name)
    assert isinstance(df, pd.DataFrame)
    assert set(df.columns) == set(expected_columns)
    assert df.shape == expected_shape



# test that each of the columns "cust_request_qty", "cust_request_tn" and "tn" sums the same in each of the datasets 01_por_cliente, 01_productos_todos and 01_original
def test_columns_sum():
    datasets = ["01_original", "01_productos_todos", "01_120", "02_original", "02_productos_todos", "02_120"] 
    columns = ["cust_request_qty", "cust_request_tn", "tn"]
    dfs = [get_dataset(dataset) for dataset in datasets]

    #597 1233 36
    assert dfs[0]["product_id"].nunique() == 1233
    assert dfs[1]["product_id"].nunique() == 1296
    
    assert dfs[3]["product_id"].nunique() == 1233
    assert dfs[4]["product_id"].nunique() == 1296

    assert dfs[0]["periodo"].nunique() == 36
    assert dfs[1]["periodo"].nunique() == 36
    assert dfs[2]["periodo"].nunique() == 36
    assert dfs[3]["periodo"].nunique() == 36
    assert dfs[4]["periodo"].nunique() == 36
    assert dfs[5]["periodo"].nunique() == 36



    # 6329834.0 1353074.0208099994 1324988.5884099994
    for column in columns:
        print(column)
        assert (
            round(dfs[0][column].sum(), 2)
            == round(dfs[1][column].sum(), 2)
            
            == round(dfs[3][column].sum(), 2)
            == round(dfs[4][column].sum(), 2)
        )

        filtered_df = dfs[0][(dfs[0]["product_id"].isin(get_productos_importantes()))&(dfs[0]["customer_id"].isin(get_clientes_importantes()))]
        assert (
            round(filtered_df[column].sum(), 2)
            == round(dfs[2][column].sum(), 2)
        )
        filtered_df_2 = dfs[3][(dfs[3]["product_id"].isin(get_productos_importantes()))&(dfs[3]["customer_id"].isin(get_clientes_importantes()))]
        assert (
            round(filtered_df_2[column].sum(), 2)
            == round(dfs[5][column].sum(), 2)
        )


def test_get_dataset_02_precios_cuidados():
    df = get_dataset("02_precios_cuidados")
    df_or = get_dataset("02_original")
    # get datasates[3] and filter out rows where plan_precios_cuidados=1
    df_or_ppc = df_or[df_or["plan_precios_cuidados"]==1]
    # get each unique pair of product_id and periodo
    df_or_ppc = df_or_ppc[["product_id", "periodo"]].drop_duplicates()
    # assert that each unique pair of product_id and periodo in df_or_ppc exists in 02_precios_cuidados
    assert df_or_ppc.merge(df, on=["product_id", "periodo"]).shape[0] == df_or_ppc.shape[0]


def test_get_dataset_02_productos_todos_anti_leak():
    df = get_dataset("02_productos_todos_anti_leak")
    # assert that the unique periodo values are 26 and that all are less than 201903
    assert df["periodo"].nunique() == 26
    assert all(df["periodo"] < 201903)

def test_get_dataset_02_120_anti_leak():
    df = get_dataset("02_120_anti_leak")
    # assert that the unique periodo values are 26 and that all are less than 201903
    assert df["periodo"].nunique() == 26
    assert all(df["periodo"] < 201903)

def test_get_dataset_02_stocks_productos_todos():
    dataset_name = "02_stocks_productos_todos"
    df = get_dataset(dataset_name)
    assert isinstance(df, pd.DataFrame)

def test_get_dataset_02_stocks_anti_leak():
    dataset_name = "02_stocks_anti_leak"
    df = get_dataset(dataset_name)
    assert isinstance(df, pd.DataFrame)


def test_get_dataset_02_productos_todos_con_FE_04():
    dataset_name = "02_productos_todos_anti_leak_con_FE_04"
    df = get_dataset(dataset_name)
    assert isinstance(df, pd.DataFrame)
    largo = len(df)
    ancho = len(df.columns)
    assert ancho == 53
    assert largo % 26 == 0
    assert largo // 26 == 1296

def test_get_dataset_02_productos_todos_con_FE_06():
    dataset_name = "02_productos_todos_anti_leak_con_FE_06"
    df = get_dataset(dataset_name)
    assert isinstance(df, pd.DataFrame)
    largo = len(df)
    ancho = len(df.columns)
    assert ancho > 53
    assert largo % 26 == 0
    assert largo // 26 == 1296

def test_get_dataset_02_desglosado_crudo():
    dataset_name = "02_productos_desglosado_crudo"
    df = get_dataset(dataset_name)
    assert isinstance(df, pd.DataFrame)
   
    # check that there are 36 unique values in column "periodo"
    assert df["periodo"].nunique() == 36

    # check that there are 1233 unique values in column "product_id"
    assert df["product_id"].nunique() == 1233

    # check that there are 595 unique values in column "customer_id"
    assert df["customer_id"].nunique() == 597

def test_get_dataset_02_desglosado():
    dataset_name = "02_productos_desglosado"
    df = get_dataset(dataset_name)
    assert isinstance(df, pd.DataFrame)
   
    # check that there are 36 unique values in column "periodo"
    assert df["periodo"].nunique() == 36

    # check that there are 1233 unique values in column "product_id"
    assert df["product_id"].nunique() == 1233

    # check that there are 595 unique values in column "customer_id"
    assert df["customer_id"].nunique() == 597

    # check that columns cat2, product_category, sku_size, brand and plan_precios_cuidados exist and have not null values
    for col in ["cat2", "cat3", "product_category", "sku_size", "brand", "plan_precios_cuidados"]:
        assert col in df.columns.to_list()
        assert df[col].isnull().sum() == 0
    
    assert df.isna().sum().sum() == 0

def test_get_dataset_02_sellout_agrupado_por_cliente():
    dataset_name = "02_sellout_agrupado_por_cliente"
    df = get_dataset(dataset_name)
    assert isinstance(df, pd.DataFrame)
   
    # check that there are 36 unique values in column "periodo"
    assert df["periodo"].nunique() == 36

    # check that there are 595 unique values in column "customer_id"
    assert df["customer_id"].nunique() == 597

    # check that it has all the rows
    shape = df.shape
    expected_rows = 36*597
    expected_cols = 5
    assert shape[0] == expected_rows
    assert shape[1] == expected_cols
    

    assert df.isna().sum().sum() == 0
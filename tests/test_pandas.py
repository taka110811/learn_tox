import pandas as pd
import pytest

# サンプルデータフレームを作成する関数
def create_sample_dataframe():
    data = {
        'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'age': [25, 30, 35, 40],
        'city': ['New York', 'Los Angeles', 'Chicago', 'Houston']
    }
    return pd.DataFrame(data)

# データフレームの内容が正しいかをテスト
def test_dataframe_creation():
    df = create_sample_dataframe()

    # 行数と列数を確認
    assert df.shape == (4, 3), "DataFrameのサイズが正しくありません"

    # カラム名を確認
    expected_columns = ['name', 'age', 'city']
    assert list(df.columns) == expected_columns, "カラム名が正しくありません"

    # 値を確認
    assert df['name'].iloc[0] == 'Alice', "最初の行の名前が正しくありません"
    assert df['age'].iloc[1] == 30, "2番目の行の年齢が正しくありません"
    assert df['city'].iloc[2] == 'Chicago', "3番目の行の都市が正しくありません"

# 年齢のフィルタリングをテスト
def test_filter_by_age():
    df = create_sample_dataframe()

    # 30歳以上の行をフィルタリング
    filtered_df = df[df['age'] >= 30]

    # フィルタリング後の行数を確認
    assert len(filtered_df) == 3, "30歳以上の行が正しくフィルタリングされていません"

    # フィルタされたデータの内容を確認
    assert all(filtered_df['age'] >= 30), "フィルタリングされたデータの年齢が正しくありません"

# データの更新をテスト
def test_update_city():
    df = create_sample_dataframe()

    # 'Alice'の都市を'San Francisco'に変更
    df.loc[df['name'] == 'Alice', 'city'] = 'San Francisco'

    # 値が正しく更新されているか確認
    assert df.loc[df['name'] == 'Alice', 'city'].iloc[0] == 'San Francisco', "都市の値が正しく更新されていません"
from typing import List, Optional
import pandas as pd


class TableExtractor:
    """CSSセレクタを使用してHTMLから情報を抽出するクラス"""

    def __init__(
        self,
        table_index: Optional[int] = None,
        table_match: Optional[str] = None,
        keep_first_columns: int = None,
        skip_first_rows: int = 0,
        column_names: List[str] = None,
    ):
        """
        Args:
            table_index (int, optional): 対象のtableのindex
            table_match (str, optional): テーブル内の文字列でマッチング
            keep_first_columns (int, optional): 先頭から保持する列数（Noneの場合は全列を保持）
            skip_first_rows (int, optional): 先頭からスキップする行数
            column_names (List[str], optional): 列名のリスト
        """
        if table_index is None and table_match is None:
            raise ValueError("table_indexまたはtable_matchのいずれかを指定してください")
        if table_index is not None and table_match is not None:
            raise ValueError("table_indexとtable_matchは同時に指定できません")

        self.table_index = table_index
        self.table_match = table_match
        self.keep_first_columns = keep_first_columns
        self.skip_first_rows = skip_first_rows
        self.column_names = column_names if column_names is not None else []

    def extract(self, html: str) -> pd.DataFrame:
        # インデックス指定
        if self.table_index is not None:
            table = pd.read_html(html)[self.table_index]
        # match指定
        else:
            table = pd.read_html(html, match=self.table_match)[0]

        # 先頭行をスキップ
        if self.skip_first_rows > 0:
            table = table.iloc[self.skip_first_rows :]

        # 先頭から指定列数のみ保持
        if self.keep_first_columns is not None:
            table = table.iloc[:, : self.keep_first_columns]

        # 列名を設定
        if self.column_names:
            table.columns = self.column_names

        return table.reset_index(drop=True)

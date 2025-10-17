from enum import Enum
from typing import Any, Callable, Dict, Optional
from pydantic import BaseModel
from bs4 import BeautifulSoup


class ElementAttrEnum(str, Enum):
    """要素から取得する属性の種類を定義"""

    TEXT = "text"
    HREF = "href"
    SRC = "src"
    CLASS = "class"
    ID = "id"
    TITLE = "title"
    ALT = "alt"
    VALUE = "value"
    PASS = "pass"
    HTML = "innerHTML"


class InstructionField(BaseModel):
    """抽出指示を定義するフィールド"""

    css_selector: str
    attr: ElementAttrEnum = ElementAttrEnum.TEXT
    index: Optional[int] = None
    processor: Optional[Callable[[Any], Any]] = None

    class Config:
        arbitrary_types_allowed = True


class CssSelectExtractor:
    """CSSセレクタを使用してHTMLから情報を抽出するクラス"""

    def __init__(self, instructions: Dict[str, InstructionField]):
        """
        Args:
            instructions: 抽出指示の辞書（キー: 結果のキー名, 値: InstructionField）
        """
        self.instructions = instructions

    def extract(self, html: str) -> Dict[str, Any]:
        """
        HTMLから指定された情報を抽出

        Args:
            html: 解析対象のHTML文字列

        Returns:
            抽出結果の辞書（キー: instructionsで指定したキー, 値: 抽出値）
        """
        soup = BeautifulSoup(html, "html.parser")
        result = {}

        for key, instruction in self.instructions.items():
            extracted_value = self._extract_single_field(soup, instruction)
            result[key] = extracted_value

        return result

    def _extract_single_field(
        self, soup: BeautifulSoup, instruction: InstructionField
    ) -> Any:
        """
        単一のフィールドを抽出

        Args:
            soup: BeautifulSoupオブジェクト
            instruction: 抽出指示

        Returns:
            抽出された値
        """
        elements = soup.select(instruction.css_selector)

        if not elements:
            return None

        # index指定がある場合は単一要素を取得
        if instruction.index is not None:
            if instruction.index >= len(elements):
                return None
            elements = [elements[instruction.index]]

        # 属性に応じて値を抽出
        values = []
        for element in elements:
            if instruction.attr == ElementAttrEnum.TEXT:
                value = element.get_text(strip=True)
            elif instruction.attr == ElementAttrEnum.PASS:
                value = element
            else:
                value = element.get(instruction.attr.value)

            # processorが指定されている場合は適用
            if value is not None and instruction.processor:
                try:
                    value = instruction.processor(value)
                except Exception as e:
                    print(f"Processor error for key '{key}': {e}")
                    value = None

            values.append(value)

        # index指定がある場合は単一値を返す
        if instruction.index is not None:
            return values[0] if values else None

        return values

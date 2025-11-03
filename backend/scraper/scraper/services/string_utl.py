import re


def extract_year(text):
    era_start = {
        "令和": 2019,
        "平成": 1989,
        "昭和": 1926,
        "大正": 1912,
        "明治": 1868,
    }

    # 西暦4桁を直接検索
    western_match = re.search(r"\d{4}", text)
    if western_match:
        return int(western_match.group())

    # 和暦を検索
    for era, start_year in era_start.items():
        if era in text:
            # 和暦の後の数字を抽出（1-2桁）
            pattern = era + r"\s*(\d{1,2})"
            match = re.search(pattern, text)
            if match:
                era_year = int(match.group(1))
                return start_year + era_year - 1

            # 数字が和暦の前にある場合（例: "31平成"）
            pattern = r"(\d{1,2})" + era
            match = re.search(pattern, text)
            if match:
                era_year = int(match.group(1))
                return start_year + era_year - 1

    raise ValueError(f"年を抽出できませんでした: {text}")

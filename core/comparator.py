import pandas as pd

from core.excel_reader import read_excel


def compare_spreadsheets(old_file, new_file, key_column=None):
    old_df = read_excel(old_file)
    new_df = read_excel(new_file)

    old_df = old_df.fillna('')
    new_df = new_df.fillna('')

    if not key_column:
        key_column = old_df.columns[0]

    old_keys = set(old_df[key_column])
    new_keys = set(new_df[key_column])

    added = new_df[new_df[key_column].isin(new_keys - old_keys)]
    removed = old_df[old_df[key_column].isin(old_keys - new_keys)]

    modified = []

    common = old_keys.intersection(new_keys)

    for key in common:
        old_row = old_df[old_df[key_column] == key].iloc[0]
        new_row = new_df[new_df[key_column] == key].iloc[0]

        differences = {}

        for col in old_df.columns:
            if str(old_row[col]) != str(new_row[col]):
                differences[col] = {
                    'old': old_row[col],
                    'new': new_row[col]
                }

        if differences:
            modified.append({
                'key': key,
                'changes': differences
            })

    total_old = len(old_df)
    total_new = len(new_df)

    return {
        'total_old': total_old,
        'total_new': total_new,
        'added': added,
        'removed': removed,
        'modified': modified,
        'difference_percent': round(
            (len(modified) / max(total_new, 1)) * 100,
            2
        )
    }

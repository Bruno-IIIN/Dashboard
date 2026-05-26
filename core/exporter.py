import pandas as pd


def export_to_excel(data, filename):
    with pd.ExcelWriter(filename, engine='xlsxwriter') as writer:
        data.to_excel(writer, index=False)

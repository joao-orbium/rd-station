import pandas as pd
import matplotlib.pyplot as plt
from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference
from openpyxl.utils.dataframe import dataframe_to_rows

class Sheets:
    def __init__(self, parsed_data):
        self.parsed_data = parsed_data

    def make_simple_sheet(self, file_name):
        self.simple_sheet_filename = file_name
        df = pd.DataFrame(self.parsed_data)
        df['Produtos Negociados'] = df['Produtos Negociados'].apply(lambda x: ', '.join(x) if isinstance(x, list) else x)
        df.to_excel(file_name, index=False)
        print(f"Excel sheet saved under {self.simple_sheet_filename}")

    def make_revenue_sheet(self, file_name):
        df = pd.DataFrame(self.parsed_data)
        revenue_summary = df.groupby('Tipo').agg({
            'Valor Mensal': 'sum',
            'Valor Único': 'sum',
            'Projeção Anual': 'sum' 
        }).reset_index()

        # Format the currency columns to Brazilian Real format for display
        formatted_revenue_summary = revenue_summary.copy()
        formatter = "R$ {:,.2f}".format
        formatted_revenue_summary['Valor Mensal'] = formatted_revenue_summary['Valor Mensal'].apply(formatter)
        formatted_revenue_summary['Valor Único'] = formatted_revenue_summary['Valor Único'].apply(formatter)
        formatted_revenue_summary['Projeção Anual'] = formatted_revenue_summary['Projeção Anual'].apply(formatter)

        wb = Workbook()
        ws = wb.active
        ws.title = 'Análise de Receita'

        # Append formatted data for display
        for r in dataframe_to_rows(formatted_revenue_summary, index=False, header=True):
            ws.append(r)

        # Append numerical data for chart
        chart_start_row = len(revenue_summary) + 3
        for r in dataframe_to_rows(revenue_summary, index=False, header=True):
            ws.append(r)

        # Create a bar chart using the numerical data
        chart = BarChart()
        categs = Reference(ws, min_col=1, min_row=chart_start_row + 1, max_row=chart_start_row + len(revenue_summary))
        data = Reference(ws, min_col=2, min_row=chart_start_row, max_row=chart_start_row + len(revenue_summary), max_col=4)

        chart.add_data(data, titles_from_data=True)
        chart.set_categories(categs)
        chart.title = "Análise de Receita"

        # Set the labels for the data series
        for i, name in enumerate(['Valor Mensal', 'Valor Único', 'Projeção Anual']):
            chart.series[i].name = name

        ws.add_chart(chart, 'A' + str(chart_start_row + len(revenue_summary) + 2))

        wb.save(file_name)

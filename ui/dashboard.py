from PySide6.QtWidgets import (
        self.pie_chart.setHtml(pie.to_html(include_plotlyjs='cdn'))

        bars = go.Figure(
            data=[
                go.Bar(
                    x=['Novos', 'Removidos', 'Alterados'],
                    y=[added, removed, modified],
                    orientation='v'
                )
            ]
        )

        bars.update_layout(
            template='plotly_dark',
            paper_bgcolor='rgba(0,0,0,0)'
        )

        self.bar_chart.setHtml(bars.to_html(include_plotlyjs='cdn'))

        heatmap = go.Figure(
            data=go.Heatmap(
                z=[[added, removed, modified]],
                x=['Novos', 'Removidos', 'Alterados'],
                y=['Impacto']
            )
        )

        heatmap.update_layout(
            template='plotly_dark',
            paper_bgcolor='rgba(0,0,0,0)'
        )

        self.heatmap_chart.setHtml(heatmap.to_html(include_plotlyjs='cdn'))

        ranking = go.Figure(
            data=[
                go.Bar(
                    x=[modified, removed, added],
                    y=['Alterados', 'Removidos', 'Novos'],
                    orientation='h'
                )
            ]
        )

        ranking.update_layout(
            template='plotly_dark',
            paper_bgcolor='rgba(0,0,0,0)'
        )

        self.ranking_chart.setHtml(ranking.to_html(include_plotlyjs='cdn'))

        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(['Categoria', 'Quantidade'])

        data = [
            ('Novos', added),
            ('Removidos', removed),
            ('Alterados', modified)
        ]

        self.table.setRowCount(len(data))

        for row, item in enumerate(data):
            self.table.setItem(row, 0, QTableWidgetItem(item[0]))
            self.table.setItem(row, 1, QTableWidgetItem(str(item[1])))

        self.alerts.clear()

        if modified > 0:
            self.alerts.addItem(QListWidgetItem(
                f'⚠ Foram encontradas {modified} alterações críticas.'
            ))

        if removed > 0:
            self.alerts.addItem(QListWidgetItem(
                f'⚠ {removed} registros foram removidos.'
            ))

        if added > 0:
            self.alerts.addItem(QListWidgetItem(
                f'✔ {added} novos registros adicionados.'
            ))

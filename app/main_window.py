from PySide6.QtWidgets import (

        self.progress = QProgressBar()
        self.progress.setValue(0)

        self.dashboard = DashboardPage()

        self.old_btn.clicked.connect(self.select_old)
        self.new_btn.clicked.connect(self.select_new)
        self.compare_btn.clicked.connect(self.compare)

        content_layout.addWidget(header)
        content_layout.addWidget(self.old_btn)
        content_layout.addWidget(self.old_label)
        content_layout.addWidget(self.new_btn)
        content_layout.addWidget(self.new_label)
        content_layout.addWidget(self.compare_btn)
        content_layout.addWidget(self.progress)
        content_layout.addWidget(self.dashboard)

        main_layout.addWidget(sidebar)
        main_layout.addWidget(content)

    def select_old(self):
        file, _ = QFileDialog.getOpenFileName(
            self,
            'Selecionar planilha anterior',
            '',
            'Excel (*.xlsx *.xls)'
        )

        if file:
            self.old_file = file
            self.old_label.setText(file)

    def select_new(self):
        file, _ = QFileDialog.getOpenFileName(
            self,
            'Selecionar planilha atual',
            '',
            'Excel (*.xlsx *.xls)'
        )

        if file:
            self.new_file = file
            self.new_label.setText(file)

    def compare(self):
        if not self.old_file or not self.new_file:
            QMessageBox.warning(self, 'Aviso', 'Selecione ambas as planilhas.')
            return

        try:
            self.progress.setValue(20)

            result = compare_spreadsheets(
                self.old_file,
                self.new_file
            )

            self.progress.setValue(80)

            self.dashboard.update_dashboard(result)

            self.progress.setValue(100)

            self.history.addItem(
                f'Comparação realizada: {self.new_file}'
            )

        except Exception as e:
            QMessageBox.critical(self, 'Erro', str(e))

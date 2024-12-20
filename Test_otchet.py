from docx import Document 

def save_to_docx(self):
        document = Document()
        table = document.add_table(rows=1, cols=self.table.columnCount())
        
        # Добавление заголовков
        hdr_cells = table.rows[0].cells
        for i in range(self.table.columnCount()):
            hdr_cells[i].text = self.table.horizontalHeaderItem(i).text()

        # Добавление данных из QTableWidget
        for row in range(self.table.rowCount()):
            row_cells = table.add_row().cells
            for col in range(self.table.columnCount()):
                item = self.table.item(row, col)
                if item is not None:
                    row_cells[col].text = item.text()

        # Сохранение документа
        document.save('table_data.docx')
        print("Данные сохранены в table_data.docx")
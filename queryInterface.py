import sqlite3
import csv
import os
class QueryInterface:
    def __init__(self, conn):
        self.conn = conn
        self.cur = conn.cursor()
    def fetchall(self, query, params=()):
        self.cur.execute(query, params)
        result = self.cur.fetchall()
        column_names = [description[0] for description in self.cur.description]
        return column_names, result
    def get_dataset_text_labels(self, metadata = False, show_lines = 10, save_to=None):
        query = '''
        SELECT dataset.dataset_name, text.text, label.label_name, label.label_value
        FROM text
        JOIN dataset ON text.dataset_id = dataset.dataset_id
        JOIN label ON label.dataset_id = dataset.dataset_id AND label.text_id = text.text_id;
        '''
        if metadata:
            query = '''
            SELECT dataset.dataset_name, text.text, label.label_name, label.label_value, label.label_definition, text_source.source, language.language
            FROM text
            JOIN dataset ON text.dataset_id = dataset.dataset_id
            JOIN label ON label.dataset_id = dataset.dataset_id AND label.text_id = text.text_id
            JOIN text_source ON text_source.source_id = text.source_id
            JOIN language ON language.language_id = text.language_id
            '''
        column_names, result = self.fetchall(query)
        if save_to is not None:
            _, file_extension = os.path.splitext(save_to)
            if file_extension == '.csv':
                with open(save_to, 'w', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow(column_names)
                    for row in result:
                        # deal with None value
                        row = [str(item) if item is not None else '' for item in row]
                        writer.writerow(row)
            elif file_extension.lower() == '.tsv':
                with open(save_to, 'w', encoding='utf-8') as f:
                    f.write('\t'.join(column_names) + '\n')
                    for row in result:
                        # deal with None value
                        row = [str(item) if item is not None else '' for item in row]
                        f.write('\t'.join(row) + '\n')
            else:
                raise ValueError("Unsupported file extension. Please use .csv or .tsv")
        return column_names, result[:show_lines]
    def close(self):
        self.conn.close()
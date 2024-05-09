# import sqlite3
# import os
#
# import myGlobals
# conn = myGlobals.connect()
# c = conn.cursor()
#
# c.execute("SELECT name FROM sqlite_master WHERE type='table';")
# tables = c.fetchall()
#
# for table_name in tables:
#     print(table_name[0])
# #%%
# def add_dataset(file_path, dataset_name):
#     dataset_original_name = os.path.basename(file_path)
#     try:
#         c.execute("INSERT INTO dataset (datasetOriginalName, datasetName) VALUES (?, ?)",
#                   (dataset_original_name, dataset_name))
#         conn.commit()
#         print(f"Dataset {dataset_name} added successfully.")
#         return c.lastrowid
#     except sqlite3.IntegrityError as e:
#         print(f"Failed to add dataset {dataset_name}: {e}")
#
# dataset_id = add_dataset('H:\\UZH\\Master Project\\data\\edos_labelled_aggregated.csv', 'HateSpeech1')
# #%%
# def add_schema(dataset_id, label_name):
#     try:
#         c.execute("INSERT INTO schema (datasetID, labelName) VALUES (?, ?)",
#                   (dataset_id, label_name))
#         conn.commit()
#     except sqlite3.IntegrityError as e:
#         print(f"Error: {e}")
#         print("This may be due to the non-existence of the corresponding datasetID.")
#
# add_schema(dataset_id, 'Example Label')
# #%%
# def add_text(text_id, dataset_id, source_id, text_content):
#     try:
#         c.execute("INSERT INTO text (textID, datasetID, sourceID, text) VALUES (?, ?, ?, ?)",
#                   (text_id, dataset_id, source_id, text_content))
#         conn.commit()
#     except sqlite3.IntegrityError as e:
#         print(f"Error: {e}")
#         print("This may be due to a violation of a uniqueness constraint or the non-existence of the corresponding datasetID.")
#
#
# add_text(0, dataset_id, 101, 'Sample Text')
# add_text(1, dataset_id, 102, 'Sample Text 2')
# #%%
# def add_label(dataset_id, text_id, label_name, label_value, label_definition):
#     try:
#         c.execute("INSERT INTO label (datasetID, textID, labelName, labelValue, labelDefinition) VALUES (?, ?, ?, ?, ?)",
#                   (dataset_id, text_id, label_name, label_value, label_definition))
#         conn.commit()
#     except sqlite3.IntegrityError as e:
#         print(f"Error: {e}")
#         print("This may be due to a violation of uniqueness constraints, foreign key constraints, or the non-existence of the corresponding datasetID and textID.")
#
#
# add_label(dataset_id, 0, 'Category', 'Education', 'Defines the type of education topic discussed.')
# #%%
# def add_text_source(source_name):
#     try:
#         c.execute("INSERT INTO textSource (source) VALUES (?)",
#                   (source_name,))
#         conn.commit()
#     except sqlite3.IntegrityError as e:
#         print(f"Error: {e}")
#         print("An error occurred while adding data.")
#
# add_text_source('Wikipedia Article')
# #%%
# conn.close()
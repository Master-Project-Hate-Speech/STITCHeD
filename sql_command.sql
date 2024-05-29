SELECT dataset.dataset_name, text.text, label.label_name, label.label_value, label.label_definition, text_source.source, language.language
FROM text
JOIN dataset ON text.dataset_id = dataset.dataset_id
JOIN label ON label.dataset_id = dataset.dataset_id AND label.text_id = text.text_id
JOIN text_source ON text_source.source_id = text.source_id
JOIN language ON language.language_id = text.language_id
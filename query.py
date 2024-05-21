import argparse
from queryInterface import QueryInterface
import myGlobals

def display_query_results(column_names, result):
    print(column_names)
    for row in result:
        print(row)

def setup_get_dataset_text_labels_parser(subparsers):
    parser_get_dataset_text_labels = subparsers.add_parser('get_dataset_text_labels', help='Query the database')
    parser_get_dataset_text_labels.add_argument('--metadata', help='Whether the label definition, text source and language are needed', action='store_true')
    parser_get_dataset_text_labels.add_argument('--show-lines', type=int, help='Number of lines to show')
    parser_get_dataset_text_labels.add_argument('--save-to', type=str, help='Path to save the results')
def main():
    # connect to database
    conn = myGlobals.connect()
    queryInterface = QueryInterface(conn)
    # create parser
    parser = argparse.ArgumentParser(description="Command line interface for querying the database.")
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    # set subparsers
    setup_get_dataset_text_labels_parser(subparsers)
    # parse arguments
    args = parser.parse_args()
    # process commands
    if args.command == 'get_dataset_text_labels':
        column_names, result = queryInterface.get_dataset_text_labels(metadata=args.metadata, show_lines=args.show_lines, save_to=args.save_to)
        display_query_results(column_names, result)
if __name__ == '__main__':
    '''
    CommandLine:
    python query.py
    python query.py get_dataset_text_labels
    python query.py get_dataset_text_labels --metadata --show-lines 1 --save-to trial.csv
    '''
    main()
import argparse
from participant_list import participant_list
from evaluate import pick

def main():
    parser = argparse.ArgumentParser(prog='Secret Santa Picker')
    subparsers = parser.add_subparsers()
    
    parser_list = subparsers.add_parser('list', help='Handling the list of participants.')
    parser_list.set_defaults(func=participant_list)
    list_args = parser_list.add_mutually_exclusive_group(required=True)
    list_args.add_argument('-r', '--register', action='append', help='Register a new participant.', metavar='\"NAME:EMAIL\"')
    list_args.add_argument('-s', '--show', action='store_true', help='Show the enrolled participants.')
    list_args.add_argument('-d', '--delete', action='append', help='Delete a participant', metavar='\"NAME OR EMAIL\"')

    parser_pick = subparsers.add_parser('pick', help='Shuffling and sending the results')
    parser_pick.add_argument('-n', '--nosend', action='store_true', help='Only shuffle, don\'t send results')
    parser_pick.set_defaults(func=pick)

    args = parser.parse_args()
    args.func(args)



if __name__=='__main__':
    main()
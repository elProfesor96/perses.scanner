import argparse


def args_init():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,prog="perses",description="""Scan any file with multiple AV solutions/engines. 
This project was inspired by virustotal, but with the redteam focus, offline scanner for corporates and malware developers.

Credits:
    https://elprofesor.io
    https://github.com/elprofesor96/perses.scanner""", epilog="Example: ")
    parser.add_argument("scan", help="Scan with all AV plugins or just one.",nargs='*', action="store")
    parser.add_argument("updatedb", help="Updates all the AV plugins databases.",nargs='*', action="store")
    parser.add_argument("list", help="List all AV plugins installed.",nargs='*', action="store")
    parser.add_argument("api", help="Start the api service.",nargs='*', action="store")

    args = parser.parse_args()
    return args, parser


def main():
    args, parser = args_init()
    try:
        if args.scan[0] == 'scan':
            
            exit()
        elif args.scan[0] == 'updatedb':
            
            exit()
        elif args.scan[0] == 'list':
            
            exit()
        elif args.scan[0] == 'api':
            import api
        else:
            parser.print_help()
    except IndexError:
        parser.print_help()


if __name__ == '__main__':
    main()
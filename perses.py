import argparse
import api
from engine import Engine 


def args_init():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,prog="perses",description="""Scan any file with multiple AV solutions/engines. 
This project was inspired by virustotal, but with the redteam focus, offline scanner for corporates and malware developers.

Credits:
    https://elprofesor.io
    https://github.com/elprofesor96/perses.scanner""", epilog="Example: perses -h")
    parser.add_argument("scan", help="Scan file with all AV plugins. Example: perses scan [FILE]",nargs='*', action="store")
    parser.add_argument("plugins", help="AV plugins commmands to list/update. Example: perses plugins [LIST/UPDATE]",nargs='*', action="store")
    parser.add_argument("api", help="Start the api service.",nargs='*', action="store")

    args = parser.parse_args()
    return args, parser


def main():
    args, parser = args_init()
    try:
        if args.scan[0] == 'scan':
            if args.scan[1]:
                engine = Engine()
                engine.scan(args.scan[1])   
            exit()
        elif args.scan[0] == 'plugins':
            if args.scan[1] == 'list':
                print("installed plugins")
            elif args.scan[1] == 'update':
                print("update plugins")
            else:
                parser.print_help()  
            exit()
        elif args.scan[0] == 'api':
            api.run()
        else:
            parser.print_help()
    except IndexError:
        parser.print_help()


if __name__ == '__main__':
    main()
'''urlp CLI'''


import argparse
import sys
import tldextract

try:
    from urlparse import parse_qs, urlparse
except ImportError:
    from urllib.parse import parse_qs, urlparse


def run_host_command(args, url):
    hostname = urlparse(url).hostname
    print(hostname)


def run_path_command(args, url):
    path = urlparse(url).path
    if args.path_index > -1:
        pathes = path.split('/')
        if len(pathes) < (args.path_index + 1):
            sys.stderr.write('path_index out of range\n')
            exit(1)
        print(pathes[args.path_index+1])
    else:
        print(path)


def run_query_command(args, url):
    query = urlparse(url).query
    if args.query_field:
        kvs = parse_qs(query)
        if args.query_field not in kvs:
            sys.stderr.write('no query_field named {}\n'.format(args.query_field))
            exit(1)
        print(','.join(kvs[args.query_field]))
    else:
        print(query)


def run_registered_domain(args, url):
    print(tldextract.extract(url).registered_domain)


def run_default_command(args, url):
    print(url)


commands = {
    'host': run_host_command,
    'path': run_path_command,
    'query': run_query_command,
    'registered_domain': run_registered_domain,
    'all': run_default_command,
}


def execute(args):
    command = commands[args.part]
    for url in args.input:
        command(args, url)


def execute_from_stdin(args):
    command = commands[args.part]
    for line in sys.stdin:
        url = line.strip()
        command(args, url)


def main():
    '''urlp CLI main command.'''

    parser = argparse.ArgumentParser(
        prog='urlp',
        description='A command line url parser'
    )

    parser.add_argument('input', metavar='url', nargs='*', help='URL to parse')
    parser.add_argument('--part', default='all', choices=commands.keys(),
                        help='Part of URL to show')
    parser.add_argument('--path_index', type=int, default=-1,
                        help='Filter parsed path by index')
    parser.add_argument('--query_field', 
                        help='Value for the specified query field')

    args = parser.parse_args()

    if len(args.input) is 0:
        execute_from_stdin(args)
    else:
        execute(args)


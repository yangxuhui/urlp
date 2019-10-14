'''urlp CLI'''


import argparse
import sys
import tldextract

try:
    from urlparse import parse_qs, urlparse
except ImportError:
    from urllib.parse import parse_qs, urlparse


def get_path(parsed, path_index):
    path = parsed.path
    if path_index > -1:
        pathes = path.split('/')
        return '' if len(pathes) < (path_index + 1) else pathes[path_index+1]
    else:
        return path


def get_query(parsed, query_field):
    query = parsed.query
    if query_field:
        kvs = parse_qs(query)
        return '' if query_field not in kvs else ','.join(kvs[query_field])
    else:
        return query


def run(args, url):
    parsed = urlparse(url)
    result = []
    if args.host:
        result.append(parsed.hostname)
    if args.path:
        result.append(get_path(parsed, args.path_index))
    if args.query:
        result.append(get_query(parsed, args.query_field))
    if args.registered_domain:
        result.append(tldextract.extract(url).registered_domain)
    if result:
        print('\t'.join(result))
    else:
        print(url)


def execute(args):
    for url in args.input:
        run(args, url)


def execute_from_stdin(args):
    for line in sys.stdin:
        url = line.strip()
        run(args, url)


def main():
    '''urlp CLI main command.'''

    parser = argparse.ArgumentParser(
        prog='urlp',
        description='A command line url parser'
    )

    parser.add_argument('input', metavar='urls', nargs='*', help='URLs to parse')
    parser.add_argument('--host', action='store_true', help='hostname')
    parser.add_argument('-p', '--path', action='store_true', help='Path')
    parser.add_argument('-i', '--path_index', type=int, default=-1, 
                        metavar='path_index', help='filter parsed path by index')
    parser.add_argument('-q', '--query', action='store_true', help='query string')
    parser.add_argument('-k', '--query_field', metavar='query_field', 
                        help='value for the specified query field')
    parser.add_argument('-r', '--registered_domain', action='store_true', 
                        help='registered domain')

    args = parser.parse_args()

    if len(args.input) is 0:
        execute_from_stdin(args)
    else:
        execute(args)


# urlp
A simple command-line utility for parsing URLs, written in Python. Inspired by [urlp](https://github.com/clayallsopp/urlp).

```bash
$ urlp --host "http://www.cnn.com/service/alert.jsp?s=cnn&v=a"
www.cnn.com
$ urlp --registered_domain "http://www.cnn.com/service/alert.jsp?s=cnn&v=a"
cnn.com
$ urlp --path "http://www.cnn.com/service/alert.jsp?s=cnn&v=a"
/service/alert.jsp
$ urlp --path -i 0 "http://www.cnn.com/service/alert.jsp?s=cnn&v=a"
service
$ urlp --query "http://www.cnn.com/service/alert.jsp?s=cnn&v=a"
s=cnn&v=a
$ urlp --query --query_field=s "http://www.cnn.com/service/alert.jsp?s=cnn&v=a"
cnn
```
urlp often works together with other unix command-line tools. For example:
* Find all hosts in urls, sorted by count.
```bash
cat urlfile | urlp --host | sort | uniq -c | sort -nr -k1,1
```
* Find all url path words (separated by "/"), sorted by count.
```bash
cat urlfile | urlp --path | tr / \\n | awk '$1!=""' | sort | uniq -c | sort -nr -k1,1
```

## Install
```
pip install urlp
```

## Usage
```
$ urlp --help
usage: urlp [-h] [--host] [-p] [-i path_index] [-q] [-k query_field] [-r]
            [urls [urls ...]]

A command line url parser

positional arguments:
  urls                  URLs to parse

optional arguments:
  -h, --help            show this help message and exit
  --host                hostname
  -p, --path            Path
  -i path_index, --path_index path_index
                        filter parsed path by index
  -q, --query           query string
  -k query_field, --query_field query_field
                        value for the specified query field
  -r, --registered_domain
                        registered domain
```
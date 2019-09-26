# urlp
A simple command-line utility for parsing URLs, written in Python. Inspired by [urlp](https://github.com/clayallsopp/urlp).

```bash
$ urlp --part=host "http://audience.cnn.com/services/activatealert.jsp?source=cnn&id=203&value=hurricane+isabel"
audience.cnn.com
$ urlp --part=registered_domain "http://audience.cnn.com/services/activatealert.jsp?source=cnn&id=203&value=hurricane+isabel"
cnn.com
$ urlp --part=path "http://audience.cnn.com/services/activatealert.jsp?source=cnn&id=203&value=hurricane+isabel"
/services/activatealert.jsp
$ urlp --part=path --path_index=0 "http://audience.cnn.com/services/activatealert.jsp?source=cnn&id=203&value=hurricane+isabel"
services
$ urlp --part=query "http://audience.cnn.com/services/activatealert.jsp?source=cnn&id=203&value=hurricane+isabel"
source=cnn&id=203&value=hurricane+isabel
$ urlp --part=query --query_field=source "http://audience.cnn.com/services/activatealert.jsp?source=cnn&id=203&value=hurricane+isabel"
cnn
```
urlp often works together with other unix command-line tools. For example:
* Find all hosts in urls, sorted by count.
```bash
cat urlfile | urlp --part=host | sort | uniq -c | sort -nr -k1,1
```
* Find all url path words (separated by "/"), sorted by count.
```bash
cat urlfile | urlp --part=path | tr / \\n | awk '$1!=""' | sort | uniq -c | sort -nr -k1,1
```

## Install
```
pip install urlp
```
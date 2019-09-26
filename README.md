# urlp
A simple command-line utility for parsing URLs, written in Python. Inspired by [urlp](https://github.com/clayallsopp/urlp).

```bash
$ urlp --part=host "http://www.cnn.com/service/alert.jsp?s=cnn&v=a"
www.cnn.com
$ urlp --part=registered_domain "http://www.cnn.com/service/alert.jsp?s=cnn&v=a"
cnn.com
$ urlp --part=path "http://www.cnn.com/service/alert.jsp?s=cnn&v=a"
/service/alert.jsp
$ urlp --part=path --path_index=0 "http://www.cnn.com/service/alert.jsp?s=cnn&v=a"
service
$ urlp --part=query "http://www.cnn.com/service/alert.jsp?s=cnn&v=a"
s=cnn&v=a
$ urlp --part=query --query_field=s "http://www.cnn.com/service/alert.jsp?s=cnn&v=a"
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
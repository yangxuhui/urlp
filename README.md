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
```

## Install
```
pip install urlp
```
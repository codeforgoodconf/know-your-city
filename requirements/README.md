**Do not** modify the `*.txt` file directly. If you need to add a package, add
them to the proper `*.in` file and use [pip-tools][] to compile the
requirements. You can also pin a package to a specific version if needed.

If there are packages you like to use during development that's not specified,
create a `local.in` file. For example:

```
-r dev.in

ipython
```

Be sure to include `dev.in` and the different `make` targets will do the right
thing.

Note that `local.in` and `local.txt` are not checked in.


[pip-tools]: https://github.com/jazzband/pip-tools

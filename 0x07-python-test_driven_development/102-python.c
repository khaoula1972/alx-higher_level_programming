#include <stdio.h>
#include <Python.h>
#include <wchar.h>
/**
 * print_python_string - a function that prints Python strings.
 * @p: pointer to the string
 */
void print_python_string(PyObject *p)
{
        wchar_t *str;
        int compact;
        Py_ssize_t len;

        printf("[.] string object info\n");
        if (!PyUnicode_Check(p))
        {
                fprintf(stderr, " [ERROR] Invalid String Object\n");
                return;
        }

        str = PyUnicode_AsWideCharString(p, NULL);
        len = PyUnicode_GET_SIZE(p);
        compact = PyUnicode_IS_COMPACT_ASCII(p) ? 1 : 0;

        printf(" type: %s %s\n", compact ? "compact" : "compact unicode", compact ? "ascii" : "object");
        printf(" length: %ld\n", len);
        printf(" value: %ls\n", str);
}

#include <stdio.h>
#include <Python.h>
#include <wchar.h>

/**
 * print_python_string - a function that prints Python strings.
 * @p: pointer to the string
 */
void print_python_string(PyObject *p)
{
    Py_UNICODE *str;
    Py_ssize_t len, i;

    printf("[.] string object info\n");

    if (!PyUnicode_Check(p))
    {
        fprintf(stderr, " [ERROR] Invalid String Object\n");
        return;
    }

    len = PyUnicode_GET_SIZE(p);
    str = PyUnicode_AsUnicode(p);

    if (!str)
    {
        fprintf(stderr, " [ERROR] Unable to convert to Unicode\n");
        return;
    }

    printf(" type: %s %s\n", PyUnicode_IS_COMPACT_ASCII(p) ? "compact" : "compact unicode", PyUnicode_IS_COMPACT_ASCII(p) ? "ascii" : "object");
    printf(" length: %ld\n", len);

    printf(" value: ");
    for (i = 0; i < len; i++)
    {
        wchar_t ch = str[i];
        if (ch >= 0x20 && ch <= 0x7E)
        {
            // Printable ASCII character, print it directly
            printf("%c", (char)ch);
        }
        else
        {
            // Non-ASCII character, manually convert to UTF-8
            if (ch <= 0x7FF)
            {
                // 2-byte UTF-8 encoding
                printf("%c%c", (char)(0xC0 | (ch >> 6)), (char)(0x80 | (ch & 0x3F)));
            }
            else
            {
                // 3-byte UTF-8 encoding
                printf("%c%c%c", (char)(0xE0 | (ch >> 12)), (char)(0x80 | ((ch >> 6) & 0x3F)), (char)(0x80 | (ch & 0x3F)));
            }
        }
    }
    printf("\n");
}

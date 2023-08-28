#include <Python.h>

/**
 * print_python_list - print some basic info about Python lists
 * @p: a pointer
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t allocated, size;
	PyObject *item;

	if (!PyList_Check(p))
	{
		printf("[ERROR] Invalid List Object\n");
		return;
	}

	size = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}


/**
 * print_python_bytes - print some basic info about Python bytes
 * @p: a pointer
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	const char *string = PyBytes_AsString(p);

	if (!PyBytes_Check(p))
	{
		printf("[ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);

	printf("  trying string: ");
	for (i = 0; i < size && i < 10; i++)
		printf("%c", string[i]);
	printf("\n");

	printf("  first 10 bytes: ");
	for (i = 0; i < size && i < 10; i++)
		printf("%02x ", (unsigned char)string[i]);
	printf("\n");
}

/**
 * print_python_float - print some basic info about Python float
 * @p: a pointer
 */
void print_python_float(PyObject *p)
{
	double value;

	if (!PyFloat_Check(p))
	{
		printf("[ERROR] Invalid Float Object\n");
		return;
	}

	value = PyFloat_AsDouble(p);

	printf("[.] float object info\n");
	printf("  value: %f\n", value);
}


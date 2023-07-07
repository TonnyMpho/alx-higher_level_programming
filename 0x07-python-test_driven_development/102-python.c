#include <stdio.h>
#include <Python.h>
#include <string.h>

/**
 * print_python_string - function that prints Python strings
 * @p: Python object
 * Return: Void (nothing)
 */
void print_python_string(PyObject *p)
{
	size_t len;
	PyObject *str;

	printf("[.] string object info\n");

	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	len = PyUnicode_GET_LENGTH(p);
	str = PyUnicode_AsUTF8String(p);

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");

	printf("  length: %ld\n", len);
	printf("  value: %ls\n", PyBytes_AsString(str));
}


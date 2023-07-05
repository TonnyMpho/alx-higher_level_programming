#include <stdio.h>
#include <Python.h>

/**
 * print_python_string - function that prints Python strings
 * @p: Python object
 * Return: Void (nothing)
 */
void print_python_string(PyObject *p)
{
	py_ssize_t len;
	char *str;

	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	str = PyUnicode_AsUTF8AndSize(p, &len);

	printf("[.] string object info\n");

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");

	printf("  length: %zd\n", len);
	printf("  value: %s\n", str);
}


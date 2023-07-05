#include <stdio.h>
#include <Python.h>

/**
 * print_python_string - function that prints Python strings
 * @p: Python object
 * Return: Void (nothing)
 */
void print_python_string(PyObject *p)
{
	size_t len;
	char *str;

	printf("[.] string object info\n");

	if (strcmp(p->ob_type->tp_name, "str"))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	len = ((PyASCIIObject *)(p))->len;
	str = PyUnicode_AsWideCharString(p, &len);

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");

	printf("  length: %ld\n", len);
	printf("  value: %ls\n", str);
}


#include <stdio.h>
#include <Python.h>

/**
 * print_python_list - C functions that print some basic info
 * about Python lists
 * @p: pointer to python object
 * Return: Void (nothing)
 */
void print_python_list(PyObject *p)
{
	size_t size, i;
	PyListObject *list = (PyListObject *)p;
	PyObject *item;

	size = PyObject_Length(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		item = list->ob_item[i]->on_type->tp_name;

		printf("Element %d: %s\n", i, item);
		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}

/**
 * print_python_bytes - C function that print some basic info
 * about Python bytes objects.
 * @p: pointer to python object
 * Return: Void
 */
void print_python_bytes(PyObject *p)
{
	size_t size, i;
	char *bytes;

	printf("[.}] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf(" [ERROR] Invalid Bytes Object\n");
		return;
	}

	bytes = ((PyBytesObject *)p)->obval;
	size = ((PyVarObject *)p)->ob_size;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);

	printf("  first %ld bytes: ", size > 10 ? 10 : size);

	for (i = 0; i < (size > 10 ? 10 : size); i++)
	{
		printf("%02hhx", bytes[i]);
		if (i == ((size > 10) ? 9 : size - 1))
			printf("\n");
		else
			printf(" ");
	}
}

#include <stdio.h>
#include <Python.h>

void print_python_bytes(PyObject *p);
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

	size = ((PyVarObject *)p)->ob_size;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		item = ((PyListObject *)p)->ob_item[i];

		printf("Element %ld: %s\n", i, ((item)->ob_type)->tp_name);
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

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	bytes = ((PyBytesObject *)p)->ob_sval;
	size = ((PyVarObject *)p)->ob_size;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", bytes);

	printf("  first %ld bytes: ", size >= 10 ? 10 : size + 1);

	for (i = 0; i < (size >= 10 ? 10 : size + 1); i++)
	{
		printf("%02hhx", bytes[i]);
		if (i == ((size > 10) ? 9 : size - 1))
			printf("\n");
		else
			printf(" ");
	}
}

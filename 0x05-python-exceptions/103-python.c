#include <Python.h>
#include <stdio.h>

void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);
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

	fflush(stdout);
	printf("[*] Python list info\n");

	if (PyList_CheckExact(p))
	{
		printf("[*] Size of the Python List = %ld\n", size);
		printf("[*] Allocated = %ld\n", list->allocated);

		for (i = 0; i < size; i++)
		{
			item = ((PyListObject *)p)->ob_item[i];

			printf("Element %ld: %s\n", i, ((item)->ob_type)->tp_name);
			if (PyBytes_Check(item))
				print_python_bytes(item);
			else if (PyFloat_Check(item))
				print_python_float(item);
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
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

	fflush(stdout);
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

	if (size >= 10)
		size = 10;
	else
		size += 1;

	printf("  first %ld bytes: ", size);

	for (i = 0; i < size; i++)
	{
		printf("%02hhx", bytes[i]);
		if (i == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}

/**
 * print_python_float - C function that print some basic info about Python float objects.
 * @p: pointer to python object
 */
void print_python_float(PyObject *p)
{
	double value = 0;

	fflush(stdout);
	printf("[.] float object info\n");

	if (!PyObject_TypeCheck(p, &PyFloat_Type))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	if (PyFloat_Check(p))
		value = ((PyFloatObject *)p)->ob_fval;

	printf("  [.] Value: %f\n", value);
}

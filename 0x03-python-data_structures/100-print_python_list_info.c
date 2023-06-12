#include <Python.h>

/**
 * print_python_list_info - C function that prints
 * somebasic info about Python lists.
 *
 * @p: python Object
 * Return: Void
 */
void print_python_list_info(PyObject *p)
{
	size_t size = PyList_Size(p);
	size_t i;
	PyListObject *list = (PylistObject *)p;
	PyObject *item;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %li\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		item = Py_List_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

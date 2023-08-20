#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes_info - Prints basic info about a Python bytes object
 * @p: Pointer to the Python bytes object
*/

void print_python_bytes(PyObject *p)
{
	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p)) {
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	char *str;
	Py_ssize_t length, i;

	PyBytes_AsStringAndSize(p, &str, &length);
	printf("  size: %lu\n", length);
	printf("  trying string: %s\n", str);

	if (length > 10)
		length = 10;
	else
		length++;

	printf("  first %lu bytes: ", length);

	for (i = 0; i < length - 1; i++)
		printf("%02x ", str[i] & 0xff);

	printf("%02x\n", str[length - 1] & 0xff);

}

/**
 * print_python_list_info - Prints basic info about a Python list
 * @p: Pointer to the Python list object
*/

void print_python_list(PyObject *p)
{
	Py_ssize_t i;
	PyObject *list;

	if (PyList_Check(p))
	{
		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %lu\n", PyList_Size(p));
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

		for (i = 0; i < PyList_Size(p); i++)
		{
			list = PySequence_GetItem(p, i);

			printf("Element %lu: %s\n", i, list->ob_type->tp_name);

			if (strcmp(list->ob_type->tp_name, "bytes") == 0)
				print_python_bytes(list);
		}
	}
}

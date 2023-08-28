#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
#include <floatobject.h>
#include <string.h>

/**
 * print_python_bytes - Print information about Python bytes object.
 * @p: Pointer to PyObject p.
 */
void print_python_bytes(PyObject *p)
{
	size_t size, index;
	char *data;

	setbuf(stdout, NULL);
	printf("[.] Bytes object info\n");

	if (PyBytes_Check(p) == 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	data = ((PyBytesObject *)(p))->ob_sval;
	size = PyBytes_Size(p);

	printf("  size: %ld\n  trying string: %s\n", size, data);

	if (size >= 10)
		size = 10;

	printf("  first %ld bytes: ", size);

	for (index = 0; index < size - 1; index++)
		printf("%02hhx ", data[index]);

	printf("%02hhx\n", data[index]);
}

/**
 * print_python_float - Print information about Python float object.
 * @p: Pointer to PyObject p.
 */
void print_python_float(PyObject *p)
{
	char *str_repr;
	double value;

	setbuf(stdout, NULL);
	printf("[.] Float object info\n");

	if (PyFloat_Check(p) == 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	value = ((PyFloatObject *)(p))->ob_fval;
	str_repr = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);

	printf("  value: %s\n", str_repr);
}

/**
 * print_python_list - Print information about Python list object.
 * @p: Pointer to PyObject p.
 */
void print_python_list(PyObject *p)
{
	size_t allocated, list_size, index;
	const char *type_name;
	PyListObject *list;

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");

	if (PyList_Check(p) == 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	list = (PyListObject *)p;
	list_size = PyList_GET_SIZE(p);
	allocated = list->allocated;

	printf("[*] Size of the Python List = %ld\n[*] Allocated = %li\n", list_size, allocated);

	for (index = 0; index < list_size; index++)
	{
		type_name = (list->ob_item[index])->ob_type->tp_name;
		printf("Element %ld: %s\n", index, type_name);

		if (!strcmp(type_name, "bytes"))
		{
			print_python_bytes(list->ob_item[index]);
		}
		else if (!strcmp(type_name, "float"))
		{
			print_python_float(list->ob_item[index]);
		}
	}
}

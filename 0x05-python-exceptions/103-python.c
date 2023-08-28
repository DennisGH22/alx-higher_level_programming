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
	size_t byte_count, i;
	char *data;

	setbuf(stdout, NULL);
	printf("[.] Bytes object info\n");

	if (PyBytes_Check(p) == 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	data = ((PyBytesObject *)(p))->ob_sval;
	byte_count = PyBytes_Size(p);

	printf("  size: %ld\n  trying string: %s\n", byte_count, data);

	if (byte_count >= 10)
		byte_count = 10;

	printf("  first %ld bytes: ", byte_count);

	for (i = 0; i < byte_count - 1; i++)
		printf("%02hhx ", data[i]);

	printf("%02hhx\n", data[i]);
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
	size_t allocated, size, i;
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
	size = PyList_GET_SIZE(p);
	allocated = list->allocated;

	printf("[*] Size of the Python List = %ld\n[*] Allocated = %li\n", size, allocated);

	for (i = 0; i < size; i++)
	{
		type_name = (list->ob_item[i])->ob_type->tp_name;
		printf("Element %ld: %s\n", i, type_name);

		if (!strcmp(type_name, "bytes"))
		{
			print_python_bytes(list->ob_item[i]);
		}
		else if (!strcmp(type_name, "float"))
		{
			print_python_float(list->ob_item[i]);
		}
	}
}

#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
#include <floatobject.h>
#include <string.h>

/* Print information about Python bytes object */
void print_python_bytes(PyObject *p)
{
	size_t bytes_to_print, i;
	char *data;

	setbuf(stdout, NULL);
	printf("[.] Bytes object info\n");

	if (PyBytes_Check(p) == 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	data = ((PyBytesObject *)(p))->ob_sval;
	bytes_to_print = PyBytes_Size(p);

	printf("  size: %ld\n  trying string: %s\n", bytes_to_print, data);

	bytes_to_print >= 10 ? bytes_to_print = 10 : bytes_to_print++;

	printf("  first %ld bytes: ", bytes_to_print);

	for (i = 0; i < bytes_to_print - 1; i++)
	{
		printf("%02hhx ", data[i]);
	}

	printf("%02hhx\n", data[i]);
}

/* Print information about Python float object */
void print_python_float(PyObject *p)
{
	char *str;
	double value;

	setbuf(stdout, NULL);
	printf("[.] Float object info\n");

	if (PyFloat_Check(p) == 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	value = ((PyFloatObject *)(p))->ob_fval;
	str = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);

	printf("  value: %s\n", str);
}

/* Print information about Python list object */
void print_python_list(PyObject *p)
{
	size_t list_size, i;
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

	printf("[*] Size of the Python List = %ld\n", list_size);

	for (i = 0; i < list_size; i++)
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

#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
#include <floatobject.h>
#include <string.h>

/* Print information about Python bytes object */
void print_python_bytes(PyObject *py_obj)
{
	size_t bytes_to_print, index;
	char *data;

	setbuf(stdout, NULL);
	printf("[.] Bytes object info\n");

	if (PyBytes_Check(py_obj) == 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	data = ((PyBytesObject *)(py_obj))->ob_sval;
	bytes_to_print = PyBytes_Size(py_obj);

	printf("  size: %ld\n  trying string: %s\n", bytes_to_print, data);

	// Limit bytes_to_print to at most 10
	bytes_to_print >= 10 ? bytes_to_print = 10 : bytes_to_print++;

	printf("  first %ld bytes: ", bytes_to_print);

	for (index = 0; index < bytes_to_print - 1; index++)
	{
		printf("%02hhx ", data[index]);
	}

	printf("%02hhx\n", data[index]);
}

/* Print information about Python float object */
void print_python_float(PyObject *py_obj)
{
	char *str_repr;
	double value;

	setbuf(stdout, NULL);
	printf("[.] Float object info\n");

	if (PyFloat_Check(py_obj) == 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	value = ((PyFloatObject *)(py_obj))->ob_fval;
	str_repr = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);

	printf("  value: %s\n", str_repr);
}

/* Print information about Python list object */
void print_python_list(PyObject *py_obj)
{
	size_t list_size, index;
	const char *type_name;
	PyListObject *list;

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");

	if (PyList_Check(py_obj) == 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	list = (PyListObject *)py_obj;
	list_size = PyList_GET_SIZE(py_obj);

	printf("[*] Size of the Python List = %ld\n", list_size);

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

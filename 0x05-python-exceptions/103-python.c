#include <stdio.h>
#include <Python.h>

/**
 * print_python_list - Print information about a Python list.
 * @p: PyObject pointer to the list.
*/

void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		fprintf(stderr, "Error: Not a valid PyListObject\n");
		return;
	}

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
}

/**
 * print_python_bytes - Print information about a Python bytes object.
 * @p: PyObject pointer to the bytes object.
*/

void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "Error: Not a valid PyBytesObject\n");
		return;
	}

	printf("[.] bytes object info\n");
	printf("  [.] size: %ld\n", PyBytes_GET_SIZE(p));
	printf("  [.] trying string: %s\n", PyBytes_AsString(p));
}

/**
 * print_python_float - Print information about a Python float object.
 * @p: PyObject pointer to the float object.
*/

void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		fprintf(stderr, "Error: Not a valid PyFloatObject\n");
		return;
	}

	printf("[.] float object info\n");
	printf("  [.] value: %lf\n", PyFloat_AsDouble(p));
}

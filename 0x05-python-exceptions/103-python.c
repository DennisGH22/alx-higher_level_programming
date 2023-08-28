#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* Function prototypes */
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);
void print_python_list(PyObject *p);

/* Set stdout to unbuffered mode */
void set_unbuffered_stdout(void)
{
	setbuf(stdout, NULL);
}

/* Print error message for invalid object type */
void print_error_message(const char *type)
{
	fprintf(stderr, "[ERROR] Invalid %s Object\n", type);
}

/* Print information about Python bytes object */
void print_python_bytes(PyObject *p)
{
	size_t size, i;
	const char *str;
	PyBytesObject *bytes;

	set_unbuffered_stdout();
	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		print_error_message("Bytes");
		return;
	}

	bytes = (PyBytesObject *)p;
	size = PyBytes_Size(p);

	printf("  size: %ld\n  trying string: %s\n", size, bytes->ob_sval);

	size_t bytes_to_print = (size >= 10) ? 10 : size;
	printf("  first %zd bytes: ", bytes_to_print);

	for (i = 0; i < bytes_to_print - 1; i++)
		printf("%02hhx ", bytes->ob_sval[i]);
	printf("%02hhx\n", bytes->ob_sval[i]);
}

/* Print information about Python float object */
void print_python_float(PyObject *p)
{
	double value;
	char *str;

	set_unbuffered_stdout();
	printf("[.] float object info\n");

	if (!PyFloat_Check(p))
	{
		print_error_message("Float");
		return;
	}

	value = ((PyFloatObject *)(p))->ob_fval;
	str = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", str);
	PyMem_Free(str);
}

/* Print information about Python list object */
void print_python_list(PyObject *p)
{
	size_t size, i;
	const char *type_name;
	PyListObject *list;

	set_unbuffered_stdout();
	printf("[*] Python list info\n");

	if (!PyList_Check(p))
	{
		print_error_message("List");
		return;
	}

	list = (PyListObject *)p;
	size = PyList_GET_SIZE(p);

	printf("[*] Size of the Python List = %ld\n", size);

	for (i = 0; i < size; i++)
	{
		PyObject *item = list->ob_item[i];
		type_name = item->ob_type->tp_name;
		printf("Element %ld: %s\n", i, type_name);

		if (strcmp(type_name, "bytes") == 0)
			print_python_bytes(item);
		else if (strcmp(type_name, "float") == 0)
			print_python_float(item);
	}
}

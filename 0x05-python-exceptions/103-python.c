#include <Python.h>
#include <stdio.h>

void print_python_bytes(PyObject *obj);
void print_python_float(PyObject *obj);
void print_python_list(PyObject *obj);

void set_unbuffered_stdout(void)
{
	setbuf(stdout, NULL);
}

void print_error_message(const char *type)
{
	fprintf(stderr, "[ERROR] Invalid %s Object\n", type);
}

void print_bytes_info(PyBytesObject *bytes)
{
	size_t bytes_to_print = PyBytes_Size(bytes) >= 10 ? 10 : PyBytes_Size(bytes);

	printf("  size: %ld\n  trying string: %s\n", PyBytes_Size(bytes), bytes->ob_sval);
	printf("  first %zd bytes: ", bytes_to_print);

	for (size_t i = 0; i < bytes_to_print; i++)
	{
		printf("%02hhx ", bytes->ob_sval[i]);
	}
	printf("\n");
}

void print_float_info(PyFloatObject *flt)
{
	char *str = PyOS_double_to_string(flt->ob_fval, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", str);
	PyMem_Free(str);
}

void print_list_info(PyListObject *list)
{
	size_t size = PyList_GET_SIZE(list);
	size_t allocated = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n[*] Allocated = %li\n", size, allocated);

	for (size_t i = 0; i < size; i++)
	{
		PyObject *item = list->ob_item[i];
		const char *type_name = item->ob_type->tp_name;

		printf("Element %ld: %s\n", i, type_name);

		if (strcmp(type_name, "bytes") == 0)
		{
			print_python_bytes(item);
		}
		else if (strcmp(type_name, "float") == 0)
		{
			print_python_float(item);
		}
	}
}

void print_python_bytes(PyObject *obj)
{
	set_unbuffered_stdout();
	printf("[.] bytes object info\n");

	if (PyBytes_Check(obj))
	{
		print_bytes_info((PyBytesObject *)obj);
	}
	else
	{
		print_error_message("Bytes");
	}
}

void print_python_float(PyObject *obj)
{
	set_unbuffered_stdout();
	printf("[.] float object info\n");

	if (PyFloat_Check(obj))
	{
		print_float_info((PyFloatObject *)obj);
	}
	else
	{
		print_error_message("Float");
	}
}

void print_python_list(PyObject *obj)
{
	set_unbuffered_stdout();
	printf("[*] Python list info\n");

	if (PyList_Check(obj))
	{
		print_list_info((PyListObject *)obj);
	}
	else
	{
		print_error_message("List");
	}
}

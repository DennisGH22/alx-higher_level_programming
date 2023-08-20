#include <Python.h>

/**
 * print_python_list - Prints information about a Python list.
 * @p: The PyObject representing the Python list.
*/

void print_python_bytes(PyObject *p)
{
    printf("[.] bytes object info\n");

    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    char *str;
    Py_ssize_t length;

    PyBytes_AsStringAndSize(p, &str, &length);

    printf("  size: %lu\n", length);
    printf("  trying string: %s\n", str);

    Py_ssize_t print_length = (length > 10) ? 10 : length;
    printf("  first %lu bytes: ", print_length);
    for (Py_ssize_t i = 0; i < print_length; i++)
    {
        printf("%02x ", str[i] & 0xff);
    }
    printf("\n");
}

/**
 * print_python_bytes - Prints information about a Python bytes object.
 * @p: The PyObject representing the Python bytes object.
*/

void print_python_list(PyObject *p)
{

    if (!PyList_Check(p))
    {
        printf("Invalid Python object. Please provide a Python list.\n");
        return;
    }

	const char *item_type_name;
	PyObject *list_item;

    printf("[*] Python list info\n");

    Py_ssize_t size = PyList_Size(p);
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (Py_ssize_t i = 0; i < size; i++)
    {
        list_item = PyList_GetItem(p, i);
        item_type_name = list_item->ob_type->tp_name;

        printf("Element %ld: %s\n", i, item_type_name);

        if (strcmp(item_type_name, "bytes") == 0)
        {
            print_python_bytes(list_item);
        }
    }
}

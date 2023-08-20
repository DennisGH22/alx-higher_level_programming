#include <stdio.h>
#include <Python.h>

/**
 * print_python_list - Prints information about a Python list.
 * @p: The PyObject representing the Python list.
*/

void print_python_list(PyObject *p)
{
    if (PyList_Check(p))
    {
        Py_ssize_t size = PyList_Size(p);
        PyObject *item;

        printf("[*] Python list info\n");
        printf("[*] Size of the Python List = %ld\n", size);
        printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

        for (Py_ssize_t i = 0; i < size; i++)
        {
            item = PyList_GetItem(p, i);
            printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
        }
    }
    else
    {
        fprintf(stderr, "  [ERROR] Invalid List Object\n");
    }
}

/**
 * print_python_bytes - Prints information about a Python bytes object.
 * @p: The PyObject representing the Python bytes object.
*/

void print_python_bytes_info(PyObject *p)
{
    if (!PyBytes_Check(p))
    {
        printf("[.] bytes object info\n");
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    printf("[.] bytes object info\n");

    char *str = PyBytes_AsString(p);
    Py_ssize_t length = PyBytes_Size(p);
    Py_ssize_t print_length = (length > 10) ? 10 : length;

    printf("  size: %ld\n", length);
    printf("  trying string: %s\n", str);

    printf("  first %ld bytes: ", print_length);
    for (Py_ssize_t i = 0; i < print_length; i++)
    {
        printf("%02x", str[i] & 0xff);
        if (i < print_length - 1)
            printf(" ");
    }
    printf("\n");
}

void print_python_list_info(PyObject *p)
{
    if (!PyList_Check(p))
    {
        printf("[*] Invalid Python object. Please provide a Python list.\n");
        return;
    }

    printf("[*] Python list info\n");

    Py_ssize_t size = PyList_Size(p);
    printf("[*] Size of the Python List = %ld\n", size);

    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (Py_ssize_t i = 0; i < size; i++)
    {
        PyObject *list_item = PyList_GetItem(p, i);
        const char *item_type_name = list_item->ob_type->tp_name;
        printf("Element %ld: %s\n", i, item_type_name);

        if (strcmp(item_type_name, "bytes") == 0)
        {
            print_python_bytes_info(list_item);
        }
    }
}

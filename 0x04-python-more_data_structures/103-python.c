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

void print_python_bytes(PyObject *p)
{
    if (PyBytes_Check(p))
    {
        printf("[.] bytes object info\n");
        printf("  [.] size: %ld\n", PyBytes_Size(p));
        printf("  [.] trying string: %s\n", PyBytes_AS_STRING(p));
        printf("  [.] first %ld bytes: ", PyBytes_Size(p) < 10 ? PyBytes_Size(p) : 10);

        for (Py_ssize_t i = 0; i < (Py_ssize_t)PyBytes_Size(p) && i < 10; i++)
        {
            printf("%02x", (unsigned char)PyBytes_AS_STRING(p)[i]);
            if (i < (Py_ssize_t)PyBytes_Size(p) - 1 && i < 9)
                printf(" ");
        }
        printf("\n");
    }
    else
    {
        fprintf(stderr, "  [ERROR] Invalid Bytes Object\n");
    }
}

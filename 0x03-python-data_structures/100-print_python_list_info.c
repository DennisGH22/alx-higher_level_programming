#include <Python.h>

/**
 * print_python_list_info - Prints basic info about a Python list
 * @p: Pointer to the Python list object
*/

void print_python_list_info(PyObject *p)
{
    if (!PyList_Check(p))
    {
        printf("Invalid Python object. Please provide a Python list.\n");
        return;
    }

    Py_ssize_t size = PyList_Size(p);
    printf("[*] Size of the Python List = %ld\n", size);

    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (Py_ssize_t i = 0; i < size; i++)
    {
        PyObject *item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

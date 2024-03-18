#include <Python.h>
#include <stdio.h>

/**
 * print_item_info - Displays the info of items of a python list
 * @prmItem: item of a python object
 * @prmItemIndex: item index
 *
 * Return: void
 */
void print_item_info(PyObject *prmItem, int prmItemIndex)
{
	char *iname;

	iname = (char *)Py_TYPE(PrmItem)->tp_name;
	printf("Element %d: %s\n", prmItemIndex, iname);
}
/**
 * print_python_list_info - displays all item info from a python object
 * @p: python object
 *
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	PyObject *item;
	int it_idx, obj_allo = 0;
	Py_ssize_t obj_size = 0;

	if (PyList_Check(p))
	{
		obj_size = PyList_Size(p);
		obj_allo = ((PyListObject *)p)->allocated;
		printf("[*] Size of the Python List = %d\n", (int) obj_size);
		printf("[*] Allocated = %d\n", obj_allo);

		for (it_idx = 0; it_idx < obj_size; it_idx++)
		{
			item = PyList_GetItem(p, it_idx);
			print_item_info(item, it_idx);
		}
	}
}

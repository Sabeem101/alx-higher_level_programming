#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - checks lists
 * @list: list
 * Return: 0 if ther is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *cur, *chk;

	cur = list;
	chk = list;
	if (list == NULL)
	{
		return (0);
	}
	chk = chk->next;
	while (chk != NULL && chk->next != NULL && cur != NULL)
	{
		if (cur == chk)
		{
			return (1);
		}
		cur = cur->next;
		chk = chk->next->next;
	}
	return (0);
}

#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: first node
 *
 * Return: 1 on success, 0 if failed
 */
int is_palindrome(listint_t **head)
{
	int vals[2048], x = 0, limit, lp;
	listint_t *tmp = *head;

	if (head == NULL || *head == NULL)
	{
		return (1);
	}
	while (tmp != NULL)
	{
		vals[x] = tmp->n;
		x++;
		tmp = tmp->next;
	}
	limit = (x % 2 == 0) ? x / 2 : (x + 1) / 2;
	for (lp = 0; lp < limit; lp++)
		if (vals[lp] != vals[x - 1 - lp])
			return (0);
	return (1);
}

#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - insert node in a linked list
 * @head: pointer to the head of the linked list
 * @number: value of the new node
 *
 * Return: head of the linked list including the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nhead = malloc(sizeof(listint_t));
	listint_t *temp = *head;

	if (nhead == NULL)
		return (NULL);
	if (temp == NULL)
	{
		nhead->n = number;
		nhead->next = NULL;
		(*head) = nhead;
		return (nhead);
	}
	if (temp->next == NULL || number == 0)
	{
		if (number < temp->n)
		{
			nhead->n = number;
			nhead->next = temp;
			(*head) = nhead;
			return (nhead);
		}
	}
	while (temp->next)
	{
		if ((number >= temp->n) && (number <= temp->next->n))
		{
			nhead->n = number;
			nhead->next = temp->next;
			temp->next = nhead;
			return (nhead);
		}
		temp = temp->next;
	}
	nhead->n = number;
	nhead->next = NULL;
	temp->next = nhead;
	return (nhead);
}

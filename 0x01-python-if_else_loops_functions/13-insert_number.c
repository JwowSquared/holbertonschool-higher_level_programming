#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
* insert_node - creates a new node at its rightful spot in a list
* @head: double pointer to list head
* @number: n value of new node to create
*
* Return: pointer to new node, else NULL
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *itr, *prev, *new;

	if (head == NULL)
		return (NULL);

	prev = *head;

	if (prev == NULL || number < prev->n)
	{
		new = malloc(sizeof(listint_t));
		if (new == NULL)
			return (NULL);
		new->next = prev;
		new->n = number;
		*head = new;
		return (new);
	}

	itr = (*head)->next;

	while (itr != NULL)
	{
		if (number < itr->n)
			break;
		prev = itr;
		itr = itr->next;
	}

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->next = itr;
	prev->next = new;
	new->n = number;
	return (new);
}

#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - function in C that inserts a number
 * into a sorted singly linked list
 * @head: the start of the list
 * @number: The number to insert
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head;
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;

	if (node == NULL)
	{
		new_node->next = node;
		*head = new_node;
		return (new_node);
	}

	while (node && node->next)
	{
		node = node->next;
	}

	new_node->next = node->next;
	node->next = new_node;

	return (new_node);
}

#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - function in C that checks
 * if a singly linked list is a palindrome.
 *
 * @head: head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev = NULL;
	listint_t *curr, *next;
	listint_t *f_half = *head;
	listint_t *s_half;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast && fast->next)
	{
		fast = fast->next->next;
		slow = slow->next;
	}

	curr = slow;

	while (curr)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}

	s_half = prev;

	while (s_half)
	{
		if (f_half->n != s_half->n)
			return (0);

		f_half = f_half->next;
		s_half = s_half->next;
	}

	return (1);
}

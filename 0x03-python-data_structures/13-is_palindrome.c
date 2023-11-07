#include "lists.h"
/**
 * is_palindrome - check if linked list is palindrome
 * @head: pointer to linked list head
 *
 * Return: 1-palidrome or 0-not palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *original;
	listint_t *reverse = NULL;
	listint_t *temp;

	original = *head;
	while (original)
	{
		temp = original->next;
		original->next = reverse;
		reverse = original;
		original = temp;
	}
	original = *head;
	while (original && reverse)
	{
		if (original->n != reverse->n)
			return (0);
		original = original->next;
		reverse = reverse->next;
	}
	return (1);
}

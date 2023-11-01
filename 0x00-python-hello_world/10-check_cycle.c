#include "lists.h"
/**
 * check_cycle - check if linked list contain loop
 * @list: pointer to linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *step1_ptr = list, *step2_ptr = list;

	while (step1_ptr &&  step2_ptr && step2_ptr->next)
	{
		step1_ptr = step1_ptr->next;
		step2_ptr = step2_ptr->next->next;
		if (step1_ptr == step2_ptr)
			return (1);
	}
	return (0);
}

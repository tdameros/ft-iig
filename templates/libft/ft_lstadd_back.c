/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstadd_back.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tdameros <tdameros@student.42lyon.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/10/11 18:35:36 by tdameros          #+#    #+#             */
/*   Updated: 2022/10/11 20:09:53 by tdameros         ###   ########lyon.fr   */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <string.h>

typedef struct s_list
{
	void			*content;
	struct s_list	*next;
}	t_list;

void ft_lstadd_back(t_list **lst, t_list *new);

void	ft_print_lst(t_list	*lst)
{
	while (lst != NULL)
	{
		printf("%s", (char *) lst->content);
		if (lst->next != NULL)
			printf("->");
		lst = lst->next;
	}
}

void	testnull(char *node_name)
{
	t_list	*node1 = NULL;
	t_list	new_node = {node_name, NULL};
	ft_lstadd_back(&node1, &new_node);
	ft_print_lst(node1);
}

void	test1(char	*node_name)
{
	t_list	node1 = {"node1", NULL};
	t_list	new_node = {node_name, NULL};
	t_list	*lst = &node1;
	ft_lstadd_back(&lst, &new_node);
	ft_print_lst(lst);
}

void	test2(char	*node_name)
{
	t_list	node2 = {"node2", NULL};
	t_list	node1 = {"node1", &node2};
	t_list	new_node = {node_name, NULL};
	t_list	*lst = &node1;
	ft_lstadd_back(&lst, &new_node);
	ft_print_lst(lst);
}

void	test3(char	*node_name)
{
	t_list	node3 = {"node3", NULL};
	t_list	node2 = {"node2", &node3};
	t_list	node1 = {"node1", &node2};
	t_list	new_node = {node_name, NULL};
	t_list	*lst = &node1;
	ft_lstadd_back(&lst, &new_node);
	ft_print_lst(lst);
}

int	main(int argc,	char **argv)
{
	if (argc == 3)
	{
		if (!strcmp(argv[1], "NULL"))
			testnull(argv[2]);
		else if (!strcmp(argv[1], "node1"))
			test1(argv[2]);
		else if (!strcmp(argv[1], "node1->node2"))
			test2(argv[2]);
		else if (!strcmp(argv[1], "node1->node2->node3"))
			test3(argv[2]);
	}
	return (0);
}

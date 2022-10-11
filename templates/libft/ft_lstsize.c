/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstsize.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tdameros <tdameros@student.42lyon.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/10/11 18:35:36 by tdameros          #+#    #+#             */
/*   Updated: 2022/10/11 18:59:28 by tdameros         ###   ########lyon.fr   */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <string.h>

typedef struct s_list
{
	void			*content;
	struct s_list	*next;
}	t_list;

int ft_lstsize(t_list *lst);

void	testnull()
{
	t_list	*node1 = NULL;
	printf("%d", ft_lstsize(node1));
}

void	test1()
{
	t_list	node1 = {"node1", NULL};
	printf("%d", ft_lstsize(&node1));
}

void	test2()
{
	t_list	node2 = {"node2", NULL};
	t_list	node1 = {"node1", &node2};
	printf("%d", ft_lstsize(&node1));
}

void	test3()
{
	t_list	node3 = {"node3", NULL};
	t_list	node2 = {"node2", &node3};
	t_list	node1 = {"node1", &node2};
	printf("%d", ft_lstsize(&node1));
}

int	main(int argc,	char **argv)
{
	if (argc == 2)
	{
		if (!strcmp(argv[1], "NULL"))
			testnull();
		else if (!strcmp(argv[1], "node1"))
			test1();
		else if (!strcmp(argv[1], "node1->node2"))
			test2();
		else if (!strcmp(argv[1], "node1->node2->node3"))
			test3();
	}
	return (0);
}

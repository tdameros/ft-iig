/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstnew.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tdameros <tdameros@student.42lyon.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/10/11 15:53:54 by tdameros          #+#    #+#             */
/*   Updated: 2022/10/11 16:24:40 by tdameros         ###   ########lyon.fr   */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>

typedef struct s_list
{
	void			*content;
	struct s_list	*next;
}	t_list;

t_list	*ft_lstnew(void *content);

int	main(int argc, char **argv)
{
	t_list	*node;

	if (argc == 2)
	{
		node = ft_lstnew(argv[1]);
		if (node != NULL)
		{
			printf("%s", (char *) node->content);
			free(node);
		}
	}	
}

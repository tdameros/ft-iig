/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tdameros <tdameros@student.42lyon.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/10/09 16:16:02 by tdameros          #+#    #+#             */
/*   Updated: 2022/10/09 16:59:00 by tdameros         ###   ########lyon.fr   */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include <stdio.h>

char **ft_split(char const *s, char c);

void	display_tab(char **tab)
{
	size_t	index;

	index = 0;
	printf("{");
	while (tab[index] != NULL)
	{
		printf("%s", tab[index]);	
		free(tab[index]);
		if (tab[index + 1] != NULL)
			printf(", ");
		index++;
	}
	printf("}");
	free(tab);
}

int	main(int argc, char **argv)
{
	char	**split_tab;

	if (argc == 3)
	{
		split_tab = ft_split(argv[1], argv[2][0]);		
		display_tab(split_tab);
	}
}

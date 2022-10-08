/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strtrim.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tdameros <tdameros@student.42lyon.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/10/08 23:55:03 by tdameros          #+#    #+#             */
/*   Updated: 2022/10/08 23:56:39 by tdameros         ###   ########lyon.fr   */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>

char	*ft_strtrim(char const *s1, char const *set);

int	main(int argc, char **argv)
{
	char	*s;

	if (argc == 3)
	{
		s = ft_strtrim(argv[1], argv[2]);
		if (s != NULL)
		{
			printf("%s", s);
			free(s);
		}
	}
}

/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tdameros <tdameros@student.42lyon.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/10/08 22:01:02 by tdameros          #+#    #+#             */
/*   Updated: 2022/10/10 23:19:04 by tdameros         ###   ########lyon.fr   */
/*                                                                            */
/* ************************************************************************** */

#include <string.h>
#include <stdio.h>
#include <stdlib.h>

char	*ft_strdup(const char *s);

int	main(int argc, char **argv)
{
	char	*s_dup;

	if (argc == 2)
	{
		s_dup = ft_strdup(argv[1]);
		if (s_dup == argv[1])
			printf("Not a dup string");
		else
			printf("%s", s_dup);
		free(s_dup);
	}
}

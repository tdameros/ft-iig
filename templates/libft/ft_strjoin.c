/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strjoin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tdameros <tdameros@student.42lyon.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/10/08 23:24:05 by tdameros          #+#    #+#             */
/*   Updated: 2022/10/10 23:18:46 by tdameros         ###   ########lyon.fr   */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>

char	*ft_strjoin(char const *s1, char const *s2);

int	main(int argc, char **argv)
{
	char	*strjoin;

	if (argc == 3)
	{
		strjoin = ft_strjoin(argv[1], argv[2]);
		if (strjoin != NULL)
		{
			printf("%s", strjoin);
			free(strjoin);
		}
	}
}

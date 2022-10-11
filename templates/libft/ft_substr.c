/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_substr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tdameros <tdameros@student.42lyon.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/10/08 22:47:33 by tdameros          #+#    #+#             */
/*   Updated: 2022/10/10 23:19:14 by tdameros         ###   ########lyon.fr   */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>

char	*ft_substr(char const *s, unsigned int start, size_t len);

int	main(int argc, char **argv)
{
	unsigned int	start;
	size_t			len;
	char			*substr;

	if (argc == 4)
	{
		start = atoi(argv[2]);
		len = atoi(argv[3]);
		substr = ft_substr(argv[1], start, len);
		if (substr != NULL)
		{
			printf("%s", substr);
			free(substr);
		}
	}
}

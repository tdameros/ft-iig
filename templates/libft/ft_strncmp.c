/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strncmp.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tdameros <tdameros@student.42lyon.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/10/07 11:31:08 by tdameros          #+#    #+#             */
/*   Updated: 2022/10/07 11:41:56 by tdameros         ###   ########lyon.fr   */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>

int	ft_strncmp(const char *s1, const char *s2, size_t n);

int	main(int argc, char **argv)
{
	int	result;

	if (argc == 4)
	{
		result = ft_strncmp(argv[1], argv[2], atoi(argv[3]));
		if (result < 0)
			result = -1;
		else if (result > 0)
			result = 1;
		else
			result = 0;
		printf("%d", result);
	}
	return (0);
}

/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcpy.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tdameros <tdameros@student.42lyon.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/10/06 22:29:35 by tdameros          #+#    #+#             */
/*   Updated: 2022/10/06 23:01:09 by tdameros         ###   ########lyon.fr   */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>


size_t	ft_strlcpy(char *dst, const char *src, size_t size);

int	main(int argc, char **argv)
{
	size_t	result;
	char	dest[100];

	if (argc == 4)	
	{
		result = ft_strlcpy(dest, argv[2], atoi(argv[3])); 
		printf("%s|%zu", dest, result);
	}
	return (0);
}

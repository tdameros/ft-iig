/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tdameros <tdameros@student.42lyon.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/10/06 23:19:53 by tdameros          #+#    #+#             */
/*   Updated: 2022/10/07 11:07:15 by tdameros         ###   ########lyon.fr   */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

size_t	ft_strlcat(char *dst, const char *src, size_t size);

int	main(int argc, char **argv)
{
	size_t	result;
	char	dest[100];

	(void) argc;
	strcpy(dest, argv[1]);
	result = ft_strlcat(dest, argv[2], atoi(argv[3]));
	printf("%s|%zu", dest, result);
}

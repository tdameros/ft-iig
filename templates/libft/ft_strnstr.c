/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strnstr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tdameros <tdameros@student.42lyon.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/10/07 13:22:01 by tdameros          #+#    #+#             */
/*   Updated: 2022/10/07 14:15:56 by tdameros         ###   ########lyon.fr   */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>

/*
 * Find the first occurrence of find in s, where the search is limited to the
 * first slen characters of s.
 */
char	*ft_strnstr(const char *s1, const char *s2, size_t n);

int	main(int argc, char **argv)
{
	if (argc == 4)
	{
		printf("%s", ft_strnstr(argv[1], argv[2], atoi(argv[3])));
	}
}

/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_calloc.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tdameros <tdameros@student.42lyon.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/10/08 21:01:44 by tdameros          #+#    #+#             */
/*   Updated: 2022/10/08 22:05:37 by tdameros         ###   ########lyon.fr   */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include <stdio.h>

void	*ft_calloc(size_t nmemb, size_t size);

void	print_bytes(void *s, size_t n)
{
	unsigned char	*ptr;
	size_t			index;

	ptr = (unsigned char *) s;
	index = 0;
	while (index < n)
	{
		printf("%d|", *ptr);
		ptr++;
		index++;
	}
}

int	main(int argc, char **argv)
{
	void	*ptr;
	int		nmemb;
	int		size;

	if (argc == 3)
	{
		nmemb = atoi(argv[1]);
		size = atoi(argv[2]);
		ptr = ft_calloc(nmemb, size);
		print_bytes(ptr, nmemb * size);
		if (ptr != NULL)
			free(ptr);
	}
}

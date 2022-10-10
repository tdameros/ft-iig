/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tdameros <tdameros@student.42lyon.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/10/10 23:12:51 by tdameros          #+#    #+#             */
/*   Updated: 2022/10/10 23:16:33 by tdameros         ###   ########lyon.fr   */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>

char	*ft_itoa(int n);

int	main(int argc, char **argv)
{
	char	*s_nbr;

	if (argc == 2)
	{
		s_nbr = ft_itoa(atoi(argv[1]));
		if (s_nbr != NULL)
		{
			printf("%s", s_nbr);
			free(s_nbr);
		}
	}	
	return (0);
}

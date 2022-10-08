/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tdameros <tdameros@student.42lyon.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/10/07 11:13:18 by tdameros          #+#    #+#             */
/*   Updated: 2022/10/07 11:20:31 by tdameros         ###   ########lyon.fr   */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

char	*ft_strchr(const char *s, int c);

int	main(int argc, char **argv)
{
	if (argc == 3)
		printf("%s", ft_strchr(argv[1], argv[2][0]));
	return (0);
}

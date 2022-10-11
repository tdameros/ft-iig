/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putendl_fd.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tdameros <tdameros@student.42lyon.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/10/11 13:25:04 by tdameros          #+#    #+#             */
/*   Updated: 2022/10/11 14:45:38 by tdameros         ###   ########lyon.fr   */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

void	ft_putendl_fd(char *s, int fd);

int	main(int argc, char **argv)
{
	int		fd;

	if (argc == 3)
	{
		fd = atoi(argv[2]);
		ft_putendl_fd(argv[1], fd);
	}
}

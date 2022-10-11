/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putchar_fd.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tdameros <tdameros@student.42lyon.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/10/11 13:25:04 by tdameros          #+#    #+#             */
/*   Updated: 2022/10/11 14:45:47 by tdameros         ###   ########lyon.fr   */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

void	ft_putchar_fd(char c, int fd);

int	main(int argc, char **argv)
{
	int		fd;

	if (argc == 3)
	{
		fd = atoi(argv[2]);
		ft_putchar_fd(argv[1][0], fd);
	}
}

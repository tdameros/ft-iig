#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include "get_next_line_bonus.h"

int	main(int argc, char **argv)
{
	int		files[argc - 2];
	int		index_fd;
	char	*line;


	if (argc >= 3)
	{
		index_fd = 0;
		while (index_fd < argc - 2)
		{
			files[index_fd] = open(argv[index_fd + 1], O_RDWR);
			index_fd++;
		}
		index_fd = 0;
		for (int i = 0; i < atoi(argv[argc - 1]); i++)
		{
			line = get_next_line(files[index_fd]);
			printf("%s", line);
			free(line);
			index_fd = (index_fd + 1) % (argc - 2);
		}
		index_fd = 0;
		while (index_fd < argc - 2)
			close(files[index_fd++]);
	}
	return (0);
}


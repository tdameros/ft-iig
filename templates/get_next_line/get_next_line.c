#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include "get_next_line.h"

int	main(int argc, char **argv)
{
	int		fd;
	char	*line;

	if (argc == 3)
	{
		fd = open(argv[1], O_RDWR);
        for (int i = 0; i < atoi(argv[2]); i++)
        {
            line = get_next_line(fd);
            printf("%s", line);
            free(line);
        }
        close(fd);
	}
	return (0);
}


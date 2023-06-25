#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include "calorie.h"

char	*ft_realloc(char *old, int old_size, int new_size)
{
	char	*new;
	int		i;

	new = malloc(sizeof(char) * new_size);
	if (new == NULL)
		return (new);
	i = 0;
	while (i < old_size)
	{
		new[i] = old[i];
		i++;
	}	
	free (old);
	return (new);
}

t_str	read_file(int fd)
{
	int		i;
	t_str	str;
	char	current;
	t_str	new;

	i = 0;
	str = malloc(sizeof(char) * 11);
	if (str == NULL)
		return (str);
	while (read(fd, &current, 1) != 0)
	{
		str[i] = current;
		if (++i % 10 == 0)
		{
			new = ft_realloc(str, i + 1, sizeof(char) * i + 11);
			if (new != NULL)
				str = new;
			else
				return (str);
		}
	}
	str[i] = '\0';
	return (str);
}

t_str	open_and_read(char *file_name)
{
	int		fd;
	t_str	str;

	fd = open(file_name, O_RDONLY);
	if (fd != -1)
	{
		str = read_file(fd);
		if (close(fd) == -1)
		{
			printf("File error.");
			exit(0);
		}
		return (str);
	}
	printf("File error.");
	exit (0);
}
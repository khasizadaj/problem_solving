#include "calorie.h"
#include <stdio.h>

int	find_highest_calorie(t_str str);
t_str	open_and_read(char *file_name);

int	main(int argc, char **argv)
{
	t_str	content;
	int		highest_calorie;
	
	if (argc == 2)
	{
		content = open_and_read(argv[1]);
		highest_calorie = find_highest_calorie(content);
		printf("Highest calorie:\t%d\n", highest_calorie);
	}
	else
		printf("Please provide input file.");
}
#include "calorie.h"

int	find_highest_calorie(t_str str);

int	main(int argc, char **argv)
{
	t_str	content;
	int		highest_calorie;
	

	if (argc == 2)
	{
		// TODO Implement reading logic; 
		content = "1000\n2000\n3000\n\n4000\n\n5000\n";
		// content = read_input();
		highest_calorie = find_highest_calorie(content);
	}
}
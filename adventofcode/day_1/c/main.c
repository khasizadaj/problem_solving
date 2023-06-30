#include "helper.h"
#include "libs.h"

t_int_array	find_highest_calorie(t_str str, int count);
int	sum_highest_calories(t_int_array highest_calories, int count);
t_str	open_and_read(char *file_name);

int	main(int argc, char **argv)
{
	t_str			content;
	t_int_array		highest_calories;

	if (argc == 2)
	{
		content = open_and_read(argv[1]);
		highest_calories = find_highest_calorie(content, 1);
		printf("Highest calorie:\t%d\n", highest_calories[0]);
	}
	else if (argc == 3)
	{
		int sum;
		int count_of_highest;
		content = open_and_read(argv[1]);
		count_of_highest = ft_atoi(argv[2]);
		// TODO use atoi to change string to number
		highest_calories = find_highest_calorie(content, count_of_highest);
		sum = sum_highest_calories(highest_calories, count_of_highest);
		printf("Sum of %d highest calories:\t%d\n", count_of_highest, sum);
	}
	else
		printf("Please provide input file.");
}
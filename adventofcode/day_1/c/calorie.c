#include "helper.h"
#include "libs.h"

int	sum_highest_calories(t_int_array highest_calories, int count)
{
	int	sum;
	int	i;

	i = 0;
	sum = 0;
	while (i < count)
	{
		sum += highest_calories[i];
		i++;	
	}
	return (sum);
}

int	*get_highest_calories_array(int count)
{
	t_int_array	highest_calories;
	int	i;

	highest_calories = malloc(sizeof(int) * count);
	i = -1;
	while (++i < count)
	{
		highest_calories[i] = 0;
	}
	
	return highest_calories;
}

void	update_highest_calories(int curr_sum_calorie, t_int_array highest_calories, int count)
{
	int	i;
	int	temp;

	highest_calories[0] = curr_sum_calorie;

	i = 0;
	while (i < count - 1)
	{
		if (highest_calories[i] > highest_calories[i + 1])
		{
			temp = highest_calories[i];
			highest_calories[i] = highest_calories[i + 1];
			highest_calories[i + 1] = temp;
		}
		i++;
	}
}

t_int_array	find_highest_calorie(t_str str, int count)
{
	int			curr_sum_calorie;
	int			start;
	int			end;
	int			i;
	t_int_array	highest_calories;

	highest_calories = get_highest_calories_array(count);
	i = 0;
	end = -1;
	start = 0;
	curr_sum_calorie = 0;
	while (str[i])
	{
		if (str[i] == '\n')
		{
			start = end + 1;
			end = i;
			curr_sum_calorie += ft_atoi_loc(str, start, end);
			// it doesn't work when there is no new line character at the
			// end of the string
			if (str[i + 1] == '\n' || str[i + 1] == '\0')
			{
				if (curr_sum_calorie >= highest_calories[0])
					update_highest_calories(curr_sum_calorie, highest_calories, count);
				curr_sum_calorie = 0;
				i++;
			}
		}
		i++;
	}
	return (highest_calories);
}
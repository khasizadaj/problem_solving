#include "calorie.h"
#include <stdio.h>

/*
	init: max_sum_calorie;
	init: curr_sum_calorie;
	init: i;
	inti: start;
	init: end;
	Loop over string (with new lines)
		if str[i] is new line:
			start = end;
			end = i;
			convert string to number
			add to curr_sum_calorie

		when double newline,
			if curr_sum_calorie > max_sum_calorie:
				update max_sum_calorie
			reset curr_sum_calorie
*/

int	is_numeric(char c)
{
	return (c >= '0' && c <= '9');
}

int	is_space(char c)
{
	if (c != '\f' && c != '\n' && c != '\r'
		&& c != '\t' && c != '\v' && c != 32 && c != ' ')
		return (0);
	return (1);
}

int	ft_atoi(t_str str)
{
	int	number;
	int	sign;
	int	i;

	sign = 1;
	i = 0;
	number = 0;
	while (str[i])
	{
		while (is_space(str[i]) == 1)
			i++;
		if (str[i] == '-' || str[i] == '+')
		{
			if (str[i] == '-')
				sign *= -1;
			i++;
		}

		while (is_numeric(str[i]) != 0)
		{
			number = number * 10 + (str[i] - '0');
			i++;
		}
	}
	return (number * sign);
}

int	ft_atoi_loc(t_str str, int start, int end)
{
	int	number;
	int	sign;
	int	i;

	sign = 1;
	i = start;
	number = 0;
	while (str[i] && (i >= start && i < end))
	{
		while (is_space(str[i]) == 1)
			i++;
		if (str[i] == '-' || str[i] == '+')
		{
			if (str[i] == '-')
				sign *= -1;
			i++;
		}

		while (is_numeric(str[i]) != 0)
		{
			number = number * 10 + (str[i] - '0');
			i++;
		}
	}
	return (number * sign);
}

int	find_highest_calorie(t_str str)
{
	int	max_sum_calorie;
	int	curr_sum_calorie;
	int	start;
	int	end;
	int	i;

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
				if (curr_sum_calorie >= max_sum_calorie)
					max_sum_calorie = curr_sum_calorie;
				curr_sum_calorie = 0;
				i++;
			}
		}
		i++;
	}
	return (max_sum_calorie);
}
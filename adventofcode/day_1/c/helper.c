#include "libs.h"
#include "helper.h"

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
#ifndef HELPER_H
# define HELPER_H

typedef char* t_str;
typedef int* t_int_array;

int	is_numeric(char c);
int	is_space(char c);
int	ft_atoi(t_str str);
int	ft_atoi_loc(t_str str, int start, int end);

#endif
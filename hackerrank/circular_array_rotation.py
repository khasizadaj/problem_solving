# function returns values in array in given queries after rotation.
# I simply use get_index() to find out previous index of element
# landed in given query.

# link tp problem: https://www.hackerrank.com/challenges/circular-array-rotation/problem


def circular_array_rotation(array, num_of_rotation, queries):
  values = []
  length_of_array = len(array)

  for query_position in queries:
    index = get_index(length_of_array, num_of_rotation, query_position)
    val = array[index]
    values.append(val)

  return values


def get_index(length_of_array, num_of_rotation, query_position):
  # because it is right circular rotation, in order to find previous,
  # we need to go left
  index = query_position - num_of_rotation

  # in case index is negative, Python returns positive remainder.
  # extra info: https://torstencurdt.com/tech/posts/modulo-of-negative-numbers/
  return index % length_of_array

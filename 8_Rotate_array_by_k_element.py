def rotate_array(array, k):
  """Rotates an array by k positions.

  Args:
    array: A list of elements.
    k: The number of positions to rotate the array.

  Returns:
    A list of elements rotated by k positions.
  """

  # Reverse the entire array.
  array.reverse()

  # Reverse the first k elements.
  array[:k].reverse()

  # Reverse the remaining elements.
  array[k:].reverse()

  return array


# Example usage:

array = [1, 2, 3, 4, 5]
k = 2

rotated_array = rotate_array(array, k)

print(rotated_array)
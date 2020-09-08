def tower_builder(n_floors):
  result = []
  floor = 1
  while floor <= n_floors:
    stars = 2 * floor - 1
    offset = n_floors - floor
    result.append(' ' * offset + '*' * stars + ' ' * offset)
    floor += 1
  return result
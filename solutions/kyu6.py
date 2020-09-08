def tower_builder(n_floors):
  result = []
  floor = 1
  while floor <= n_floors:
    stars = 2 * floor - 1
    offset = n_floors - floor
    result.append(' ' * offset + '*' * stars + ' ' * offset)
    floor += 1
  return result

def find_in_array(seq, predicate): 
  for i in range(len(seq)):
    elem = seq[i]
    if predicate(elem, i):
      return i
  return -1

def sort_string(s, ordering):
    def key_getter(char):
      try:
        return ordering.index(char)
      except:
        return len(ordering) + ord(char)

    return ''.join(sorted(s, key=key_getter))
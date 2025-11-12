def has_q(input_string: str) -> bool:
    """"
    Returns true if the input string has lowercase "q". Otherwise returns false."""
    return 'q' in input_string

if __name__ == "__main__":
  assert has_q("quick") == True
  assert has_q("math") == False
  print("All tests passed!")

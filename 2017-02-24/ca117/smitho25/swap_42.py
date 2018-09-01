import sys

def swap_keys_values(d):
  my_dict = d
  new_dict = {v : k for (k, v) in my_dict.items()}
  return(new_dict)
  
new_dict = swap_keys_values(d = {'a' : 4, 'b' : 7, 'c' : 10}) 

def main():
  new_dict = swap_keys_values(d = {'a' : 4, 'b' : 7, 'c' : 10}) 
  print(new_dict.items())
  
if __name__ == "__main__":
  main()
  

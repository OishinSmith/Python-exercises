class File(object):
  FILE_PERMISSIONS = "rwx"
  
  def __init__(self, name, owner, size = "0", permissions = "null"):
    self.name = name
    self.owner = owner
    self.size = size 
    self.permissions = permissions
    if permissions != "null":
      self.permissions = "".join(sorted(permissions))
   
    
  def  __str__(self):
    print("File: {}".format(self.name))
    print("Owner: {}".format(self.owner))
    print("Permissions: {}".format(self.permissions))
    return("Size: {} bytes".format(self.size))

  def has_access(self, name, permission_1):
    if self.owner == name:
      return("True")
    else: 
      return(permission_1 in self.permissions)

def main():

    # Create some files
    f1 = File('poem.txt', 'joe')
    f2 = File('readme.txt', 'max', 100, 'wr')
    f3 = File('gedit', 'fred', 200, 'wxr')

    # Check access rights
    print('Checking access rights...')
    print(f1.has_access('joe', 'r'))
    print(f1.has_access('joe', 'w'))
    print(f1.has_access('joe', 'x'))
    print(f1.has_access('max', 'r'))
    print(f2.has_access('max', 'r'))
    print(f3.has_access('max', 'r'))

if __name__ == '__main__':
    main()

class File(object):
  FILE_PERMISSIONS = "rwx"
  def __init__(self, name, owner, size = 0, permissions = "null"):
    self.name = name
    self.owner = owner
    self.size = size
    if permissions == "null":
      self.permissions = permissions
    else:
      self.permissions = "".join(sorted(permissions))

  def __str__(self):
    print("File: {}".format(self.name))
    print("Owner: {}".format(self.owner))
    print("Permissions: {}".format(self.permissions))
    return("Size: {} bytes".format(self.size))

  def has_access(self, name, perm):
    if name == self.owner:
      return "True"
    else:
      return perm in self.permissions


  def enable_permission(self, name, perm):
    if name == self.owner:
      if self.permissions == "null":
        self.permissions = ""
        self.permissions = ("".join(sorted(perm + self.permissions)))
      else:
        if perm not in self.permissions:
          self.permissions = self.permissions + perm
    else:
      return("False")
  def disable_permission(self, name, perm):
    if name == self.owner:
      if self.permissions == "null":
        pass
      else:
        if perm in self.permissions:
          self.permissions = self.permissions.replace(perm, "")
    else:
       return"False"


def main():

    # Create some files
    f1 = File('poem.txt', 'joe')
    f2 = File('readme.txt', 'max', 100, 'wr')
    f3 = File('gedit', 'fred', 200, 'wxr')

    # Joe enables permissions
    print('Joe enables permissions...')
    f1.enable_permission('joe', 'r')
    f1.enable_permission('joe', 'x')
    print(f1)
    
    # Joe enables permissions
    print('Joe enables permissions...')
    f1.enable_permission('joe', 'r')
    print(f1)

    # Joe disables permissions
    print('Joe disables permissions...')
    f1.disable_permission('joe', 'x')
    print(f1)
    
    # Joe disables permissions
    print('Joe disables permissions...')
    f1.disable_permission('joe', 'x')
    print(f1)

    # Max enables permissions
    print('Max enables permissions...')
    print(f1.enable_permission('max', 'x'))
    print(f1)

    # Max disables permissions
    print('Max disables permissions...')
    print(f1.disable_permission('max', 'r'))
    print(f1)

if __name__ == '__main__':
    main()



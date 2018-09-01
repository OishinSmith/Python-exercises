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

class Folder(object):
  def __init__(self):
    self.d = {}
    self.size = 0

  def add_file(self, other):
    self.d[other.name] = other
    self.size += other.size

  def __str__(self):
    print("Folder contents")
    print("===============")
    for k in (self.d.values()):
      print(self.d[k])
    return("Folder size: {} bytes".format(self.size))


def main():

    # Create some files
    f1 = File('poem.txt', 'joe')
    f2 = File('gedit', 'fred', 200, 'wxr')
    f3 = File('readme.txt', 'max', 100, 'wr')

    # Create an empty folder
    folder = Folder()

    # Add files to the folder
    folder.add_file(f1)
    folder.add_file(f2)
    folder.add_file(f3)

    # Display folder contents
    print(folder)

if __name__ == '__main__':
    main()


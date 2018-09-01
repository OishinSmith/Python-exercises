class File(object):
  FILE_PERMISSIONS = "rwx"
  
  def __init__(self, name, owner, size = 0, permissions = "null"):
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

class Folder(object):
    def __init__(self):
        self.location = {} #list of stuff in location
        self.size = 0 #size zero at the beginning

    def add_file(self, other):
        self.location[other.name] = other
        self.size += other.size #total

    def __str__(self):
        print("Folder contents")
        print("===============")
        for k in sorted(self.location.keys()):
            print(self.location[k])
        return("Folder size: {} bytes".format(self.size))

def main():

    # Create some files
    f1 = File('poem.txt', 'joe')
    f2 = File('readme.txt', 'max', 100, 'wr')
    f3 = File('gedit', 'fred', 200, 'wxr')

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


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

def main():

    # Display available permissions
    print('File permissions: {}'.format(File.FILE_PERMISSIONS))

    # Create some files
    f1 = File('poem.txt', 'joe')
    f2 = File('readme.txt', 'max', 100, 'wr')
    f3 = File('gedit', 'fred', 200, 'wxr')

    # Display file details
    print('File details...')
    print(f1)
    print(f2)
    print(f3)

if __name__ == '__main__':
    main()


# Append l1 to l2. If l2 not supplied default to empty list.
import sys
def append2list(l1, l2=None):
    if l2 == None:
      l2 = []
    for i in l1:
        l2.append(i)
    return l2
print

def main():    
    list1 = ['cat', 'dog']
    nlist = append2list(list1)
    # nlist should be ['cat', 'dog']
    print(nlist)

    list2 = ['lion']
    nlist = append2list(['antelope'], list2)
    # nlist should be ['lion', 'antelope']
    print(nlist)

    list3 = ['fox', 'chicken']
    nlist = append2list(list3)
    # nlist should be ['fox', 'chicken']
    print(nlist)

if __name__ == '__main__':
    main()


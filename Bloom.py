#Bloom filter to spell check Python code for Raspberry Pi(A small singleboard computer with limited storage)
#This implementation has to be further modified to contantly loop through code while spell checking it
#import pip
#pip.main(["install","mmh3"])  #should install the packages to Anaconda's local python 


import fnvhash #access to non-cryptographic hash functions Murmur and FNV
import mmh3
size = 25
bit_array = [0] * size  #list as a bit array

valid_python = ["import","in","for","range","append","eval","abs","float","input"]

def compute_hashes_and_add(valid_python, size, bit_array): #does Murmur and FNV hashing.
    for i in valid_python:
        bit_array[(fnvhash.fnv0_32(i) % size)] = 1   #these indexes are long integer literals since it's Python 2
        bit_array[(mmh3.hash(i) % size)] = 1
    print bit_array
    return bit_array

compute_hashes_and_add(valid_python, size, bit_array)

def search(elem, bit_array, size):
    if bit_array[(fnvhash.fnv0_32(elem) % size)] == 1 and bit_array[(mmh3.hash(elem) % size)] == 1:
        print "Maybe Correctly spelled!"
        return True
    else:
        print "Incorrectly spelled!"
        return False
        
search("about", bit_array, size)
search("append", bit_array, size)





#plotting graph of false positive rates
#false positive rates vs n(number of elements in bit array)
#for m = 50 and lookups equal to the number of elements inserted.
import random
import string
import matplotlib.pyplot as plt
%matplotlib inline

def randomword(length):
    return ''.join(random.choice(string.lowercase) for i in range(length))

def one_false_positive(c):
    bit_array = [0]*50
    correct_words = []
    test_words = []
    for i in range(c):
        correct_words.append(randomword(10))
        test_words.append(randomword(5)) #makes sure all test words have not been encountered
    compute_hashes_and_add(correct_words, 50, bit_array)
    false_negatives = 0
    for z in test_words:
        if search(z, bit_array, 50):
            false_negatives += 1
        else:
            pass
    return (false_negatives*100)/float(c)

def false_positives_and_plot():
    xvalues = []
    yvalues = []
    for a in range(1,201,5):
        xvalues.append(a)
        yvalues.append(one_false_positive(a))
        
    plt.plot(xvalues,yvalues,'r' )
    plt.ylabel('probability of false positive- percentage')
    plt.xlabel('n')
    plt.title('False positive rate vs n for m = 50')
    plt.show()
        
false_positives_and_plot()
    
    
    

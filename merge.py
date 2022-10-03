def merge(a, b):
    #comment added by jeevan jyoti sahoo
    """ Function to merge two arrays """
    print("program execution started")
    c = []
    while len(a) != 0 and len(b) != 0:
        #print a[0][0]
        #print b[0][0]
        if a[0][0] < b[0][0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        c += b
    else:
        c += a
    print("merging completed")
    return c

# Code for merge sort
#code for cleaning the image
def cleanImage(self, image):
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                pixel = image[i][j]
                if sum(pixel)<=55:
                    image[i][j] = [0, 0, 0]
        return image

def mergesort(x):
    """ Function to sort an array using merge sort algorithm """
    if len(x) == 0 or len(x) == 1:
        return x
    else:
        middle = len(x) // 2
        a = mergesort(x[:middle])
        b = mergesort(x[middle:])
        return merge(a, b)
    print("program executed successfully")

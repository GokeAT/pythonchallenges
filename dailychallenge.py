def task():
    input_str = input("Enter a string: ")
    words = input_str.split()
    k = []

    for i in words:
        if (input_str.count(i)>1 and (i not in k)or input_str.count(i)==1):
            k.append(i)

    words.sort()

    print("The sorted words are:")
    for word in words:
        print(word)

task()

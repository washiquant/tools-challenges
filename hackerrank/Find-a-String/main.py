def count_substring(string, sub_string):
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)
    for i in range(0, len(string)):
        print(string[i])
count_substring("ABCDCDC","CDC")
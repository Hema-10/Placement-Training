def list_to_single_integer(lst):
    single_integer = int(''.join(map(str, lst)))
    return single_integer

if __name__ == "__main__":
    lst = list(map(int, input("Enter the list of integers separated by space: ").split()))
    print(list_to_single_integer(lst))

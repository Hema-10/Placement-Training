def pair_with_rear(matrix):
    result = []
    for row in matrix:
        rear_element = row[-1]
        pairs = [(element, rear_element) for element in row]
        result.append(pairs)
    return result

def read_matrix():
    matrix = []
    rows = int(input("Enter the number of rows: "))
    for _ in range(rows):
        row = list(map(int, input("Enter the elements of the row separated by space: ").split()))
        matrix.append(row)
    return matrix

if __name__ == "__main__":
    matrix = read_matrix()
    paired_matrix = pair_with_rear(matrix)
    for row in paired_matrix:
        print(row)

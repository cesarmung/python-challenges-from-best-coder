def main():
    fileScanner()

def fileScanner():
    numbers_in_text = open(r'C:\Users\hp\Desktop\Numbers_in_text.txt', 'r')
    file_contents = numbers_in_text.read()

    file_contents = file_contents.split()

    processed_list = []
    for data in file_contents:
        if data.isdigit():
            data = int(data)
            processed_list.append(data)

    print(f'Proccesed and unsorted list: {processed_list}')

    dataProcessor(processed_list)


def dataProcessor(unsorted_list):
    sorted_list = []
    unsorted_list.sort()
    sorted_list = sorted_list + unsorted_list

    print(f'Sorted list: {sorted_list}')
    list_length = len(sorted_list)
    print(f'The length of the list is {list_length}')

    if list_length % 2 == 0:
        first_value = sorted_list[list_length//2]
        second_value = sorted_list[list_length//2 - 1]
        
        median = (first_value + second_value)/2

    else:
        median = sorted_list[list_length//2]
        
    print(f'The median of the list is {median}')

if __name__ == "__main__":
    main()


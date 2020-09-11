# Binary, Jump (O(sqrt n)), Interpolation, Exponential (O(Log n)) & Fibonacci Search requires a sorted array!
class Search:
    def __init__(self):
        self.input_array = sorted([int(value) for value in input("Please input an array of integers:\n").split()])
        self.search_value = int(input("Enter the search value:\n"))
    
    # Iterative Binary Search
    # O(Log n)

    def binary_search(self):
        start_index = 0
        end_index = len(self.input_array) - 1

        if len(self.input_array) == 0:
            return None
        
        while start_index <= end_index:
            
            mid = (start_index + end_index) // 2
            
            if self.input_array[mid] == self.search_value:
                return mid
            
            elif self.input_array[mid] < self.search_value:
                start_index = mid + 1
            
            elif self.input_array[mid] > self.search_value:
                end_index = mid - 1
        
        return "Not Found"
    
    @staticmethod
    def show_binary_search_results(search_result):
        if search_result == None:
            print("Please enter some values in input")
        
        elif search_result == "Not Found":
            print("Search value not found in the array")

        else:
            print(f"Search value found at index: {search_result}")


def main():
    search = Search()
    binary_results = search.binary_search()
    search.show_binary_search_results(binary_results)


if __name__ == '__main__':
    main()

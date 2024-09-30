import sys
print('script has started')
def my_function(value):
    print('Hello world' + value)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_value = sys.argv[1]
        my_function(input_value)
    else:
        print("Error: Missing command line argument.")

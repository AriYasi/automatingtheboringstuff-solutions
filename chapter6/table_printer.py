table_data = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def print_table(table_data):
    n = len(table_data[0])
    if all(len(x) == n for x in table_data):
        col_widths = [0] * len(table_data)

        for table_index in range(len(table_data)):
            for deep_table_index in range(len(table_data[table_index])):
                current_deep_table_item = table_data[table_index][deep_table_index]
                
                if len(current_deep_table_item) > col_widths[table_index]:
                    col_widths[table_index] = len(current_deep_table_item)
        

        column_size = len(table_data[0])

        for column in range(column_size):
            for row in range(len(table_data)):
                print(table_data[row][column].rjust(col_widths[row]), end=' ')
            print()
    else:
        print('List sizes are not the same.')

print_table(table_data)
def split_file():
    chunk_size = 1024 * 1024 * 50  # 50M
    file_number = 1
    with open("starburst-enterprise-402-e.5.rpm.zip", 'rb') as file:
        chunk = file.read(chunk_size)
        while chunk:
            with open("starburst_part_" + str(file_number), 'wb') as chunk_file:
                chunk_file.write(chunk)
            file_number += 1
            chunk = file.read(chunk_size)

def combine_file():
    merged_file = open('merge_file.rpm', 'wb')
    for i in range(23):
        merged_file.write(open('starburst_part_' + str(i + 1), 'rb').read())
    merged_file.close()
        

if __name__ == '__main__':
    # split_file()
    combine_file()
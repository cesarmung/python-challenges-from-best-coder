def main():
    open_file = open(r'C:\Users\hp\Desktop\FunWithFiles.txt', 'r')
    
    FileControl(open_file)

def FileControl(read_file):
    movie1 = read_file.readline()
    movie2 = read_file.readline()
    movie3 = read_file.readline()

    movie1 = movie1.rstrip('\n')
    movie2 = movie2.rstrip('\n')
    movie3 = movie3.rstrip('\n')

    print(movie1)
    print(movie2)
    print(movie3)
    user_fav_movie = input("What is your favorite movie? ")

    read_file.close()

    read_file = open(r'C:\Users\hp\Desktop\FunWithFiles.txt', 'a')
    read_file.write(user_fav_movie + "\n")
    read_file.close()
    

if __name__ == '__main__':
    main()
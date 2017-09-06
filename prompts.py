def user_questions():
    title = input("Enter a title for the page: \n")
    h2 = input("Enter a heading for the body of the entry: \n")
    return (title,h2)

def main():
    input = user_questions()
    print(input)

if __name__ == "__main__":
    main()



def process_file():
    try:
        f= open("./data/funny.txt")
        x= 1/0
    except FileNotFoundError as e:
        print("inside except")
    finally:
        print("cleaning up file")
        f.close()
process_file()

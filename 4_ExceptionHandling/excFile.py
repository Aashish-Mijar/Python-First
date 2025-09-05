
try:
    f = open("demoFile.txt")
    try:
        f.write("Hello")
    except:
        print("Something went wrong when writting to the file")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")
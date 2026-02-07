def main():
    width = 3
    with open('punkter.txt', 'w', encoding="utf-8") as handle:
        handle.write("1")
        for k in range(width):
            for j in range(width):
                for i in range(width):
                    if i == j == k == 0:
                        handle.write("\n" + str(i) + " " + str(j) + " " + str(k) + "\n")
                    else:
                        handle.write(str(i) + " " +     str(j) + " " + str(k) + "\n")


if __name__ == "__main__":
    main()
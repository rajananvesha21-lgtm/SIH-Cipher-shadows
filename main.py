from src.sys_info.detection import detect_system


def main():
    print("\n" + "=" * 50)
    print("              CIPHER SHADOWS")
    print("         Digital Forensics Toolkit")
    print("                  Project 1")
    print("=" * 50)

    print("\nSYSTEM INFORMATION")
    print("-" * 50)

    system_info = detect_system()

    for item in system_info:
        print(item, ":", system_info[item])


if __name__ == "__main__":
    main()
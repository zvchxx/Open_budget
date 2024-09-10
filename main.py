def main():
    print("\n1. Login\n"
          "2. Register\n"
          "3. Exit\n")

    print("""
    super admin login&password = super
    """)
    choice = input("Enter your choice: ")

    if choice == '1':
       pass
    elif choice == '2':
       pass
    elif choice == '3':
        print("Exiting...")
        return None
    else:
        print("Invalid choice. Please try again.")

    return main()


if __name__ == "__main__":
    main()
def main():
    try:
        a = int(input("Enter a number: "))
        print(a)
        return      # anything else will not be run (like break but for function)

    except Exception as e:
        print(e)
        return
    
    finally:    # Finally block is run even if return is applied.
        print("I am inside of finally block")

    print("Done!")  # will not be printed

main()
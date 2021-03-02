from Stack import Solution
import sys

def main():
    calculator = Solution()
    for expression in sys.stdin:
        try:
            if expression == 'exit\n':
                return 0
            
            result = calculator.calculate(expression)
            print(result)
        except:
            print("Wrong Expression.")

if __name__ == "__main__":
    main()

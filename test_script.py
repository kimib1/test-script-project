#!/usr/bin/env python3

def calculate_fibonacci(n):
    """
    Calculate the Fibonacci sequence up to n numbers.
    Returns a list containing the sequence.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def test_fibonacci():
    """
    Simple test function to verify fibonacci calculation
    """
    assert calculate_fibonacci(5) == [0, 1, 1, 2, 3]
    assert calculate_fibonacci(0) == []
    assert calculate_fibonacci(1) == [0]
    print("All tests passed!")

if __name__ == "__main__":
    # Example usage
    print("Testing Fibonacci calculation...")
    test_fibonacci()
    
    # Generate and display first 10 Fibonacci numbers
    result = calculate_fibonacci(10)
    print(f"\nFirst 10 Fibonacci numbers: {result}")

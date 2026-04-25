

# Timing Function Execution with a Decorator
# import time
# def timer(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()  # Record the start time
#         result = func(*args, **kwargs)  # Call the original function
#         end_time = time.time()  # Record the end time
#         print(f"Execution time: of function {func.__name__}: {end_time - start_time:.4f} seconds")  # Print the execution time
#         return result  # Return the result of the original function
#     return wrapper

# # Example usage of the timer decorator
# @timer
# def example_function(n):
#     """A sample function that simulates a time-consuming task."""
#     total = 0
#     for i in range(n):
#         total += i ** 2  # Simulate some work by calculating squares
#     return total

# # Call the example function to see the timer in action
# result = example_function(1000000)




# Debugging function calls with a Decorator
import cv2

# Open the default camera (index 0)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("Can't receive frame. Exiting...")
        break

    # Display the frame
    cv2.imshow('Webcam', frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()

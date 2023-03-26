import cv2

# Capture video from a file or a camera
cap = cv2.VideoCapture(vehicle.mp4)

# Get the frame width and height
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Define the codec and create a video writer
fourcc = cv2.VideoWriter_fourcc('XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (frame_width,frame_height))

# Set the initial position of the vehicle
vehicle_x1 = 0
vehicle_y1 = 0
vehicle_x2 = 0
vehicle_y2 = 0

# Set the initial time to zero
t = 0

while True
    ret, frame = cap.read()
    if not ret
        break
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect the vehicle in the frame
    vehicle_x1, vehicle_y1, vehicle_x2, vehicle_y2 = detect_vehicle(gray)

    # Calculate the speed of the vehicle
    speed = ((vehicle_x2 - vehicle_x1)  2 + (vehicle_y2 - vehicle_y1)  2)  0.5  (t + 1)

    # Display the frame and the speed
    cv2.rectangle(frame, (vehicle_x1, vehicle_y1), (vehicle_x2, vehicle_y2), (0, 0, 255), 2)
    cv2.putText(frame, Speed {.2f} pixelsframe.format(speed), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow(Vehicle Speed Detection, frame)
    out.write(frame)
    cv2.waitKey(1)

    # Update the time
    t += 1

# Release the video capture and writer
cap.release()
out.release()
cv2.destroyAllWindows()

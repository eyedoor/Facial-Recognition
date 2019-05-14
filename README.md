# Facial-Recognition

The facial recognition script runner is structured such that the stored faces are searched and compared against
the new face at the door, and then sent to the server to confirm whether the face is known or not. By storing
the faces of the user's friends in a .pickle file, we can easily retrieve and store the encodings of the faces,
making the system much more efficient than having to reiterate over each encoding every single time. Once the 
encoding of the new face has been compared to the encoding of every face stored in the .pickle file, the results
are sent to the server so that the user can receive an SMS notification with the name of the person at the door.

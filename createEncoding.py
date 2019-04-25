import os
import sys
import pickle
import face_recognition

friendImage = face_recognition.load_image_file(sys.argv[1])
userPath = sys.argv[2]
friendId = sys.argv[3]

try: 
    encodings = pickle.load(open(userPath + "/encodings.pickle", "rb"))
except (OSError, IOError) as error:
    encodings = {}

friendEncoding = face_recognition.face_encodings(friendImage)
encodings[friendId] = friendEncoding

outfile = open(userPath + "/encodings.pickle", "wb")
pickle.dump(encodings, outfile)
outfile.close()

# Take image on command line (argv 2)
# Encode image with face_recognition
# Save encoding object to variable
# If no file then create new dictionary with encoding
# else open pickle file, add encoding to dictionary
# repickle dictionary
# done

# open pickle dictionary
# use encodings to match image
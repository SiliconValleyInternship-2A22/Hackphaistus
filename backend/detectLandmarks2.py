import dlib
 
img = dlib.load_rgb_image("jk.png")
win = dlib.image_window(img, "Image")
 
detector = dlib.get_frontal_face_detector()
faces = detector(img)
win.add_overlay(faces)
 
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
 
for face in faces:
    landmarks = predictor(img, face)
 
    parts = landmarks.parts()
 
    # jaw, ear to ear
    for part in parts[0:17]:
        win.add_overlay_circle(part, 1.3, dlib.rgb_pixel(255,0,0))
        print("face=",part)
 
    # left eyebrow
    for part in parts[17:22]:
        win.add_overlay_circle(part, 1.3, dlib.rgb_pixel(0, 255, 0))
 
    # right eyebrow
    for part in parts[22:27]:
        win.add_overlay_circle(part, 1.3, dlib.rgb_pixel(0, 0, 255))
 
    # line on top of nose
    for part in parts[27:31]:
        win.add_overlay_circle(part, 1.3, dlib.rgb_pixel(0, 0, 0))
 
    # bottom part of the nose
    for part in parts[31:36]:
        win.add_overlay_circle(part, 1.3, dlib.rgb_pixel(255, 0, 255))
 
    # left eye
    for part in parts[36:42]:
        win.add_overlay_circle(part, 1.3, dlib.rgb_pixel(255, 255, 0))
 
    # right eye
    for part in parts[42:48]:
        win.add_overlay_circle(part, 1.3, dlib.rgb_pixel(0, 255, 255))
 
    # outer part of the lips
    for part in parts[48:60]:
        win.add_overlay_circle(part, 1.3, dlib.rgb_pixel(100, 100, 100))
 
    # inner part of the lips
    for part in parts[60:68]:
        print(part)
        win.add_overlay_circle(part, 1.3, dlib.rgb_pixel(255, 255, 255))
 
win.wait_until_closed()
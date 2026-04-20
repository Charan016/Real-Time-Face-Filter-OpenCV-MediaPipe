# Libraries
import cv2
import mediapipe as mp
import numpy as np

# Loading the Four channel image RGBA
mustache_png = cv2.imread("mustache.png", cv2.IMREAD_UNCHANGED)
hat_png = cv2.imread("hat.png", cv2.IMREAD_UNCHANGED)

# checking if the image is uploded or not and it is 4 channel
for name, img in (("mustache.png", mustache_png), ("hat.png", hat_png)):
    if img is None or img.shape[2] < 4:
        raise FileNotFoundError(f"Missing file {name}")


mp_face = mp.solutions.face_mesh

face_mesh = mp_face.FaceMesh(
    static_image_mode = False,    # detect face in video streaming
    max_num_faces = 1,   # Track the first detected face in the video
    refine_landmarks = False,  # no need of high resolution mesh
    min_detection_confidence = 0.5, # consider it as a face if p > 0.5
    min_tracking_confidence = 0.5  # p > 0.5, continue tracking the face
)

# Capture the video from webcam
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

if not cap.isOpened():
    raise RuntimeError("Cannot capture your video")

def overlay_rgba(background, overlay, x, y, w, h):
    overlay = cv2.resize(overlay, (w, h), interpolation=cv2.INTER_AREA)

    b, g, r, a = cv2.split(overlay)

    alpha = a.astype(float) / 255.0
    alpha = cv2.merge([alpha, alpha, alpha])

    h_bg, w_bg = background.shape[:2]

    x0, y0 = max(0, x), max(0, y)
    x1, y1 = min(x + w, w_bg), min(y + h, h_bg)

    if x0 >= x1 or y0 >= y1:
        return background

    overlay_slice = (slice(y0 - y, y1 - y), slice(x0 - x, x1 - x))
    background_roi = (slice(y0, y1), slice(x0, x1))

    foreground = cv2.merge([b, g, r])[overlay_slice]
    alpha_roi = alpha[overlay_slice]
    bg_roi = background[background_roi]

    if foreground.size == 0 or bg_roi.size == 0:
        return background

    blended = cv2.convertScaleAbs(
        foreground * alpha_roi + bg_roi * (1 - alpha_roi)
    )

    background[background_roi] = blended
    return background



while True:
    ok, frame = cap.read()

    if not ok:
        print("Frame is Empty")
        break

    # converting horizontal to selfie format
    frame = cv2.flip(frame,1)
    h_frame, w_frame = frame.shape[:2]   # taking height and width of frame

    # convert BGR (capture by CV2) to RGB (Mediapipe)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)


    # Using face grid to get the landmarks
    result = face_mesh.process(rgb)

    # finding the required landmarks on the face grid

    if result.multi_face_landmarks:
        landmarks = result.multi_face_landmarks[0].landmark

        # utility function
        def to_px(idx):
            pt = landmarks[idx]
            return int(pt.x * w_frame), int(pt.y * h_frame)
        
        lip_x1, lip_y1 = to_px(13)
        lip_x2, lip_y2 = to_px(14)

        # average to get the center lip postion
        lip_x = (lip_x1 + lip_x2) // 2
        lip_y = (lip_y1 + lip_y2) // 2

        # Hat postion
        left_temple_x,_ = to_px(127)
        right_temple_x,_ = to_px(356)
        forehead_x, forehead_y = to_px(10) 

        face_w = right_temple_x - left_temple_x

        # Add mustache on face
        mush_w = face_w
        mush_h = int(mush_w * 0.30)

        mush_x = lip_x - mush_w // 2
        mush_y = lip_y - int(mush_h * 0.75)

        frame = overlay_rgba(frame, mustache_png, mush_x, mush_y, mush_w, mush_h)

        # Add Hat on Face
        hat_w = int(face_w * 1.6)
        hat_h = int(hat_w * 0.9) # 0.9
        hat_x = forehead_x - hat_w //2
        hat_y = forehead_y - int(hat_h * 0.9)
        frame = overlay_rgba(frame, hat_png, hat_x, hat_y, hat_w, hat_h)

    cv2.imshow("Press ESC to quit | Press s to Save", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == 27:
        break
    elif key == ord('s'):
        cv2.imwrite("My_Funny_Image.png", frame)
        print("Frame successfully Saved")


cv2.release()
cv2.destroyAllWindows()




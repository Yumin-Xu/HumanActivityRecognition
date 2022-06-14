import cv2
import numpy as np

img = np.zeros((900, 1000, 3), np.uint8)
pts = np.array([[320, 506 - 200], [335, 653 - 200], [468, 581 - 200]])
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.polylines(img, [pts], True, (0, 255, 255), 2)
cv2.putText(img, 'label A',
            (335, 581 - 200), font, 0.5, (255, 255, 0), 2)

pts = np.array([[415, 474 - 200], [429, 607 - 200], [548, 542 - 200]])
cv2.polylines(img, [pts], True, (10, 255, 255), 2)
cv2.putText(img, 'label B',
            (429, 542 - 200), font, 0.5, (255, 255, 0), 2)

pts = np.array([[354, 525 - 200], [370, 666 - 200], [494, 604 - 200]])
cv2.polylines(img, [pts], True, (20, 255, 255), 2)
cv2.putText(img, 'label C',
            (370, 604 - 200), font, 0.5, (255, 255, 0), 2)

pts = np.array([[549, 727 - 200], [560, 845 - 200], [657, 796 - 200]])
cv2.polylines(img, [pts], True, (30, 255, 255), 2)
cv2.putText(img, 'label D',
            (560, 796 - 200), font, 0.5, (255, 255, 0), 2)

pts = np.array([[510, 681 - 200], [526, 813 - 200], [644, 770 - 200]])
cv2.polylines(img, [pts], True, (40, 255, 255), 2)
cv2.putText(img, 'label E',
            (526, 770 - 200), font, 0.5, (255, 255, 0), 2)

pts = np.array([[517, 729 - 200], [528, 841 - 200], [619, 793 - 200]])
cv2.polylines(img, [pts], True, (50, 255, 255), 2)
cv2.putText(img, 'label F',
            (528, 793 - 200), font, 0.5, (255, 255, 0), 2)

pts = np.array([[463, 681 - 200], [476, 807 - 200], [599, 761 - 200]])
cv2.polylines(img, [pts], True, (60, 255, 255), 2)
cv2.putText(img, 'label G',
            (476, 761 - 200), font, 0.5, (255, 255, 0), 2)

pts = np.array([[504, 719 - 200], [512, 826 - 200], [616, 786 - 200]])
cv2.polylines(img, [pts], True, (70, 255, 255), 2)
cv2.putText(img, 'label H',
            (512, 786 - 200), font, 0.5, (255, 255, 0), 2)

pts = np.array([[509, 720 - 200], [522, 841 - 200], [621, 794 - 200]])
cv2.polylines(img, [pts], True, (80, 255, 255), 2)
cv2.putText(img, 'label I',
            (512, 786 - 200), font, 0.5, (255, 255, 0), 2)

pts = np.array([[517, 718 - 200], [530, 831 - 200], [632, 792 - 200]])
cv2.polylines(img, [pts], True, (90, 255, 255), 2)
cv2.putText(img, 'label J',
            (530, 792 - 200), font, 0.5, (255, 255, 0), 2)

pts = np.array([[529, 709 - 200], [546, 833 - 200], [656, 793 - 200]])
cv2.polylines(img, [pts], True, (100, 255, 255), 2)
cv2.putText(img, 'label K',
            (546, 793 - 200), font, 0.5, (255, 255, 0), 2)

pts = np.array([[551, 723 - 200], [562, 827 - 200], [664, 796 - 200]])
cv2.polylines(img, [pts], True, (110, 255, 255), 2)
cv2.putText(img, 'label L',
            (562, 796 - 200), font, 0.5, (255, 255, 0), 2)

pts = np.array([[448, 532 - 200], [472, 693 - 200], [611, 616 - 200]])
cv2.polylines(img, [pts], True, (120, 255, 255), 2)
cv2.putText(img, 'label M',
            (472, 616 - 200), font, 0.5, (255, 255, 0), 2)

pts = np.array([[493, 581 - 200], [522, 724 - 200], [651, 666 - 200]])
cv2.polylines(img, [pts], True, (130, 255, 255), 2)
cv2.putText(img, 'label O',
            (522, 666 - 200), font, 0.5, (255, 255, 0), 2)

pts = np.array([[524, 573 - 200], [539, 714 - 200], [672, 649 - 200]])
cv2.polylines(img, [pts], True, (140, 255, 255), 2)
cv2.putText(img, 'label P',
            (539, 649 - 200), font, 0.5, (255, 255, 0), 2)

pts = np.array([[543, 724 - 200], [548, 837 - 200], [648, 793 - 200]])
cv2.polylines(img, [pts], True, (150, 255, 255), 2)
cv2.putText(img, 'label Q',
            (548, 793 - 200), font, 0.5, (255, 255, 0), 2)

pts = np.array([[503, 657 - 200], [518, 791 - 200], [639, 733 - 200]])
cv2.polylines(img, [pts], True, (160, 255, 255), 2)
cv2.putText(img, 'label R',
            (518, 733 - 200), font, 0.5, (255, 255, 0), 2)

pts = np.array([[488, 630 - 200], [506, 762 - 200], [626, 703 - 200]])
cv2.polylines(img, [pts], True, (170, 255, 255), 2)
cv2.putText(img, 'label S',
            (506, 703 - 200), font, 0.5, (255, 255, 0), 2)

cv2.imshow("line", img)
cv2.waitKey(0)
cv2.destroyAllWindows()



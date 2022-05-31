import cv2

def image_resize(image, width = None, Height = None, inter = cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]
    if width is None and Height is None:
        return image
    if width is None:
        r = Height / float(h)
        dim = (int(w * r), Height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))
    resized = cv2.resize(image, dim, interpolation = inter)
    return resized
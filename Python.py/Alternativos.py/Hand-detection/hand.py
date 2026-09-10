import cv2
import mediapipe as mp


class HandDetector:
  """Class to detect hands."""
  def __init__(self, mode=False, max_hands=2, confidence_detection=0.5,
                tracking_confidence=0.5, point_colors=(0,0,255), connections_colors=(255,255,255)):
    """_summary_
    Function used to initialize the class
    Args:
        mode (bool, optional): Image capture mode. If True, tracking detection will be made at all the time; this makes too stuck. If False, not will be made tracking detection all the time; can lose marks to some instants but not stuck.
        
        max_hands (int, optional): Max quantity of hands to be detected.
        
        confidence detection (float, optional): Percentual rate of hand detection. If it is smaller than this limit, the detection do not happens.
        
        rastreio_confianca (float, optional): Percentual rate of hand points tracking. If it is smaller than this limit, tracking do not happens.
        
        point_colors (tuple, optional): Point colors.
        
        connections_colors (tuple, optional): Connection colors.
    """
    self.mode=mode
    self.max_hands=max_hands
    self.confidence_detection=confidence_detection
    self.tracking_confidence=tracking_confidence
    self.point_colors=point_colors
    self.connections_colors=connections_colors
    
    self.hands_mp=mp.solutions.hands
    self.hands=self.hands_mp.Hands(
      self.mode,
      self.max_hands,
      1,
      self.confidence_detection,
      self.tracking_confidence
    )
    
    self.draw_mp=mp.solutions.drawing_utils
    self.draw_settin_points=self.draw_mp.DrawingSpec(color=self.point_colors)
    self.draw_settin_connections=self.draw_mp.DrawingSpec(color=self.connections_colors)
  
  def find_hands(self,image,draw=True):
    """_summary_
    Function to detect the hands
    Args:
        image (_type_): captured image.
        draw (bool, optional): draw points and connections in hands. Defaults to True.
        return: Return images with detection.
    """
    image_rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    self.result=self.hands.process(image_rgb)
    if self.result.multi_hand_landmarks:
      for point in self.result.multi_hand_landmarks:
          print(point)

def main():
  cap=cv2.VideoCapture(0)
  detector=HandDetector()
  while True:
    _,image=cap.read()
    image=cv2.flip(image,1)
    detector.find_hands(image)
    cv2.imshow('Captura',image)
    cv2.waitKey(1)

if __name__=='__main__':
  main()
  
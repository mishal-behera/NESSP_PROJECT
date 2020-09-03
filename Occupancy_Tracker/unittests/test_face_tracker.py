import unittest
# from face_tracker import FaceTracker
from Occupancy_Tracker.human_detector import HumanDetector
from Occupancy_Tracker.send_receive_messages import SendReceiveMessages
from Occupancy_Tracker.logger import Logger
import logging
import os
from Occupancy_Tracker.constants import TEST_VIDEO_FILE_PATH_1, TEST_VIDEO_FILE_PATH_2, Direction
import cv2


class TestFaceTracker(unittest.TestCase):
    """
    This class will test the face tracker class.

    :key
    """
    def __cleanup(self):
        for file in os.listdir(os.getcwd()):
            if file.endswith('.jpg'):
                os.remove(file)

    def test_one_person_entering(self):
        """
        This method validates if occupancy detector can actually detect one person entering the premises.
        :return:
        """
        human_detector_inst = HumanDetector(
            find_humans_from_video_file_name='videos/one_person_entering.mp4',
            use_pi_camera=False, open_display=False)
        self.assertEqual(human_detector_inst.perform_job(), None)
        human_centroid_dict = human_detector_inst.get_human_centroid_dict()
        self.assertEqual(len(human_centroid_dict), 1)
        self.assertEqual(human_centroid_dict[0].direction, Direction.ENTER)
        self.assertEqual(human_detector_inst.send_receive_message_instance.get_face_detected_count_locally(), 1)
        human_detector_inst.clean_up()
        self.__cleanup()

    def test_two_persons_exiting(self):
        """
        This method validates if occupancy detector can actually detect two persons exiting the premises.
        :return:
        """
        human_detector_inst = HumanDetector(
            find_humans_from_video_file_name='videos/two_persons_exiting.mp4',
            use_pi_camera=False, open_display=False)
        self.assertEqual(human_detector_inst.perform_job(), None)
        human_centroid_dict = human_detector_inst.get_human_centroid_dict()
        self.assertEqual(len(human_centroid_dict), 2)
        self.assertEqual(human_centroid_dict[0].direction, Direction.EXIT)
        self.assertEqual(human_centroid_dict[1].direction, Direction.EXIT)
        self.assertEqual(human_detector_inst.send_receive_message_instance.get_face_detected_count_locally(), -2)
        human_detector_inst.clean_up()
        self.__cleanup()

    def test_three_persons_entering(self):
        """
        This method validates if occupancy detector can actually detect three persons entering the premises.
        :return:
        """
        human_detector_inst = HumanDetector(
            find_humans_from_video_file_name='videos/3_persons_entering.mp4',
            use_pi_camera=False, open_display=False)
        self.assertEqual(human_detector_inst.perform_job(), None)
        human_centroid_dict = human_detector_inst.get_human_centroid_dict()
        self.assertEqual(len(human_centroid_dict), 3)
        self.assertEqual(human_centroid_dict[0].direction, Direction.ENTER)
        self.assertEqual(human_centroid_dict[1].direction, Direction.ENTER)
        self.assertEqual(human_centroid_dict[1].direction, Direction.ENTER)
        self.assertEqual(human_detector_inst.send_receive_message_instance.get_face_detected_count_locally(), 3)
        human_detector_inst.clean_up()
        self.__cleanup()

    def test_horizontal_line_4_entering(self):
        """
        This method validates if occupancy detector can actually detect three persons entering the premises.
        :return:
        """
        human_detector_inst = HumanDetector(
            find_humans_from_video_file_name='videos/TempleVideos/horizontal_line_4_Exiting.mp4',
            use_pi_camera=False, open_display=False)
        self.assertEqual(human_detector_inst.perform_job(), None)
        human_centroid_dict = human_detector_inst.get_human_centroid_dict()
        self.assertEqual(len(human_centroid_dict), 4)
        self.assertEqual(human_centroid_dict[0].direction, Direction.EXIT)
        self.assertEqual(human_centroid_dict[1].direction, Direction.EXIT)
        self.assertEqual(human_centroid_dict[2].direction, Direction.EXIT)
        self.assertEqual(human_centroid_dict[3].direction, Direction.EXIT)
        self.assertEqual(human_detector_inst.send_receive_message_instance.get_face_detected_count_locally(), -4)
        human_detector_inst.clean_up()
        self.__cleanup()


if __name__ == '__main__':
    unittest.main()

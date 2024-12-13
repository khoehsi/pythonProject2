from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap
from project2 import *
import os


class Logic(QMainWindow, Ui_MainWindow):
    MIN_VOLUME = 0
    MAX_VOLUME = 3
    MIN_CHANNEL = 0
    MAX_CHANNEL = 2

    def __init__(self)-> None:
        """Initialize the remote control with default settings."""

        super().__init__()
        self.setupUi(self)

        self.__status = False
        self.__muted = False
        self.__set_mute_0 = False
        self.__volume = Logic.MIN_VOLUME
        self.__channel = Logic.MIN_CHANNEL
        self.__slider_value = 0
        self.__previous_volume = Logic.MIN_VOLUME

        self.mute.clicked.connect(self.mute_button)
        self.channelup.clicked.connect(self.channel_up)
        self.power_button.clicked.connect(self.toggle_power_state)
        self.channeldown.clicked.connect(self.channel_down)
        self.pushButton_27.clicked.connect(self.channel_one)
        self.pushButton_26.clicked.connect(self.channel_second)
        self.pushButton_25.clicked.connect(self.channel_third)
        self.horizontalSlider.valueChanged.connect(self.adjust_volume)



    def toggle_power_state(self) -> None:
        """Toggle the power state of the TV (on/off)."""
        print("power on")
        self.__status = not self.__status
        self.__channel = Logic.MIN_CHANNEL
        self.show_image()

    def mute_button(self) -> None:
        """Toggle the mute state of the TV."""
        if self.__status:
            if self.__muted == True:
                self.__muted = False
                self.mute.setText("Mute")
                print("Unmuted the tv")
                self.__volume = self.__previous_volume
                self.horizontalSlider.setValue(self.__volume)
            elif self.__muted == False:
                self.__muted = True
                self.mute.setText("Unmute")
                print("Muted the tv")
                self.__set_mute_0 = True
                self.horizontalSlider.setValue(0)

        print(f"###mute_button, current self.__muted {self.__muted}\nprev vol: {self.__previous_volume}\nvol: {self.__volume}\n\n")
        # print(f"self.__perivouse_volume:{self.__previous_volume}")
        # print(f"///self.__slider_value:{self.__slider_value}")
        # print(f"///self.__volume:{self.__volume}")


    def adjust_volume(self,value) -> None:
        """It is for adjustment of the volume ."""
        self.__slider_value = value
        if self.__status:
            if self.__set_mute_0 == True:
                self.__set_mute_0 = False
                self.__volume = value
            elif self.__muted == True:
                print("TV was muted, unmuting TV\n")
                self.__muted = False
                self.mute.setText("Mute")
                self.__volume = value
                self.__previous_volume = self.__volume
            elif self.__muted == False:
                print("TV was unmuted, no change\n")
                self.__volume = value
                self.__previous_volume = self.__volume
        # print(f"###adjust_volume (mute = TRUE)\nprev vol: {self.__previous_volume}\nvol: {self.__volume}\n\n")



    def channel_up(self) -> None:
        """Increase the channel by one, or reset to the first channel."""
        if self.__status:
            if self.__channel < Logic.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Logic.MIN_CHANNEL
            self.show_image()


    def channel_down(self) -> None:
        """Decrease the channel by one, or reset to the last channel."""
        if self.__status:
            if self.__channel > Logic.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Logic.MAX_CHANNEL
            self.show_image()



    def channel_one(self) -> None:
        """Select channel 1 and update the display."""
        if self.__status:
            self.__channel = Logic.MIN_CHANNEL
            self.show_image()


    def channel_second(self) -> None:
        """Select channel 2 and update the display."""
        if self.__status:
            self.__channel = 1
            self.show_image()


    def channel_third(self) -> None:
        """Select channel 2 and update the display."""
        if self.__status:
            self.__channel = Logic.MAX_CHANNEL
            self.show_image()


    def show_image(self) -> None:

        """ Update the display channel image. """


        if self.__status:
            print("show image")
            cwd = os.getcwd()
            if self.__channel == 0:
                file_path = os.path.join(cwd, "IMAGES", "FOX.png")
                Pixmap = QPixmap(file_path)
                self.screen.setPixmap(Pixmap)

            elif self.__channel == 1:
                file_path = os.path.join(cwd, "IMAGES", "BBC.png")
                Pixmap = QPixmap(file_path)
                self.screen.setPixmap(Pixmap)

            elif self.__channel == 2:
                file_path = os.path.join(cwd, "IMAGES", "CNN.png")
                Pixmap = QPixmap(file_path)
                self.screen.setPixmap(Pixmap)

            self.screen.setScaledContents(True)
        else:
            self.screen.setPixmap(QPixmap())



    def __str__(self) -> None:
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Logic.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'

        """Return a string representation of the current TV state."""
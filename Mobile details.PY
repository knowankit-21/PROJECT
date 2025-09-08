class Mobile:
    ls='YES'
    jk='YES'

    def __init__(self):
        self.model='Realme X'

        self.price=18000

        self.date="Announced-2019,May.Released 2019,July"

        self.battery="""Type-3765mAh
        Charging-20W wired,55% in 30 min """

        self.display="""Type-AMOLED
        Size-6.53 inches
        Resolution-1080*2340 pixels
        Protection-Corning Gorilla glass 5"""

        self.body="""Dimensions-161.2*9.4 mm
      weight-191g
      sim-Nano-sim + Nano-sim        """

        self.comms="""WLAN- Wi-Fi 802.11 a/b/g/n/ac, dual-band, Wi-Fi Direct
       Bluetooth-5.0,A2DP,LE,aptX HD
       Positioning-GPS,GLONASS,BDS
       NFC-No
       Radio-FM radio
       USB-USB Type-C        """

        self.memory="""Card slot- NO
        Internal- 128GB 6GB RAM
        UFS 2.1"""

        self.camera="""Dual- 48 MP(wide) and 5 MP(depth)
            Features-LED flash,HDR
            Video-4k@30fps,1080p@30fps"""

        self.selfie="""Single-Motorized pop-up 16 MP
               Features-HDR
               Video-1080@30fps"""

        self.platform="""OS-Android 9.0(pie)
          Chipset-Qualcomm SDM710 Snapdragon 710(10nm)
          CPU-Octa-core
          GPU-Adreno 616"""

    def show_model(self):
        print("MODEL:",self.model)
        print()

    def show_price(self):
        print("PRICE:",self.price)
        print()

    def show_releasedate(self):
        print("LAUNCH:",self.date)
        print()

    def show_battery(self):
        print("BATTERY:",self.battery)
        print()

    def show_display(self):
        print("DISPLAY:",self.display)
        print()

    def show_body(self):
        print("BODY:",self.body)
        print()

    def show_comms(self):
        print("COMMS:",self.comms)
        print()

    def show_memory(self):
        print("MEMORY:",self.memory)
        print()

    def show_maincamera(self):
        print("MAIN CAMERA:",self.camera)
        print()

    def show_selfiecamera(self):
        print("SELFIE CAMERA:",self.selfie)
        print()

    def show_platform(self):
        print("PLATFORM:",self.platform)
        print()


    @classmethod   #Function decorators
    def is_ls(cls):
        print("Loudspeaker: ",cls.ls)

    @classmethod   #Function decorators
    def is_jk(cls):
        print("3.5mm jack: ",cls.jk)


realme=Mobile()
realme.show_model()
realme.show_price()
realme.show_releasedate()
realme.show_battery()
realme.show_display()
realme.show_body()
realme.show_comms()
realme.show_memory()
realme.show_maincamera()
realme.show_selfiecamera()
realme.show_platform()
Mobile.is_ls()
Mobile.is_jk()


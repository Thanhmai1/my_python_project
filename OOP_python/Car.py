class Car:
    def __init__(self, nameCar, nam_san_xuat, hang_xe, so_ghe):
        self._nameCar = nameCar
        self._nam_san_xuat = nam_san_xuat
        self._hang_xe = hang_xe
        self._so_ghe = so_ghe
        
        
    def tang_toc(self):
        print(self._nameCar + " khoi dong")
        
    def start(self):
        print(self._nameCar + " bat dau")
    def stop(self):
        print(self._nameCar + " dung lai")
        
mycar = Car("Mec", 2020, "Mec", 5)    

mycar.tang_toc()
mycar.start()
mycar.stop()
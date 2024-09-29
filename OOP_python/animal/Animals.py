class Animal:
    def __init__(self, name, sound):
        self._name = name   
        self._sound = sound        
    
    def speak(self):
        return f"{self._name} say {self._sound}"

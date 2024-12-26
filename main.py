# from dataclasses import dataclass

# @dataclass
# class Product:
#     nomi: str
#     _puli: float
#     availability: bool
#
#     @property
#     def price(self):
#         return self._puli
#
#     @price.setter
#     def price(self, value):
#         if value > 0:
#             self._puli = value
#         else:
#             raise ValueError("Narx ijobiy bo'lishi kerak")
#
# class ElectronicProduct(Product):
#     def __init__(self, name: str, pul: float, mavjud: bool, kafolat_muddati: int):
#         super().__init__(name, pul, mavjud)
#         self.kafolat_muddati = kafolat_muddati
#
# product = ElectronicProduct("asua", 515, True, 3)
# print(f"Mahsulot: {product.nomi}, Narx: {product.price}, Mavjud: {product.availability}, Kafolat: {product.kafolat_muddati} oy")



# 2-misol
# from dataclasses import dataclass
# @dataclass
# class Vehicle:
#     brand: str
#     _tezlik: float
#     @property
#     def speed(self):
#         return self._tezlik
#     def moshina(self, increment: float):
#         if self._tezlik + increment <= 300:
#             self._tezlik += increment
#         else:
#             raise ValueError("Tezlik 300 dan oshmasligi kerak")
# class moshinalar(Vehicle):
#     def __init__(self, brand: str, tezlik: float, yoqilgi_turi: str):
#         super().__init__(brand, tezlik)
#         self.yoqilgi_turi = yoqilgi_turi
#
# class velespst(Vehicle):
#     def __init__(self, brand: str, tezlik: float, yoqilgi_turi: str):
#         super().__init__(brand, tezlik)
#         self.yoqilgi_turi = yoqilgi_turi
# car = moshinalar("Toyota", 150, "Petrol")
# bicycle = velespst("germaniski", 25, "ozin tepasan")
# car.moshina(100)
# print(f"Avtomobil: {car.brand}, Tezlik: {car.speed}, Yoqilg'i turi: {car.yoqilgi_turi}")
# bicycle.moshina(20)
# print(f"Velosiped: {bicycle.brand}, Tezlik: {bicycle.speed}, Tormoz turi: {bicycle.yoqilgi_turi}")

# 3-misol
# from dataclasses import dataclass
#
# @dataclass
# class Book:
#     turi: str
#     mualif: str
#     _narxi: float
#
#     @property
#     def price(self):
#         return self._narxi
#
#     def update_price(self, yangi_narh: float, a: bool):
#         if a:
#             self._narxi = yangi_narh
#         else:
#             raise PermissionError("Faqat kitob egasi narxni o'zgartirishi mumkin")
#
# class EBook(Book):
#     def __init__(self, turi: str, mualif: str, narhi: float, fayl_sizi: float):
#         super().__init__(turi, mualif, narhi)
#         self.fayl_sizi = fayl_sizi
#
# class PrintedBook(Book):
#     def __init__(self, turi: str, mualif: str, narhi: float, qogoz_turi: str):
#         super().__init__(turi, mualif, narhi)
#         self.qogoz_turi = qogoz_turi
#
# # Misol
# kitob = EBook("Python Dasturlash", "O'qituvchi", 29.99, 10)
# bosilgan_kitob = PrintedBook("Dasturlash 101", "Muallif", 39.99, "A4")
#
# print(f"Kitob: {kitob.turi}, Muallif: {kitob.mualif}, Narx: {kitob._narxi}, Fayl hajmi: {kitob.fayl_sizi}MB")
# print(f"Qog'oz Kitob: {bosilgan_kitob.turi}, Muallif: {bosilgan_kitob.mualif}, Narx: {bosilgan_kitob.price}, Qog'oz turi: {bosilgan_kitob.qogoz_turi}")

# 4-misol
# from dataclasses import dataclass
# @dataclass
# class Employee:
#     ism: str
#     lovozm: str
#     _ishhaqi: float
#     @property
#     def salary(self):
#         return self._ishhaqi
#     def increase_salary(self, oshirish: float, a: bool):
#         if a:
#             self._ishhaqi += oshirish
#         else:
#             raise PermissionError("Faqat direktor maoshni ko'paytirishi mumkin")
# class ishcji(Employee):
#     def manage_team(self):
#         return "odiy ishchi"
# class Dasturchi(Employee):
#     def write_code(self):
#         return "Kod yozadi"
# a = ishcji("Ali", "qora ishchi", 10000)
# dasturchi = Dasturchi("husanboy", "Dasturchi", 40000)
# print(f"ishcji: {a.ism}, qora ishchi: {a.lovozm}, Maosh: {a.salary}")
# print(f"Dasturchi: {dasturchi.ism}, Lavozim: {dasturchi.lovozm}, Maosh: {dasturchi.salary}")


# 5-misol
# from dataclasses import dataclass
#
# @dataclass
# class Athlete:
#     ism: str
#     port_yuri: str
#     _rekodi: list
#
#     @property
#
#     def records(self):
#         return self._rekodi
#
#     def update_records(self, yangi_rekodi: float):
#         self._rekodi = [yangi_rekodi]
#
# class Runner(Athlete):
#     def __init__(self, name: str, sport_turi: str, rekot: list, masofa: float):
#         super().__init__(name, sport_turi, rekot)
#         self.masofa = masofa
#
# class Swimmer(Athlete):
#     def __init__(self, name: str, sport_turi: str, rekot: list, suzishmasova: float):
#         super().__init__(name, sport_turi, rekot)
#         self.suzishmasova = suzishmasova
# yugirish = Runner("qodir", "Yugurish", [10.5, 11.2], 100)
# suzish = Swimmer("husanboy", "Suzish", [1.0, 32.5], 50)
#
# yugirish.update_records(9.8)
# print(f"Yuguruvchi: {yugirish.ism}, Sport turi: {yugirish.masofa}, Yangi rekord: {yugirish.records[0]} s, Masofa: {yugirish.masofa}m")
#
# suzish.update_records(29.5)
# print(f"Suzuvchi: {suzish.ism}, Sport turi: {suzish.suzishmasova}, Yangi rekord: {suzish.records[0]} s, Havza hajmi: {suzish.suzishmasova}m")

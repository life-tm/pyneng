# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

network_mask = input ("Введите IP-сеть в формате: 10.1.1.0/24\n")
network_mask = network_mask.split('/')
network = network_mask[0].split('.')
network_1 = int(network[0])
network_2 = int(network[1])
network_3 = int(network[2])
network_4 = int(network[3])
mask_prefix = network_mask[1]
mask_int = '1'*int(mask_prefix)
mask_1 = int(mask_int[0:8],2)
mask_2 = int(mask_int[8:16],2)
mask_3 = int(mask_int[16:23],2)
mask_4 = int(mask_int[23:31],2)
print('''
Network:
{network[0]:8}  {network[1]:8}  {network[2]:8}  {network[3]:8}
{network_1:08b}  {network_2:08b}  {network_3:08b}  {network_4:08b}

Mask:
/{mask_prefix}
{mask_1:<8}  {mask_2:<8} {mask_3:<8}
{mask_1:<08b}  {mask_2:<08b} {mask_3:<08b}
'''.format(network=network,network_1=network_1,network_2=network_2,network_3=network_3,network_4=network_4,mask_prefix=mask_prefix,mask_1=mask_1,mask_2=mask_2,mask_3=mask_3))
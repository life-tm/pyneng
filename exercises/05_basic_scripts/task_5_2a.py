# -*- coding: utf-8 -*-
"""
Задание 5.2a

Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети,
надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску,
как в задании 5.2.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.195/28 - хост из сети 10.0.5.192/28

Если пользователь ввел адрес 10.0.1.1/24, вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000


Проверить работу скрипта на разных комбинациях хост/маска, например:
    10.0.5.195/28, 10.0.1.1/24

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)


Подсказка:
Есть адрес хоста в двоичном формате и маска сети 28. Адрес сети это первые 28 бит
адреса хоста + 4 ноля.
То есть, например, адрес хоста 10.1.1.195/28 в двоичном формате будет
bin_ip = "00001010000000010000000111000011"

А адрес сети будет первых 28 символов из bin_ip + 0000 (4 потому что всего
в адресе может быть 32 бита, а 32 - 28 = 4)
00001010000000010000000111000000

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

network_mask = input ("Введите IP-хоста или сеть в формате: 10.0.1.1/24\n")
network_mask = network_mask.split('/')
network = network_mask[0].split('.')
network_1 = int(network[0])
network_2 = int(network[1])
network_3 = int(network[2])
network_4 = int(network[3])
network_count_1 = bin(network_1)[2:].count('0')+bin(network_1)[2:].count('1')
network_count_2 = bin(network_2)[2:].count('0')+bin(network_2)[2:].count('1')
network_count_3 = bin(network_3)[2:].count('0')+bin(network_3)[2:].count('1')
network_count_4 = bin(network_4)[2:].count('0')+bin(network_4)[2:].count('1')
network_bin_1 = '0'*(8-network_count_1) + bin(network_1)[2:]
network_bin_2 = '0'*(8-network_count_2) + bin(network_2)[2:]
network_bin_3 = '0'*(8-network_count_3) + bin(network_3)[2:]
network_bin_4 = '0'*(8-network_count_4) + bin(network_4)[2:]
network_bin_common = network_bin_1 + network_bin_2 + network_bin_3 + network_bin_4
mask_prefix = network_mask[1]
bin_network = network_bin_common[0:int(mask_prefix)] + '0' * (32-int(mask_prefix))
int_network_1 = int(bin_network[0:8],2)
int_network_2 = int(bin_network[8:16],2)
int_network_3 = int(bin_network[16:24],2)
int_network_4 = int(bin_network[24:32],2)
mask_int = '1'*int(mask_prefix) + '0' * (32 - int(mask_prefix))
mask_1 = int(mask_int[0:8],2)
mask_2 = int(mask_int[8:16],2)
mask_3 = int(mask_int[16:24],2)
mask_4 = int(mask_int[24:32],2)
print('''
Network:
{int_network_1:8}  {int_network_2:8}  {int_network_3:8}  {int_network_4:8}
{int_network_1:08b}  {int_network_2:08b}  {int_network_3:08b}  {int_network_4:08b}

Mask:
/{mask_prefix}
{mask_1:<8}  {mask_2:<8}  {mask_3:<8}  {mask_4:<8}
{mask_1:<08b}  {mask_2:<08b}  {mask_3:<08b}  {mask_4:<08b}
'''.format(int_network_1=int_network_1,int_network_2=int_network_2,int_network_3=int_network_3,int_network_4=int_network_4,mask_prefix=mask_prefix,mask_1=mask_1,mask_2=mask_2,mask_3=mask_3,mask_4=mask_4))
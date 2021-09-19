# -*- coding: utf-8 -*-
"""
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.
"""

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
ospf_route = ospf_route.replace(',',' ')
ospf_route = ospf_route.strip().split()
ospf_route.pop(2)
ospf_1 = ospf_route[1].strip('[]')
ospf_route.pop(1)
ospf_route.insert(1, ospf_1)
template = '''
Prefix                {0}
AD/Metric             {1}
Next-Hop              {2}
Last update           {3}
Outbound Interface    {4}
'''
print(template.format(ospf_route[0],ospf_route[1],ospf_route[2],ospf_route[3],ospf_route[4]))
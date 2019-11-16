#!/usr/bin/python
# -*- coding: utf-8 -*-
def generate_page(head,body):
    page = f"<html>{head}{body}<p><hr><a href='index.html'>Основная страница</a></p></html>"
    return page


def generate_head(title):
    head = f"""<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <title>{title}</title>
    </head>"""
    return head


def generate_body(header):
    body = f"<h1>{header}</h1>" """<p>Параметры генерации: перечень всех использованных списков для генерации (времена дня, глаголы, ожидания). Каждый список — это элемент пронумерованного списка с его элементами внутри, как ненумерованный. Типа такого:</p>
    <p>1. Времена дня:<br><li>Утром.</li><br><li>Вечером.</li><br><li>После обеда.</li><br>2. Глаголы:<br><br><li>Остерегайтесь;</li><br><li>Ожидайте.</li></p>
    <img src='zodiak.jpg' width="100" height="100" alt="омоним?">"""



    return body



def save_page(title,header,output="about.html"):
    fp = open(output, "w")
    page = generate_page(
            head = generate_head(title),
            body = generate_body(header=header)
    )
    print(page,file = fp)
    fp.close
save_page(
    title = "О нас",
    header = "О чем все это"    
)




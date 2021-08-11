import os
from fpdf import FPDF
from math import ceil
from pathlib import Path
from pyfiglet import figlet_format


def read_user_input():

    out = figlet_format("Welcome", font="slant")
    print(out)

    print('================================================================')
    print('Please enter the desired settings for the output of the program:')
    print('================================================================')

    folder_names = input("Enter folders names containing images (separated by space): ") 
    print(f'You chose: {folder_names}')

    page_num = input("Enter page numbering desire (on or off): ")
    print(f'You chose: {page_num}')
    
    image_num = input("Enter image numbering desire (on or off): ") 
    print(f'You chose: {image_num}')
    
    img_per_p = input("Enter images per page (1, 2, 4, 6, 8, 15 or 24): ") 
    print(f'You chose: {img_per_p}')

    print('===================================')
    print('========Program has started========')
    print('===================================')
    
    return [folder_names, page_num, image_num, img_per_p]


def add_heading(heading, x=80, y=140):
    pdf.add_page()
    pdf.set_font('Times', 'B', 32)
    pdf.text(x, y, txt=heading)


def add_footer(page_number):
    pdf.set_font('Times', 'B', 18)
    pdf.text(100, 284, txt=f'- {page_number} -')


def get_files_list(path):
    return os.listdir(path)


def add_images_to_pdf_1(images, path_to_img, image_n, page_f, page_number):

    x, y, w, h = 25, 55, 160, 160
    image_number = 1

    for i in range(len(images)):
        pdf.add_page()
        
        if image_n == 'on':
            pdf.set_font('Times', 'B', 24)
            pdf.text(25, 50, txt=f'{image_number}.')
            image_number += 1

        pdf.image(path_to_img + images[i], x, y, w, h)
        
        if page_f == 'on':            
            add_footer(page_number)
            page_number += 1
    
    return page_number


def add_images_to_pdf_2(images, path_to_img, image_n, page_f, page_number):

    x, y, w, h = 50, 24, 110, 110
    image_number = 1
    pages = ceil(len(images) / 2)
    images_quantity = len(images)
    images_added = 0

    for i in range(pages):

        pdf.add_page()
        pdf.set_font('Times', 'B', 18)

        if images_added < images_quantity:
            pdf.image(path_to_img + images[i], x, y, w, h)
            images_added += 1
            if image_n == 'on':
                pdf.text(36.7, 28, txt=f'{image_number}.')
                image_number += 1

        if images_added < images_quantity:
            pdf.image(path_to_img + images[i + 1], x, y + 126, w, h)
            images_added += 1
            if image_n == 'on':
                pdf.text(36.7, 154, txt=f'{image_number}.')
                image_number += 1
        

        if page_f == 'on':
            add_footer(page_number)
            page_number += 1

    return page_number

def add_images_to_pdf_4(images, path_to_img, image_n, page_f, page_number):

    x, y, w, h = 25, 45, 72, 72
    image_number = 1
    pages = ceil(len(images) / 4)
    images_quantity = len(images)
    images_added = 0

    for i in range(pages):

        pdf.add_page()
        pdf.set_font('Times', 'B', 18)

        if images_added < images_quantity:
            pdf.image(path_to_img + images[i], x, y, w, h)
            images_added += 1
            if image_n == 'on':
                pdf.text(25, 43, txt=f'{image_number}.')
                image_number += 1

        if images_added < images_quantity:
            pdf.image(path_to_img + images[i + 1], x + 90, y, w, h)
            images_added += 1
            if image_n == 'on':
                pdf.text(115, 43, txt=f'{image_number}.')
                image_number += 1

        if images_added < images_quantity:
            pdf.image(path_to_img + images[i + 2], x, y + 95, w, h)
            images_added += 1
            if image_n == 'on':
                pdf.text(25, 138, txt=f'{image_number}.')
                image_number += 1

        if images_added < images_quantity:
            pdf.image(path_to_img + images[i + 3], x + 90, y + 95, w, h)
            images_added += 1
            if image_n == 'on':
                pdf.text(115, 138, txt=f'{image_number}.')
                image_number += 1

        if page_f == 'on':
            add_footer(page_number)
            page_number += 1

    return page_number


def add_images_to_pdf_6(images, path_to_img, image_n, page_f, page_number):

    x, y, w, h = 25, 25, 71, 71
    image_number = 1
    pages = ceil(len(images) / 6)
    images_quantity = len(images)
    images_added = 0

    for i in range(pages):

        pdf.add_page()
        pdf.set_font('Times', 'B', 18)

        if images_added < images_quantity:
            pdf.image(path_to_img + images[i], x, y, w, h)
            images_added += 1
            if image_n == 'on':
                pdf.text(25, 23, txt=f'{image_number}.')
                image_number += 1

        if images_added < images_quantity:
            pdf.image(path_to_img + images[i + 1], x + 90, y, w, h)
            images_added += 1
            if image_n == 'on':
                pdf.text(115, 23, txt=f'{image_number}.')
                image_number += 1

        if images_added < images_quantity:
            pdf.image(path_to_img + images[i + 2], x, y + 85, w, h)
            images_added += 1
            if image_n == 'on':
                pdf.text(25, 108, txt=f'{image_number}.')
                image_number += 1

        if images_added < images_quantity:
            pdf.image(path_to_img + images[i + 3], x + 90, y + 85, w, h)
            images_added += 1
            if image_n == 'on':
                pdf.text(115, 108, txt=f'{image_number}.')
                image_number += 1

        if images_added < images_quantity:
            pdf.image(path_to_img + images[i + 4], x, y + 170, w, h)
            images_added += 1
            if image_n == 'on':
                pdf.text(25, 193, txt=f'{image_number}.')
                image_number += 1

        if images_added < images_quantity:
            pdf.image(path_to_img + images[i + 5], x + 90, y + 170, w, h)
            images_added += 1
            if image_n == 'on':
                pdf.text(115, 193, txt=f'{image_number}.')
                image_number += 1

        if page_f == 'on':
            add_footer(page_number)
            page_number += 1

    return page_number


def add_images_to_pdf_8(images, path_to_img, image_n, page_f, page_number):

    image_number = 1
    pages = ceil(len(images) / 8)
    images_quantity = len(images)
    images_added = 0

    for i in range(pages):

        pdf.add_page()
        pdf.set_font('Times', 'B', 14)
        x, y, w, h = 30, 18, 58, 58
        count = 1

        for i in range(8):

            if images_added < images_quantity:
                if image_n == 'on':
                    pdf.text(x - 6.7, y + 3.6, txt=f'{image_number}.')
                    image_number += 1
                pdf.image(path_to_img + images[i], x, y, w, h)
                images_added += 1
                x += 85

            if count == 2:
                x = 30
                y += 66
                count = 0

            count += 1

        if page_f == 'on':
            add_footer(page_number)
            page_number += 1   


    return page_number


def add_images_to_pdf_15(images, path_to_img, image_n, page_f, page_number):

    image_number = 1
    pages = ceil(len(images) / 15)
    images_quantity = len(images)
    images_added = 0

    for i in range(pages):

        pdf.add_page()
        pdf.set_font('Times', 'B', 11)
        x, y, w, h = 25, 15, 48, 48
        count = 1

        for i in range(15):

            if images_added < images_quantity:
                if image_n == 'on':
                    pdf.text(x - 6.2, y + 2.4, txt=f'{image_number}.')
                    image_number += 1
                pdf.image(path_to_img + images[i], x, y, w, h)
                images_added += 1
                x += 56

            if count == 3:
                x = 25
                y += 53
                count = 0

            count += 1

        if page_f == 'on':
            add_footer(page_number)
            page_number += 1   


    return page_number


def add_images_to_pdf_24(images, path_to_img, image_n, page_f, page_number):

    image_number = 1
    pages = ceil(len(images) / 24)
    images_quantity = len(images)
    images_added = 0

    for i in range(pages):

        pdf.add_page()
        pdf.set_font('Times', 'B', 10)
        x, y, w, h = 20, 15, 38, 38
        count = 1

        for i in range(24):

            if images_added < images_quantity:
                if image_n == 'on':
                    pdf.text(x, y - 1.5, txt=f'{image_number}.')
                    image_number += 1
                pdf.image(path_to_img + images[i], x, y, w, h)
                images_added += 1
                x += 42

            if count == 4:
                x = 20
                y += 44
                count = 0

            count += 1

        if page_f == 'on':
            add_footer(page_number)
            page_number += 1   


    return page_number


user_input = read_user_input()

dirs = user_input[0].split()
page_f = user_input[1]
image_n = user_input[2]
img_per_p = int(user_input[3])


pdf = FPDF('P','mm','A4')
page_number = 1

for i in range(len(dirs)):

    print(f'Folder {dirs[i]} proccessing...')

    images = get_files_list(Path(f"{dirs[i]}/"))
    
    add_heading(input(f'Choose heading for images in folder {dirs[i]}: '))
    
    if img_per_p == 1:
        page_number = add_images_to_pdf_1(images, f'{dirs[i]}/', image_n, page_f, page_number)
    elif img_per_p == 2:
        page_number = add_images_to_pdf_2(images, f'{dirs[i]}/', image_n, page_f, page_number)
    elif img_per_p == 4:
        page_number = add_images_to_pdf_4(images, f'{dirs[i]}/', image_n, page_f, page_number)
    elif img_per_p == 6:
        page_number = add_images_to_pdf_6(images, f'{dirs[i]}/', image_n, page_f, page_number)
    elif img_per_p == 8:
        page_number = add_images_to_pdf_8(images, f'{dirs[i]}/', image_n, page_f, page_number)
    elif img_per_p == 15:
        page_number = add_images_to_pdf_15(images, f'{dirs[i]}/', image_n, page_f, page_number)
    elif img_per_p == 24:
        page_number = add_images_to_pdf_24(images, f'{dirs[i]}/', image_n, page_f, page_number)


pdf.output("result.pdf","F")
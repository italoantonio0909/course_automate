import re
import time

from config.settings import env_reader
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import UnexpectedAlertPresentException

from .selectors import course_by_id


def course_save_students(*, course_id: int):
    course = course_by_id(course_id=course_id)
    print(course.file_data)


def course_formated_string(*, course):
    course_name = course.split('(')
    course_name_striped = course_name[0].lower()

    return course_name_striped


def select_option(*, field, key: str):

    # Obtener la lista de las opciones disponibles del campo
    options = [x for x in field.find_elements_by_tag_name('option')]

    # Iterar sobre las opciones disponibles del campo
    for element in options:
        element_text = element.get_attribute('text')
        if element_text == key:
            element.click()


def select_course(
    *,
    field,
    course_name: str
):

    # Obtener los cursos
    courses = [x for x in field.find_elements_by_tag_name('option')]

    # Iterar los cursos disponibles
    for element in courses:
        course_attribute = element.get_attribute('text')

        # Quitando el paréntesis para hacer búsqueda de coincidencias -> (20 horas)
        course_name_formated = course_formated_string(course=course_attribute)
        course_formated = course_formated_string(course=course_name)

        # ¿ Coincide el curso de la base de datos con el parámetro de la iteración?
        match = re.match(course_formated, course_name_formated)
        if match:
            element.click()


def login(*, browser, username: str, password: str, course_name: str):

    # Credentials
    username = username
    password = password
    code = '85fda89'
    motive_default = 'CURSOS DE CAPACITACIÓN DEL INFOCENTRO'

    time.sleep(3)

    # Obteniendo elementos del DOM
    username_field = browser.find_elements_by_xpath(
        "//input[@name='TXT_USUARIO']")
    password_field = browser.find_elements_by_xpath(
        "//input[@name='TXT_CLAVE']")
    code_field = browser.find_elements_by_xpath("//input[@name='TXT_CODINF']")
    submit = browser.find_elements_by_xpath("//input[@name='BTN_ACCEDER']")
    motives_field = browser.find_element_by_xpath(
        "//select[@name='CMB_RAZONES']")

    time.sleep(3)

    select_option(field=motives_field, key=motive_default)

    time.sleep(3)

    # Seleccionar curso
    courses_field = browser.find_element_by_xpath(
        "//select[@name='CMB_PROGRAMAS']")
    select_course(field=courses_field, course_name=course_name)

    time.sleep(4)

    username_field[0].send_keys(username)
    password_field[0].send_keys(password)
    code_field[0].send_keys(code)

    time.sleep(5)

    # Envío del formulario
    submit[0].click()


def get_url(*, url: str):
    browser = webdriver.Chrome()
    browser.get(url)
    return browser


def course_assistance(*, course_id: int):
    url = 'https://siadi.mintel.gob.ec/siadi/ciudadanos/index.php'
    browser = get_url(url=url)

    # Obtener la lista de usuarios del curso
    course = course_by_id(course_id=course_id)

    # Iterar sobre los usuarios e iniciar sesión
    for user in course.user.all():
        username = user.identification
        password = user.identification
        login(
            browser=browser,
            username=username,
            password=password,
            course_name=course.title
        )


# def login_superuser(
#     *,
#     browser,
#     username: str,
#     password:str
#     ):

#     access_default = 'normal'
#     question_default = 'Actividad común en el fin de semana'
#     response_default = 'estudiar'

#     # Obteniendo elementos del DOM
#     username_field = browser.find_element_by_xpath("//input[@name='TXT_USUARIO']")
#     password_field = browser.find_element_by_xpath("//input[@name='TXT_CLAVE']")
#     access_field = browser.find_element_by_xpath("//select[@name='CMB_TIPO_ACCESO']")
#     submit = browser.find_element_by_xpath("//input[@name='BTN_ACCEDER']")

#     time.sleep(3)
#     username_field.send_keys(username)
#     password_field.send_keys(password)

#     # Obtener la lista de los accessos del ingreso a la plataforma
#     select_option(field=access_field, key=access_default)

#     # Obtener el elemento del DOM de las preguntas del ingreso a la plataforma
#     questions_field = browser.find_element_by_xpath("//select[@name='CMB_OID_PREGUNTAS_LOGIN']")

#     select_option(field=questions_field, key=question_default)

#     time.sleep(2)

#     #Obtener campo de respuesta
#     response = browser.find_element_by_xpath("//input[@name='TXT_RESPUESTA']")
#     response.send_keys(response_default)

#     time.sleep(12)


# def course_create():
#     chrome_options = Options()
#     chrome_options.add_argument("--disable-user-media-security=true")

#     url = 'https://siadi.mintel.gob.ec/siadi/funcionarios/index.php'
#     browser = webdriver.Chrome(options=chrome_options)
#     browser.get(url)

#     login_superuser(
#         browser=browser,
#         username='gpari.guai001',
#         password='Mindiolaza.2021'
#     )

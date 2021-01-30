from selenium import webdriver

import time
import random

#iyte mailin terminale karsı yapılan görsel erisimli bottur.

 
PATH = "chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://std.iyte.edu.tr")

data = """   
In recent years, graph theory has established itself as an important mathematical tool in
a wide variety of subjects, ranging from operational research and chemistry to genetics
and linguistics, and from electrical engineering and geography to sociology and architecture.
At the same time it has also emerged as a worthwhile mathematical discipline
in its own right.
In view of this, there is a need for an inexpensive introductory text on the subject,
suitable both for mathematicians taking courses in graph theory and also for nonspecialists
wishing to learn the subject as quickly as possible. It is my hope that this
book goes some way towards filling this need. The only prerequisites to reading it are
a basic knowledge of elementary set theory and matrix theory, although a further
knowledge of abstract algebra is needed for more difficult exercises.
The contents of this book may be conveniently divided into four parts. The first of
these (Chapters 1-4) provides a basic foundation course, containing definitions and
examples of graphs, connectedness, Eulerian and Hamiltonian paths and cycles, and
trees. This is followed by two chapters (Chapters 5 and 6) on planarity and colouring,
with special reference to the four-colour theorem. The third part (Chapters 7 and 8)
deals with the theory of directed graphs and with transversal theory, with applications
to critical path analysis, Markov chains and network flows. The book ends with a chapter
on matroids (Chapter 9), which ties together material from the previous chapters
and introduces some recent developments.
Throughout the book I have attempted to restrict the text to basic material, using
exercises as a means for introducing less important material. Of the 250 exercises,
some are routine examples designed to test understanding of the text, while others
will introduce you to new results and ideas. You should read each exercise,
whether or not you work through it in detail. Difficult exercises are indicated by an
asterisk.
I have used the symbol // to indicate the end of a proof, and bold-face type is used
for definitions. The number of elements in a set S is denoted by LSI, and the empty set
is denoted by 0.
A substantial number of changes have been made in this edition. The text has been
revised throughout, and some terminology has been changed to fit in with current
usage. In addition, solutions are given for some of the exercises; these exercises are
indicated by the symbols next to the exercise number. Several changes have arisen as
"""


try:

    driver.find_element_by_id("username").send_keys("xxxxxxxxxx@std.iyte.edu.tr")
    driver.find_element_by_id ("password").send_keys("*************")
    driver.find_element_by_class_name("ZLoginButton").click()    
    time.sleep(3)
    counter=0
    while(True):
        
        while True:
          x = chr(ord('a') + random.randint(0, 26))
          if x != "l": break
        for i in range(8):
          x += str(random.randint(0, 9))


        driver.find_element_by_id("zb__NEW_MENU").click()
        time.sleep(1)
        driver.find_element_by_id("zv__COMPOSE-1_to_control").send_keys("bilgehanay@std.iyte.edu.tr")
        driver.find_element_by_id("zv__COMPOSE-1_subject_control").send_keys(x)
        driver.find_element_by_id("ZmHtmlEditor1_body_ifr").send_keys((data))
        driver.find_element_by_id('zb__COMPOSE-1__SEND_left_icon').click()
        print("İsmi verilen kisiye {} tane mail gönderildi".format(counter))
        counter=counter+1
        time.sleep(1)
        


    
except IndexError as e:
    print("HATA VARDIR:")
    print(e)

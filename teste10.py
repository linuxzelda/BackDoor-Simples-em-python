import re
import urllib.request
import urllib


def my_test():
    my_str = re.compile(r"[\w+\d+]+@[gmail/hotmail/outlook/yahoo]+.com")

    my_site = "listadeemailmarketinggratis".split()

    for my_site in my_site:
        print("Procurando.. %s" % (my_site))
        try:
            my_url = urllib.request.urlopen("http://" + my_site + ".blogspot.com.br/2013/10/lista-1-6857-e-mails.html").read()
        except:
            my_url = urllib.request.urlopen("http://" + my_site + ".blogspot.com.br/2013/10/lista-1-6857-e-mails.html").read()

        new_url = my_url
        my_result = re.findall(my_str,str(new_url))

        with open("teste.txt","w") as msg_data:
           for my_result in my_result:
               msg_data.write(my_result + "\n\t")

if __name__ == '__main__':
    my_test()

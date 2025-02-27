import sign_in2
def main():
    while True:
       c=str(input("Do you want to SignUp? (Yes/No):"))
       if(c.lower()=="yes"):
          sign_in2.signup()
       d=str(input("Do you want to SignIn? (Yes/No):"))
       if(d.lower()=="yes"):
          sign_in2.check()
       e=str(input("Do you want to see database? (Yes/No):"))
       if(e.lower()=="yes"):
          sign_in2.show()

if __name__=="__main__":
    main()
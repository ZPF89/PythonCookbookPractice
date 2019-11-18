def greet_me(**kwargs):
  for key,value in kwargs.items():
    print("{0} == {1}".format(key,value))

greet_me(name="yasoob")
greet_me(name="aaabbb")
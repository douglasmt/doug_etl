# def decorating_greeting(function, *args):
#     def internal_decoration():
#         print("\nGot it!")
#         function(args)
#         print("Finishing!")

#     return internal_decoration

# def client_decorated(args):
#     name = args[0]
#     lista_incrementada = args[1] + [args[0]]
#     print(f"Please welcome {name} !")
#     print(lista_incrementada)
#     lista_incrementada.extend(['Fim'])
#     print(lista_incrementada)

# lista1 = [1,2,3,4]

# test = decorating_greeting(client_decorated, 'Douglas', lista1)

# test()

#########################################################################
# NEW FUNCTION WITH DECORATOR - and parameters
# def decorating_greeting(*args,**kwargs):
#     def internal_decoration(func):
#         print(f"\nGot it! {kwargs['name']}")
#         func()
#         print("Finishing!")

#         return func

#     return internal_decoration


# @decorating_greeting(name = 'Douglas')
# def client_decorated():
#     print("Inside actual functions")


# client_decorated()

#########################################################################
# NEW FUNCTION WITH DECORATOR - and parameters
def decorating_greeting(name, lista1):
    def internal_decoration(func):
        print(f"\nStarting the decorator")

        def wrapper(*args, **kwargs):
            lista_incrementada = lista1 + [name]
            print(f"Please welcome {name} !")
            print(lista_incrementada)
            func(*args, **kwargs)

        return wrapper

    return internal_decoration


def my_fun(*args):
    for ele in args:
        print(ele)


decorating_greeting('Douglas', [1, 2, 3, 4])(my_fun)(1, 2, "Gabriel")

# name = 'Douglas', list1 =[1,2,3,4]

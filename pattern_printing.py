# # # #
# # # #
# # # #
# # # #

for i in range(4):
    for j in range(4):
        print("# ", end="")
    print("\n")


#
# #
# # #
# # # #

    for i in range(4):
        for j in range(i+1):
            print("# ", end="")
        print("\n")


# # # #
# # #
# #
#

    for i in range(4):
        for j in range(4-i):
            print("# ", end="")
        print("\n")


for i in range(1, 5+1):
    print(("#" * i).rjust(5))

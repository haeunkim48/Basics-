# *
# **
# ***
# ****
# *****
# ******
# *******
# ********
# *********
# **********


# for i in range (10):
#     for j in range (1,1+i):
#         print ('*', end = "")
#     print()

# # ----------------

# for i in range(1,11):
#     s = ''
#     for j in range (i):
#         s += '*'
        
#     print (s)

#          *
#         **
#        ***
#       ****
#      *****
#     ******
#    *******
#   ********
#  *********
# **********

# for i in range (1,11):
#     print (" " * (10-i) + "*"*i)

#          *
#         ***
#        *****
#       *******
#      *********
#     ***********
#    *************
#   ***************
#  *****************
# *******************

for i in range (1,11):
    print (" "*(10-i) + "*"*(2*i-1))
    


from instapy import InstaPy

#login sectoin
session = InstaPy(username="weixiang_w", password="27092916")
session.login()
print("\nYou're logged in\n")

#like section
session.like_by_tags(["C++", "C language", "Python", "Java", "Blender animation"], amount=10)
print("\nYour liking is done\n")

#follow section
session.set_do_follow(True, percentage=25)
print("\nYour following is done\n")

#comment section
session.set_do_comment(True, percentage=50)
session.set_comments(["Love it", "Nice post", u"Nice post 😍"])
print("\nYour commenting is done\n")
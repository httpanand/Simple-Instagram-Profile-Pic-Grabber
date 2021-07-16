import instaloader

mod=instaloader.Instaloader()

user=input("Enter Insta Username -")

mod.download_profile(user,profile_pic_only=True)

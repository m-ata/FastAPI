
videos = [
    {"name": "Intro to Python", "duration": "5:32"},
    {"name": "Data Types in Python", "duration": "7:15"},
    {"name": "Loops Explained", "duration": "9:08"},
    {"name": "Functions in Python", "duration": "6:40"},
    {"name": "OOP Basics", "duration": "8:22"}
]

def list_all_videos():
    # video = (", ").join(f"Video : {key} , Duration : {value}"  for key , value in videos.items())
    print("\n")
    print("Video List | Watch  a Video ")
    video = (" ").join(f"\n {index} - Video : {video["name"]} , Duration : {video["duration"]}\n"  for  index,video in enumerate(videos, start=1))
    print(video)


def updating_video(opt):
        print("\n")
        fetched_video={}
        print("Write Video Details to Update | Enter details and press 'Enter' ")
        for index, video in enumerate(videos, start=1):
            if index == opt:
                fetched_video = video
        print("\nPrevios Details : ")
        print(f"Video name {fetched_video["name"]}  | Duration {fetched_video["duration"]}\n")
        video_name= str(input("Enter the Video Name : "))
        video_dura= str(input("Enter the Video Duration : "))
        videos[opt-1]={"name":video_name, "duration": video_dura} 
        print("***Video Details Updated Successfully***")
        list_all_videos()

def deleting_video(option):
        print("\n")
        print(" Are you sure ? | Write 'Yes' to Delete  and press 'Enter' \n")
        delete_auth= str(input("Are you sure want to delete ?  : "))
        if delete_auth == "Yes" or "yes":
            del videos[option - 1]
        print("***Video Delete Successfully***\n")
        list_all_videos()
        return


def update_a_video_detail():
    print("\n")
    print("Update Video Detail | Enter the Video Number to update the Detail ")
    video = (" ").join(f"\n {index} - Video : {video["name"]} , Duration : {video["duration"]}\n"  for  index,video in enumerate(videos, start=1))
    print(video,"\n")

    option = int(input("Enter the Video Number : "))
    videos_length = len(videos)
    case_status = 0
    if option > videos_length:
        case_status= 0
        print("\nNo Video Exist")
    elif 0 < option <= videos_length:
        case_status = 1
        updating_video(option)
    else:
        print("\nInvalid Video Number")

    
def delete_a_video_detail():
    print("\n")
    print("Delete Video | Enter the Video Number to delete the Video ")
    list_all_videos()

    option = int(input("Enter the Video Number : "))
    videos_length = len(videos)
    case_status = 0
    if option > videos_length:
        case_status= 0
        print("\nNo Video Exist")
    elif 0 < option <= videos_length:
        case_status = 1
        deleting_video(option)
    else:
        print("\nInvalid Video Number")

    
    match option:
        case opt if opt == case_status:
            update_a_video_detail()
        case opt if opt != case_status:
            pass


def add_a_video():
    print("\n")
    print("Add a Video | Enter details and press 'Enter' ")
    video_name= str(input("Enter the Video Name : "))
    video_dura= str(input("Enter the Video Duration : "))
    videos.append({"name":video_name, "duration": video_dura})
    print("*** Video Added Successfully ***")
    list_all_videos()


while True:
    print("Youtube Manager | Choose an Option : ")

    print("1 - List all Youtube Videos")
    print("2 - Add a Youtube Videos")
    print("3 - Update a Youtube Videos Details")
    print("4 - Delete a Youtube Video")
    print("5 - Exit from App")
    print("\n")
    option = int(input("Enter your option : "))

    match str(option):
        case '1':
            list_all_videos()
        case '2':
            add_a_video()
        case '3':
            update_a_video_detail()
        case '4':
            delete_a_video_detail()
        case '5':
            break
        case _:
            print("Invalid Option")
            
import json

def load_videos():
    try:
        with open("youtube.txt",'r') as file:
            test = json.load(file)
            return test
        
    except FileNotFoundError:
        return []
    
def data_save_helper(videos):               # videos ko save/changes kar dega main file mai jaha store hai sab videos
    with open("youtube.txt",'w') as file:
        json.dump(videos,file,indent=4)


def list_all_videos(videos):
    print("\n")
    print("=" * 100)
    for index,video in enumerate(videos ,start=1):
        print(f"{index}. Name : {video['name']}, Duration : {video['time']} .")
    print("\n")
    print("=" * 100)


def add_video(videos):
    name=input("Enter video name : ")
    time=input("Enter video time : ")
    videos.append({'name':name,'time':time})
    data_save_helper(videos)
    
def update_video(videos):
    list_all_videos(videos)
    index=int(input("Enter the video number to update ."))
    if 1<=index<=len(videos):
        name=input("Enter new name for video : ")
        time=input("Enter new time for video : ")
        videos[index-1]={'name': name,'time':time}
        data_save_helper(videos)
    else :
        print("Please Enter correct index !  ")
        
def delete_video(videos):
    list_all_videos(videos)
    index=int(input("Enter the video number to delete : "))
    if 1<=index<=len(videos):
        del videos[index-1]
        print(f"Video {index} has been Deleted .")
        data_save_helper(videos)
    else:
        print("Please Enter correct index ! ")
def main():
    
    videos = load_videos()

    while True:
        print("\n YouTube Manager | Enter an Choice ")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")
        choice=input("Enter your choice : ")
        # print("\n")
        # print(videos)


        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break 
            case _:
                print("Wrong choice !!")
                
if __name__ == "__main__":
    main()
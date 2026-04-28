import json
FILE = 'youtube manager/youtube.txt'

def load_data():
    try:
        with open(FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(videos):        
    with open(FILE, 'w') as file:
        json.dump(videos, file)

# def list_all_videos(videos):
#     print("\n" + "\n")
#     for index,video in enumerate(videos, start=1):
#         print(f"{index}. name: {video['name']}, Time: {video['time']}")
#     print("\n" + "\n")

def list_all_videos(videos):
    print("\n")
    
    # Header
    print(f"{'No.':<5} {'Name':<30} {'Time':<10}")
    print("-" * 50)
    
    # Rows
    for index, video in enumerate(videos, start=1):
        print(f"{index:<5} {video['name']:<30} {video['time']:<10}")
    
    print("\n")

def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    print("\n" + "\n")
    videos.append({'name': name, 'time': time}) 
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    video_index = int(input("Enter the video number to update: "))
    print("\n" + "\n")
    if 0 < video_index <= len(videos):
        name = input("Enter new video name: ")
        time = input("Enter new video time: ")
        videos[video_index - 1] = {'name': name, 'time': time}
        save_data_helper(videos)

def delete_video(videos):
    list_all_videos(videos)
    video_index = int(input("Enter the video number to delete: "))
    print("\n" + "\n")
    if 0 < video_index <= len(videos):
        del videos[video_index - 1]
        save_data_helper(videos)

def main():
    videos = load_data()

    while True : 
        print("Welcome to YouTube Manager")
        print("1. List all videos")
        print("2. Add a video")
        print("3. Update a video details")
        print("4. Delete a video")
        print("5. Exit the program")
        print()
        choice = input("Enter your choice: ")
        print()

        match choice :
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
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
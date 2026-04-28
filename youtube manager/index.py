import sqlite3
con = sqlite3.connect('youtube manager/youtube_manager.db')
cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS videos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    time TEXT NOT NULL
)''')

def load_data():
    cur.execute("SELECT * FROM videos")
    rows = cur.fetchall()
    return [{'id': row[0], 'name': row[1], 'time': row[2]} for row in rows]

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
    cur.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    con.commit()

def update_video(videos):
    list_all_videos(videos)
    video_index = int(input("Enter the video number to update: "))
    print("\n" + "\n")
    if 0 < video_index <= len(videos):
        name = input("Enter new video name: ")
        time = input("Enter new video time: ")
        videos[video_index - 1] = {'name': name, 'time': time}
        cur.execute("UPDATE videos SET name=?, time=? WHERE id=?", (name, time, videos[video_index - 1]['id']))
        con.commit()
    else:
        print("Invalid video number.")

def delete_video(videos):
    list_all_videos(videos)
    video_index = int(input("Enter the video number to delete: "))
    print("\n" + "\n")
    if 0 < video_index <= len(videos):
        del videos[video_index - 1]
        cur.execute("DELETE FROM videos WHERE id=?", (videos[video_index - 1]['id'],))
        con.commit()
    else:
        print("Invalid video number.")

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
        con.close()

if __name__ == "__main__":
    main()
import sqlite3

# Global connection and cursor
connection = sqlite3.connect("db-youtube.db")
cursor = connection.cursor()

def create_table():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS videos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            duration TEXT NOT NULL
        )
    ''')
    connection.commit()


def list_all_videos():
    cursor.execute("SELECT * FROM videos")
    videos = cursor.fetchall()
    if not videos:
        print("No videos found.")
    print("---- ALL VIDEOS ----")
    for index ,video in enumerate(videos):
        # print(f"No #-{index+1} VIDEO - {video[1]}  ")
        print(f"\nNo #-{index+1} VIDEO - {video[1]}  DURATION - {video[2]}")
    print("\n--------")

def add_a_video(name, duration):
    cursor.execute(
        "INSERT INTO videos (name, duration) VALUES (?, ?)",
        (name, duration)
    )
    connection.commit()
    print("Video added successfully.\n")

def update_a_video_detail(video_id, new_name, new_duration):
    cursor.execute(
        "UPDATE videos SET name = ?, duration = ? WHERE id = ?",
        (new_name, new_duration, video_id)
    )
    connection.commit()
    print("Video updated successfully.\n")

def delete_a_video_detail(dlt_video_id):
    cursor.execute(
        "DELETE FROM videos WHERE id = ?",
        (dlt_video_id,)
    )
    connection.commit()
    print("Video deleted successfully.\n")

def main_menu():
    while True:
        print("Youtube Manager | Choose an Option :\n")
        print("1 - List all Youtube Videos")
        print("2 - Add a Youtube Video")
        print("3 - Update a Youtube Video's Details")
        print("4 - Delete a Youtube Video")
        print("5 - Exit from App\n")

        try:
            option = int(input("Enter your option: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.\n")
            continue

        if option == 1:
            list_all_videos()
        elif option == 2:
            print("\nAdd a Video")
            name = input("Enter the Video Name: ")
            duration = input("Enter the Video Duration: ")
            add_a_video(name, duration)
        elif option == 3:
            print("\nUpdate Video Detail")
            try:
                video_id = int(input("Enter the Video ID: "))
            except ValueError:
                print("Invalid ID. Must be a number.\n")
                continue
            name = input("Enter the new Video Name: ")
            duration = input("Enter the new Video Duration: ")
            update_a_video_detail(video_id, name, duration)
        elif option == 4:
            print("\nDelete Video")
            try:
                video_id = int(input("Enter the Video ID to delete: "))
            except ValueError:
                print("Invalid ID. Must be a number.\n")
                continue
            delete_a_video_detail(video_id)
        elif option == 5:
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid Option. Please choose between 1 to 5.\n")

def main():
    create_table()
    main_menu()
    connection.close()

if __name__ == '__main__':
    main()

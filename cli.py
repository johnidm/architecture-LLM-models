import httpx
import json
import time


API_HOST = "http://0.0.0.0:8000"


def generate_text(prompt):
    url = f"{API_HOST}/generate/"
    response = httpx.post(url, json={"prompt": prompt})
    data = response.json()
    return data["task_id"]


def get_task_status(task_id):
    url = f"{API_HOST}/task/{task_id}"
    response = httpx.get(url)
    data = response.json()
    return data


def main():
    prompt = input("Enter the prompt: ")

    task_id = generate_text(prompt)    
    while True:
        data = get_task_status(task_id)
        if "Task not completed yet" not in data["status"]:
            print(data)
            break
        time.sleep(2)


if __name__ == "__main__":
    main()

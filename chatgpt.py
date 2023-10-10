from fastapi import FastAPI, HTTPException
import openai
from datasource import SqlData


class MyOpenAI:

    def __init__(self):
        pass

    @staticmethod
    def chat(prompt: str):
        openai.api_key = open("/Users/user/openapi_key.txt", "r").read().strip('\n')
        history = SqlData.sql("select * from my_chat order by id")

        messages = []
        for m in history:
            message = {"role": m['role'], "content": m['content']}
            messages.append(message)

        messages.append({"role": "user", "content": prompt})

        try:
            post = {"table_name": "my_chat", "action": "insert", "role": "user", "content": prompt}
            SqlData.post(post)
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                max_tokens=300
            )
            role = completion.choices[0].message.role
            content = completion.choices[0].message.content
            post = {"table_name": "my_chat", "action": "insert", "role": role, "content": content}
            SqlData.post(post)
            return completion
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Error processing POST data: {str(e)}")

    @staticmethod
    def clear():
        sql = "delete from my_chat"
        SqlData.execute(sql)
        return {"result": "done"}
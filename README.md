# Real-world LLM Applications

Building scalable consumer of LLM models


### Tech stack:

- Redis
- Celery
- FatAPI
- LangChain 
- Open AI
- HuggingFace

### Step to up the application:

Use Python version **3.10.x**

- `docker run --name redis-db -p 6379:6379 -d redis`
- `pip install --no-cache-dir -r requirements.txt`
- `uvicorn app:app --host 0.0.0.0 --port 8000 --reload`
- `celery -A tasks worker -n worker1 -P prefork -l INFO`

### How to make a question

```
python cli.py
```

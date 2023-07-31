from celery import Celery, signals
from loader import ModelFake, ModelOpenAI, HFStarchat
import time
import torch
import functools


def make_celery():
    backend = broker = "redis://0.0.0.0:6379/0"
    return Celery("LLM-worker", backend=backend, broker=broker)


celery = make_celery()

model = None


@signals.worker_process_init.connect
def setup_model(signal, sender, **kwargs):
    global model
    model = HFStarchat()


@celery.task
def generate_task(text: str):
    text, time = do_model_generate(text)
    return time, text


def time_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        exec_time = end_time - start_time
        return (result, exec_time)

    return wrapper


@time_decorator
def do_model_generate(text: str):
    outputs = model.generate(text)
    return outputs

import asyncio
import time
from pathlib import Path

async def fake_fetch(url, out_file):
    await asyncio.sleep(1)  # simula latência
    Path(out_file).write_text(f"Conteúdo baixado de {url}", encoding="utf-8")
    return out_file

async def fake_downloads(urls, out_dir="downloads"):
    Path(out_dir).mkdir(exist_ok=True)
    tasks = []
    for i, url in enumerate(urls, 1):
        out_file = Path(out_dir) / f"file_{i}.txt"
        tasks.append(fake_fetch(url, out_file))
    return await asyncio.gather(*tasks)

def run_fake_downloads(urls):
    start = time.time()
    results = asyncio.run(fake_downloads(urls))
    print(f"⏱️ Tempo total: {time.time() - start:.2f}s")
    return results

async def periodic_task(interval=2, count=3):
    for i in range(count):
        print(f"🔄 Tarefa periódica {i+1}/{count}")
        await asyncio.sleep(interval)
    return "Finalizado"

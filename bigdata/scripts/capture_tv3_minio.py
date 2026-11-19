"""Chụp Console MinIO thật. Cần pip install playwright và Chrome cài trên máy.

PYTHONPATH=. python scripts/capture_tv3_minio.py --phase after
"""
import argparse
import os
from pathlib import Path

from playwright.sync_api import sync_playwright

from src.config import MINIO_ACCESS_KEY, MINIO_BUCKET_NAME, MINIO_SECRET_KEY, PROJECT_ROOT


def capture(phase, console_url, chrome):
    output = PROJECT_ROOT / 'docs' / 'screenshots'
    output.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(executable_path=chrome, headless=True)
        try:
            context = browser.new_context(viewport={'width': 1440, 'height': 1000})
            page = context.new_page()
            page.goto(console_url, wait_until='networkidle')
            page.locator('input[name="accessKey"]').fill(MINIO_ACCESS_KEY)
            page.locator('input[name="secretKey"]').fill(MINIO_SECRET_KEY)
            page.get_by_role('button', name='Login', exact=True).click()
            page.wait_for_url('**/browser**')
            page.wait_for_load_state('networkidle')
            acknowledge = page.get_by_role('button', name='Acknowledge', exact=True)
            if acknowledge.count():
                acknowledge.click()
            page.goto(f'{console_url}/browser/{MINIO_BUCKET_NAME}', wait_until='networkidle')

            def screenshot(name):
                page.screenshot(path=str(output / name))
                print(f'[SCREENSHOT] {name}: {page.url}')

            screenshot(f'tv3_minio_bucket_{phase}.png')
            for folder in ['bronze', 'transactions']:
                page.get_by_text(folder, exact=True).dblclick()
                page.wait_for_load_state('networkidle')
            page.get_by_text('tx_date=2026-11-09', exact=True).wait_for()
            screenshot(f'tv3_minio_dates_{phase}.png')
            page.get_by_text('tx_date=2026-11-09', exact=True).dblclick()
            page.get_by_text('tx_type=TRANSFER', exact=True).wait_for()
            screenshot(f'tv3_minio_types_{phase}.png')
            page.get_by_text('tx_type=TRANSFER', exact=True).dblclick()
            page.get_by_text('.snappy.parquet', exact=False).first.wait_for()
            screenshot(f'tv3_minio_{phase}_compaction.png')
            page.goto(f'{console_url}/browser/{MINIO_BUCKET_NAME}', wait_until='networkidle')
            for folder in ['quarantine', 'bad_transactions', 'rejected_date=2026-11-10']:
                page.get_by_text(folder, exact=True).dblclick()
                page.wait_for_load_state('networkidle')
            page.get_by_text('.snappy.parquet', exact=False).first.wait_for()
            screenshot(f'tv3_minio_quarantine_{phase}.png')
        finally:
            browser.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--phase', choices=['before', 'after'], required=True)
    parser.add_argument('--console-url', default='http://127.0.0.1:9001')
    parser.add_argument('--chrome', default=os.getenv('CHROME_BIN', '/usr/bin/google-chrome'))
    args = parser.parse_args()
    capture(args.phase, args.console_url.rstrip('/'), args.chrome)

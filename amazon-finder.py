#!/usr/bin/env python3

from openai import OpenAI
import os

header_format="""
---
author: ["Joy Doe"]
title: ""
date: ""
description: ""
summary: ""
tags: ["", "", "", ""]
categories: ["", ""]
ShowToc: true
TocOpen: true
---
"""

def translate_text(api_key, text):
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": f"You're a personnal shopping assistant. You'll look on amazon and give links to the user"},
            {"role": "system", "content": f"You'll ensure the links are valid and match the description"},
            {"role": "user", "content": text}
        ],
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.5
    )
    return response.choices[0].message.content.strip()

def write_article(api_key, input_file_path, output_file_path):
    with open(input_file_path, 'r') as file:
        text = file.read()

    translated_text = translate_text(api_key, text)

    with open(output_file_path, 'w') as file:
        file.write(translated_text)

    print(f"Article completed: text saved to {output_file_path}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Translate text file using OpenAI API")
    parser.add_argument("input_file", help="Path to the input text file")
    parser.add_argument("output_file", help="Path to save the translated text file")

    args = parser.parse_args()

    api_key = os.getenv("OPENAI_API_KEY")
    write_article(api_key, args.input_file, args.output_file)


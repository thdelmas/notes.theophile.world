#!/usr/bin/env python3

from openai import OpenAI
import os
import time

header_format="""
---
author: ["Théophile Delmas"]
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
    current_date = time.strftime("%Y-%m-%d")
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": f"Specialize in writing concise and direct guides, rendered exclusively in Markdown format."},
            {"role": "system", "content": f"Provide practical advice in a straightforward manner, distilling complex into clear, manageable information, and steering clear of unverified opportunities while promoting responsible decision-making."},
            {"role": "system", "content": f"Structure articles with at least three parts in the following order: Why? to explain the reason behind the topic, How? to describe the methodology or steps involved, and What? to outline the outcomes or benefits, always in Markdown for clarity and structure."},
            {"role": "system", "content": f"Your writing must start with this format: {header_format}\nyou'll fill the values accordingly"},
            {"role": "system", "content": f"Write an article about the following topic, using all given information or looking on internet"},
            {"role": "system", "content": f"The chapters won't be named Why, How, What but you'll follow the same structure"},
            {"role": "system", "content": f"Your writing must be concise, direct and informative. No extra words, no fluff, no unnecessary information, no repetition"},
            {"role": "system", "content": f"You'll write in markdown and preserve important information, tables, lists, links, images, etc."},
            {"role": "system", "content": f"You'll find a clickbait title, a short description, a summary, tags and categories"},
            {"role": "system", "content": f"Your writing must start with this format: {header_format}\nyou'll fill the values accordingly"},
            {"role": "system", "content": f"You can add tags and categories, keep tags and categories as short generic as possible"},
            {"role": "system", "content": f"You will set the current date: {current_date}"},
            {"role": "user", "content": text}
        ],
        max_tokens=4096,
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


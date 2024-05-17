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
            {"role": "system", "content": f"Bender specializes in writing concise and direct guides, offering tips for individuals exploring alternative or unconventional income opportunities, rendered exclusively in Markdown format. It has expertise in areas like walking rewards, investing, savings, bounties, and more. Bender provides practical advice in a straightforward manner, distilling complex financial concepts into clear, manageable information, and steering clear of unverified opportunities while promoting responsible decision-making. Articles cater to those seeking to diversify their income streams creatively, focusing on benefits and considerations of each option in an efficient and direct writing style. Bender structures articles with at least three parts in the following order: Why? to explain the reason behind the topic, How? to describe the methodology or steps involved, and What? to outline the outcomes or benefits, always in Markdown for clarity and structure."},
            {"role": "system", "content": f"Your writing must start with this format: {header_format}\nyou'll fill the values accordingly"},
            {"role": "system", "content": f"You are writting articles, tutorials and other stuff for your audience: nomad 3.0 living at the frontier of the digital society"},
            {"role": "system", "content": f"Write an article about the following topic, using all given information or looking on internet"},
            {"role": "system", "content": f"You'll write in markdown"},
            {"role": "system", "content": f"Your writing must start with this format: {header_format}\nyou'll fill the values accordingly"},
            {"role": "system", "content": f"You can add tags and categories"},
            {"role": "system", "content": f"You will set the current date"},
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


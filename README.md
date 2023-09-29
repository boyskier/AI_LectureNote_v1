# AI_LectureNote_v1
> ## Transform Your Medical Lectures Into Smart Scripts: Accuracy Meets Efficiency
An automation tool that converts lecture recordings into scripts and summaries. Unlike similar services like Naver Clova Note and Daglo, our software offers unique features tailored for medical education. It translates all medical terminology into English and eliminates filler words and stutters.

For example:
- Original: "3번은 닉몬이야. 그래서 폐렴이라고 하는 거는"  
  Processed: "3위는 Pneumonia입니다. 그래서 Pneumonia이"

- Original: "이 암이라는 것은 mmr살프로리퍼레이션 서브와이블 때문에 생기는 질환이에요."  
  Processed: "Cancer는 주로 MMR (Mismatch Repair) 때문에 발생하는 disease입니다."

The summaries generated are succinct and accurate, and even include a content review quiz.

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Configuration](#configuration)
- [How it Works](#how-it-works)
  - [File Scanning](#file-scanning)
  - [Text Processing](#text-processing)
  - [File Movement](#file-movement)
  - [Error Handling](#error-handling)
- [Usage](#usage)
- [Customization Options](#customization-options)
- [Directory Structure](#directory-structure)
- [File Naming Convention](#file-naming-convention)
- [Contributors](#contributors)
- [Contact](#contact)

## Overview
This Python script automatically processes raw text files by correcting errors, translating to English, summarizing the content, and converting it to a Word document.

## Prerequisites
- Python 3.x
- OpenAI API Key
- Following Python packages:
  - `python-dotenv`
  - `openai`
  - `docx`

Run the following commands to install the necessary packages:
```bash
pip install python-dotenv openai docx
```
## Configuration
1. Create a `.env` file in the root directory and add your OpenAI API Key:
    ```text
    OPEN_API_KEY=your-api-key
    ```
2. Update the `raw_root_dir` variable with your actual root directory path for raw text files.

## How it Works

### File Scanning
The function `get_txt_files` scans the `raw_root_dir` for all `.txt` files.

### Text Processing
`raw_text_to_product` performs multiple operations on each text file:
  - Correction
  - Translation to English
  - Summarization

### File Movement
After processing, the raw text file is moved to the `used_raw_root_dir`.

### Error Handling
The script retries up to 5 times if any errors are encountered.

## Usage
Run the txt_to_product.ipynb to start the automated process. It will process all raw text files in the `raw_root_dir`.

## Customization Options
- **Location of Raw Files**: The location specified by `raw_root_dir` in `txt_to_product.ipynb` can be changed according to your needs.
- **File Organization**: After the script and summary are generated, they can be organized using `OrganizeFiles.ipynb`.

## Directory Structure
- Raw files: Placed in `raw_root_dir`
- Processed files: Moved to `used_raw_root_dir`
- Intermediate and final products: Stored in `intermediate`, `englished`, and `summary` directories

## File Naming Convention
Raw text files must follow this naming convention:
`raw_subject_week_day_numb.txt`

## Contributors
- LEE KYEONGEON
- KIM TAEHONG

## Contact
For any questions or further information, feel free to reach out at [boy.skier@g.skku.edu](mailto:boy.skier@g.skku.edu).

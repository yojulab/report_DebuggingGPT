import json

prompt_template_first = {
    "description": "Alpaca-LoRA Custom prompt template",
    "prompt_input": (
        "Identify and correct the error(s) in the following Java code.\n"
        "다음의 Java에서 오류를 찾아 수정하세요. \n\n"
        "Explain the correction(s) and provide a brief description of the error(s).\n"
        "수정 사항을 설명하고 오류에 대한 간단한 설명을 제공하세요.\n\n"
        "### Instruction(명령어):\n{instruction}\n\n### Input(입력):\n{input}\n\n### Response:\n"
    ),
    "prompt_no_input": (
        "Below is an instruction that describes a task.\n"
        "아래는 작업을 설명하는 명령어입니다.\n\n"
        "Write a response that appropriately completes the request.\n"
        "명령어에 따른 요청을 적절히 완료하는 응답을 작성하세요.\n\n"
        "### Instruction(명령어):\n{instruction}\n\n### Response:\n"
    ),
    "response_split": "### Response:",
}

prompt_template_second = {
    "description": "Alpaca-LoRA Custom prompt template",
    "prompt_input": (
        "Review the following Java code and identify any potential runtime error(s).\n"
        "다음 Java 코드를 검토하고 잠재적인 런타임 오류를 식별하십시오.\n\n"
        "Suggest the necessary modification(s) to avoid the error(s) and explain the reason behind the potential error(s) and the correction(s)\n"
        "오류를 방지하기 위해 필요한 수정을 제안하고 잠재적 오류 및 수정 이면의 이유를 설명하십시오 \n\n"
        "### Instruction(명령어):\n{instruction}\n\n### Input(입력):\n{input}\n\n### Response:\n"
    ),
    "prompt_no_input": (
        "Below is an instruction that describes a task.\n"
        "아래는 작업을 설명하는 명령어입니다.\n\n"
        "Write a response that appropriately completes the request.\n"
        "명령어에 따른 요청을 적절히 완료하는 응답을 작성하세요.\n\n"
        "### Instruction(명령어):\n{instruction}\n\n### Response:\n"
    ),
    "response_split": "### Response:",
}

prompt_template_third = {
    "description": "Alpaca-LoRA Custom prompt template",
    "prompt_input": (
        "Examine the given Java code and identify the logical error(s) present. \n"
        "지정된 Java 코드를 검사하고 존재하는 논리적 오류를 식별합니다.\n\n"
        "Propose the correction(s) required to fix the logic and provide an explanation of the error(s) and the correction(s).\n"
        "논리를 수정하는 데 필요한 수정을 제안하고 오류 및 수정에 대한 설명을 제공합니다.\n\n"
        "### Instruction(명령어):\n{instruction}\n\n### Input(입력):\n{input}\n\n### Response:\n"
    ),
    "prompt_no_input": (
        "Below is an instruction that describes a task.\n"
        "아래는 작업을 설명하는 명령어입니다.\n\n"
        "Write a response that appropriately completes the request.\n"
        "명령어에 따른 요청을 적절히 완료하는 응답을 작성하세요.\n\n"
        "### Instruction(명령어):\n{instruction}\n\n### Response:\n"
    ),
    "response_split": "### Response:",
}

# save path
datas_filepath = 'Datas/custom.json'

# upload templates/custom.json
prompt_template = prompt_template_first
with open(datas_filepath, 'w', encoding='utf-8') as f:
    json.dump(prompt_template, f, ensure_ascii=False)

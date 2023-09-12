import openai

openai.api_key = 'api-key'

prompts_list = [
    {'prompt_id': 1, 'question': 'Which player has done most kills?'},
    {'prompt_id': 2, 'question': 'Which player has done most damage?'},
    {'prompt_id': 3, 'question': 'Which player has suffered most damage?'},
    {'prompt_id': 4, 'question': 'Which is most purchased weapon by each team?'},
    {'prompt_id': 5, 'question': 'Which player has done most weapon purchase among all?'},
    {'prompt_id': 6, 'question': 'Which player has done most weapon purchase in each team?'},
    {'prompt_id': 7, 'question': 'Which is most dropped weapon by each team?'},
    {'prompt_id': 8, 'question': 'Which is most picked up weapon by each team?'}
]

prompt_ids = [prompt['prompt_id'] for prompt in prompts_list]

def get_prompt(prompt_id):
    for prompt in prompts_list:
        if prompt['prompt_id'] == prompt_id:
            return prompt
    return None

def prepare_prompt(prompt_id=0, data_set={}):

    if not prompt_id or prompt_id not in prompt_ids or not data_set:
        return ""

    question_set = get_prompt(prompt_id)['question']

    if not question_set:
        return ""

    prompt = f"""
        You are an helpful assistant who have good knowledge of e-sports and games like counter strike go i.e. CSGO.
        Below is a set of JSON data that you need to analyse and refer to for answering questions.

        {data_set}

        -------------------------------------

        Using above JSON data for CSGO game, answer the following questions:

        {question_set}

        Please give concise and direct answer instead of explaining too much.

    """
    return prompt


def gpt_api(prompt_id=0, data_set={}):
    messages = [{"role": "system", "content": "You are a intelligent assistant."}]

    _prompt = prepare_prompt(prompt_id=prompt_id, data_set=data_set)
    if not _prompt:
        return "Oops, something went wrong! Prompt is not configured properly. Please fix prompt and retry!"

    messages.append({"role": "user", "content": _prompt},)

    try:
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
    except:
        reply = "Oops, something went wrong! Either data size is more than 40000 characters or OpenAI is rate limiting. Please try later on!"

    return reply


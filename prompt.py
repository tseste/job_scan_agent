REACT_PROMPT_WITH_FORMAT_INSTRUCTIONS = """
Answer the following questions as best you can. You have access to the following tools:

{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do, CRITICAL: Your next step MUST be an action. Do not skip the 'Action:' tag.
Action: the action to take, should be one of [{tool_names}], CRITICAL: Your next step MUST be an action input. Do not skip the 'Action Input:' tag.
Action Input: the input to the action, don't skip Action input even if it is empty
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question formatted according to format_instructions with links: {format_instructions}

Begin!

Question: {input}
Thought:{agent_scratchpad}
"""

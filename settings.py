# system info
DEVICE = 'cuda'
N_WORKERS = 24  # Number of concurrent VQA tasks. It can be modified to fit the rate limit of your API

# OpenAI settings
OPENAI_API_ENDPOINT = ''  # ENTER YOUR OWN ENDPOINT
OPENAI_API_KEY = ''       # ENTER YOUR OWN KEY

# Qwen (Aliyun) settings
QWEN_API_ENDPOINT = ""   # ENTER YOUR OWN ENDPOINT
QWEN_API_KEY = ''        # ENTER YOUR OWN KEY

# Set vision detail level for all agents
API_VISION_DETAIL_LEVEL = 'high'

# ROI description model settings
ROI_DESC_MODEL = 'gpt-4.1-mini'
ROI_DESC_TEMPERATURE = 0.0
ROI_DESC_REASONING_EFFORT = 'low'        # for gpt-5.x
# Task Agent model settings
TASK_AGENT_MODEL = 'gpt-4.1'
TASK_AGENT_TEMPERATURE = 0.0
TASK_AGENT_REASONING_EFFORT = 'medium'   # for gpt-5.x

# VQA judge model settings
EVAL_MODEL = 'gpt-4.1-nano'
EVAL_TEMPERATURE = 0.0

# Miscellaneous settings
ALL_COLORS = ['lime', 'purple', 'cyan', 'red', 'yellow']  # MUST contain more colors than PLANNER_BBOX_BATCH_SIZE
USE_LOCAL_DINO_WEIGHTS = False
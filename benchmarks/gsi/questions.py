import os

GSI_OTHER_QUESTIONS = [
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '1.png'),
        'question_text': 'What is the person in the dark blue jersey number 31 on the far left most likely looking at?',
        'options': [
            'The soccer ball in mid-air near the goalpost',
            'An advertising board beside the goal',
            'A teammate running down the sideline',
            'A security staff member in a fluorescent vest'
        ],
        'ground_truth': 'The soccer ball in mid-air near the goalpost'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '1.png'),
        'question_text': 'What is the player in the red and black jersey number 12 most likely focused on?',
        'options': [
            'The ball descending toward the penalty area',
            'The goalkeeper\'s position',
            'The movement of an opponent behind him',
            'An advertising board beside the goal'
        ],
        'ground_truth': 'The ball descending toward the penalty area'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '2.png'),
        'question_text': 'What is the man in the center wearing a black shirt and brown pants most likely looking at?',
        'options': [
            'The building model in front of him',
            'The brochure behind of him',
            'The ceiling lights above',
            'The person taking the photo'
        ],
        'ground_truth': 'The building model in front of him'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '2.png'),
        'question_text': 'What is the woman to the left of the man wearing black shirt and with arms crossed most likely doing?',
        'options': [
            'Explaining details about the building model to the man',
	        'Explaining details about the documents the man his holding',
	        'Reading from a document',
	        'Preparing to turn around and leave the building'
        ],
        'ground_truth': 'Explaining details about the building model to the man'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '2.png'),
        'question_text': 'What is the woman in a long dress carrying a bag on the far right most likely doing?',
        'options': [
            'Listening carefully as another woman explains something about the building models.',
            'Talking directly to the men seen on the left of her.',
            'Looking for some documents in her bag.',
            'Looking at the separate interaction on the center left of the image.'
        ],
        'ground_truth': 'Listening carefully as another woman explains something about the building models.'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '2.png'),
        'question_text': 'What is the woman in grey clothes with her arms crossed most likely to do next?',
        'options': [
            'Borrow a pen from the woman seen on her left',
            'Ask the woman seen on the left of her questions about the buildings shown in the sandbox',
            'Ask the man seen on the right of her questions about the buildings shown in the sandbox',
            'Turn around and leave the building'
        ],
        'ground_truth': 'Ask the woman seen on the left of her questions about the buildings shown in the sandbox'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '2.png'),
        'question_text': 'What is the man in a white shirt and black tie most likely focused on?',
        'options': [
            'Listening to the woman seen on the left of him',
            'Reading a message on his phone',
            'Looking at the posters behind him',
            'Adjusting his tie'
        ],
        'ground_truth': 'Listening to the woman seen on the left of him'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '2.png'),
        'question_text': 'What is the woman on the far left most likely going to do next?',
        'options': [
            'Listening to the woman seen on the right of her',
            'Walking closer to the sandbox and observe the building models',
            'Leaving the scene and potentially leaving the building',
            'Take some documents from the man in a black shirt with arms crossed.'
        ],
        'ground_truth': 'Leaving the scene and potentially leaving the building'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '3.png'),
        'question_text': 'What is the player in white (center) most likely thinking about as he looks up at the ball?',
        'options': [
            'How to head the ball toward the goal',
            'Whether to pass to his teammate on the right',
            'How to avoid the defending players',
            'When the referee will blow the whistle'
        ],
        'ground_truth': 'How to head the ball toward the goal'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '3.png'),
        'question_text': 'What is the player in yellow/green (#9) most likely focused on?',
        'options': [
            'Intercepting the ball before the white player',
            'Running back to defend his goal',
            'Calling for a substitution',
            'Arguing with the referee'
        ],
        'ground_truth': 'Intercepting the ball before the white player'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '3.png'),
        'question_text': 'What is the white player in the background most likely thinking about?',
        'options': [
            'Positioning himself for a potential rebound or second ball',
            'What to have for dinner tonight',
            'The crowd noise in the stadium',
            'His upcoming vacation plans'
        ],
        'ground_truth': 'Positioning himself for a potential rebound or second ball'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '4.png'),
        'question_text': 'What is the Caucasian man in the dark suit (right) doing?',
        'options': [
            'Taking part in a robot demo',
            'Talking to the men wearing red badges',
            'Looking for an exit from the exhibition hall',
            'Trying to fix the wrong placement of objects on the demo table'
        ],
        'ground_truth': 'Taking part in a robot demo'
    },
    { 
	    'image_path': os.path.join('benchmarks', 'gsi', 'other', '4.png'),    
	    'question_text': 'What is the woman in the background (center) most likely thinking about?',
	     'options': [ 
		     'Whether this robotics company would be a good investment opportunity',
		     'Where the exit is', 
		     'Whether the demos in the background of the image is more interesting', 
		     'Which angle is the best for filming the demo in front of her' 
	     ], 
	     'ground_truth': 'Whether this robotics company would be a good investment opportunity' 
	},    
	{
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '4.png'),
        'question_text': 'Where is the lady in brown dress holding the mobile device (right background) focusing her attention?',
        'options': [
            'Through her device screen at the robot demonstration',
            'At the exhibition signage above',
            'At people walking in the corridor',
            'At their device settings menu'
        ],
        'ground_truth': 'Through her device screen at the robot demonstration'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '4.png'),
        'question_text': 'Which way is the man in the light shirt (center-right) looking at?',
        'options': [
            'Facing toward the robot and the demonstration area',
            'Looking toward the exhibition exit',
            'Facing away from the demonstration',
            'Looking up at the ceiling displays'
        ],
        'ground_truth': 'Facing toward the robot and the demonstration area'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '5.png'),
        'question_text': 'Which direction is the man in the red cap looking?',
        'options': [
            'At the tour guide explaining the exhibit',
            'At his mobile phone',
            'At the museum shop',
            'At other visitors behind him'
        ],
        'ground_truth': 'At the tour guide explaining the exhibit'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '5.png'),
        'question_text': 'Where is the elderly man with glasses (left side) directing his attention?',
        'options': [
            'Toward the tour guide and the exhibit being explained',
            'At the museum brochure in his hand',
            'At the windows behind the group',
            'At his watch to check the time'
        ],
        'ground_truth': 'Toward the tour guide and the exhibit being explained'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '6.png'),
        'question_text': 'Where is the woman wearing a dark blue shirt and a necklace standing in the foreground looking?',
        'options': [
            'Down at the patient receiving treatment',
            'At the medical supplies on the table',
            'At other volunteers in the background',
            'At the event banners overhead'
        ],
        'ground_truth': 'Down at the patient receiving treatment'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '6.png'),
        'question_text': 'What is the healthcare worker wearing purple (in the foreground) doing?',
        'options': [
            'Focusing on providing treatment for the patient only',
            'Explaining the treatment to the woman standing',
            'Examining the medical equipment in her hand',
            'Picking up the equipment on the side of her left hand'
        ],
        'ground_truth': 'Focusing on providing treatment for the patient only'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '6.png'),
        'question_text': 'Where is the patient lying on the treatment bed (foreground) directing her gaze?',
        'options': [
            'Up at the woman in the dark blue shirt (standing) talking to her',
            'At the tent ceiling above',
            'At the other patients nearby',
            'At nothing in particular'
        ],
        'ground_truth': 'At nothing in particular'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '7.png'),
        'question_text': 'Where is the player in the yellow bib (leftmost person) looking?',
        'options': [
            'At the ball carrier in front of her',
            'At the second leftmost person in the image',
            'At the goal posts behind',
            'At her teammate on the right'
        ],
        'ground_truth': 'At the second leftmost person in the image'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '7.png'),
        'question_text': 'Which direction is the ball carrier (center) directing her gaze?',
        'options': [
            'At the player on her left who is defending',
            'Toward the sideline',
            'Back toward her teammates',
            'Up at the sky'
        ],
        'ground_truth': 'At the player on her left who is defending'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '8.png'),
        'question_text': 'Where is the model in the white traditional dress looking?',
        'options': [
            'Directly at the audience/camera',
            'At the judges sitting to her left',
            'At other models in the background',
            'At the ceiling decorations'
        ],
        'ground_truth': 'Directly at the audience/camera'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '8.png'),
        'question_text': 'Which direction is the woman in dark clothing (seated left) facing?',
        'options': [
            'Toward the model presenting the outfit',
            'At her notes or evaluation sheet',
            'At the exit door',
            'At other judges beside her'
        ],
        'ground_truth': 'Toward the model presenting the outfit'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '9.png'),
        'question_text': 'Where is the woman in black (center-right) doing?',
        'options': [
            'Posing for a photo',
            'Looking at the movie posters',
            'Looking casually at passers by',
            'Looking for a napkin in her handbag'
        ],
        'ground_truth': 'Posing for a photo'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '9.png'),
        'question_text': 'Where is the person in the light brown hat (left) looking?',
        'options': [
            'At the movie posters',
            'At their own phone',
            'At the phone of someone else',
            'At the street traffic'
        ],
        'ground_truth': 'At the phone of someone else'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '10.png'),
        'question_text': 'Where is the street performer in white looking?',
        'options': [
            'Up at the liquid he is juggling in the air',
            'At the audience watching him',
            'At the shops beside him',
            'At the money collection container'
        ],
        'ground_truth': 'Up at the liquid he is juggling in the air'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '25.jpg'),
        'question_text': 'Who is the woman on the left directly addressing?',
        'options': ['The man with white hair wearing a striped red tie', 'The man with blonde hair wearing a deep blue tie', 'The man with grey hair wearing a orange tie', 'The man with brown hair wearing a black tie on the right'],
        'ground_truth': 'The man with blonde hair wearing a deep blue tie'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '25.jpg'),
        'question_text': 'In this conversation, who is the man wearing a striped red tie most likely paying attention to?',
        'options': ['The woman sitting on the left', 'The man with blonde hair wearing a deep blue tie', 'The man with grey hair wearing a orange tie', 'The man with brown hair wearing a black tie on the right'],
        'ground_truth': 'The woman sitting on the left'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '26.jpg'),
        'question_text': 'Who is the man in black seated in the left looking at?',
        'options': ['The man with blonde hair and wearing a navy suit and a red tie in the middle', 'The man with dark hair wearing a navy suit and a deep red tie on the right', 'He is looking at the viewer (camera)', 'He is not looking at anyone in particular, focusing on some non-human objects instead'],
        'ground_truth': 'The man with dark hair wearing a navy suit and a deep red tie on the right'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '27.jpg'),
        'question_text': 'Who is the woman in the middle looking at?',
        'options': ['The man with pale blonde hear wearing a blue tie, speaking at the podium', 'The man with dark hair in the right', 'She is looking at the viewer (camera)', 'She is not looking at anyone in particular, focusing on some non-human objects instead'],
        'ground_truth': 'The man with pale blonde hear wearing a blue tie, speaking at the podium'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '28.jpg'),
        'question_text': 'Who is the man on the left with dark skin and wearing a dark tie with spots looking at?',
        'options': ['The man on the left with dark hair wearing a red tie', 'The man with his arms crossed, sporting pale blonde hair and wearing a navy suit', 'The bald man on the right with dark skin, wearing a navy suit and an orange tie'],
        'ground_truth': 'The bald man on the right with dark skin, wearing a navy suit and an orange tie'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '28.jpg'),
        'question_text': 'Who is the man in the middle with his arms crossed paying attention to?',
        'options': ['The man on the left with dark hair wearing a red tie', 'the man on the left with dark skin and wearing a dark tie with spots', 'The bald man on the right with dark skin, wearing a navy suit and an orange tie'],
        'ground_truth': 'The bald man on the right with dark skin, wearing a navy suit and an orange tie'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '29.jpg'),
        'question_text': 'Which of the following options most accurately describes the interaction between the white-haired man (A), and the man in the middle wearing a blue tie and standing behind the podium (B) in the image?',
        'options': ['B is speaking to the audience, with A listening to him', 'A is talking to B, who is in turn listening to A', 'B is listening to the woman with brown hair on the right, while A is not engaged in the conversation', 'Both A and B are looking at the viewer (camera) for a group photo.'],
        'ground_truth': 'A is talking to B, who is in turn listening to A'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '30.jpg'),
        'question_text': 'Which of the following is the most accurate description of the social dynamics of the 4 individuals in the image?',
        'options': ['They are all listening to a speaker not shown in the image', 'All 4 are engaged in the same discussion', 'The two wearing black clothes on the left are in discussion, while the two wearing blue clothes on the right are in another discussion', 'The two wearing black clothes on the left are passing a document, while the two wearing blue clothes on the right are discussing.'],
        'ground_truth': 'The two wearing black clothes on the left are passing a document, while the two wearing blue clothes on the right are discussing.'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '31.jpg'),
        'question_text': 'Which of the following diplomats is the center of attention in this image?',
        'options': ['The lady with short hair and wearing a grey suit on the left, representing Sweden.', 'The man wearing a black suit and a dark blue tie, representing the United Kingdom.', 'The lady with long dark hair and wearing grey clothes, representing the United States.', 'The lady wearing red clothes at the bottom right, filling the role of the General Secretary.'],
        'ground_truth': 'The lady with long dark hair and wearing grey clothes, representing the United States.'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '31.jpg'),
        'question_text': 'Which of the following diplomats is most likely to be absent-minded?',
        'options': ['The lady with short hair and wearing a grey suit on the left, representing Sweden.', 'The man wearing a black suit and a dark blue tie, representing the United Kingdom.', 'The lady with long dark hair and wearing grey clothes, representing the United States.', 'The man wearing a black suit and a red tie, representing the Russian Federation'],
        'ground_truth': 'The man wearing a black suit and a red tie, representing the Russian Federation.'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '32.jpg'),
        'question_text': 'Which of the following is the most accurate description of the social interaction between the four persons in the foreground?',
        'options': ['All four are engaged in a shared discussion', 'The two in front (woman wearing a white suit and the man seated and wearing a black suit) are talking to each other, while the other two (the man standing and wearing a black suit and the woman wearing a checkered coat) are in a separate interaction.', 'They are all listening to a speaker not depicted in the image.', 'The woman wearing a white suit is talking to the man wearing glass standing to her right, while the man seated in the front is talking to the woman wearing a checkered coat.'],
        'ground_truth': 'The two in front (woman wearing a white suit and the man seated and wearing a black suit) are talking to each other, while the other two (the man standing and wearing a black suit and the woman wearing a checkered coat) are in a separate interaction.'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '33.jpg'),
        'question_text': 'Which of the panelist is the center of attention?',
        'options': ['The woman wearing green clothes on the left', 'the man with dark skin directly to the right of the woman wearing green clothes', 'The woman sitting in the middle with blond hair.', 'The man on the center-right wearing a red tie.', 'The woman seated on the right.'],
        'ground_truth': 'The man on the center-right wearing a red tie.'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '33.jpg'),
        'question_text': 'Who is most likely in the process of receiving a breaking news alert from someone outside the studio?',
        'options': ['The woman wearing green clothes on the left', 'the man with dark skin directly to the right of the woman wearing green clothes', 'The woman sitting in the middle with blond hair.', 'The man on the center-right wearing a red tie.', 'The woman seated on the right.'],
        'ground_truth': 'The woman wearing green clothes on the left'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '34.jpg'),
        'question_text': 'Which of the panelists is most likely to be absent minded at the moment?',
        'options': ['The man sitting on the far left', 'the woman with blond hair', 'The man in the middle wearing a yellow time.', 'The man on the center-right wearing a red tie.', 'The man seated on the far right.'],
        'ground_truth': 'The man on the center-right wearing a red tie.'
    },
	{
	   'image_path': os.path.join('benchmarks', 'gsi', 'other', '41.png'),
	   'question_text': 'What is the woman in blue jacket and red hoodie in the middle of the photo most likely looking at?',
	   'options': [
	       'The green packaged chips in her hand',
	       'The children seated around the table',
	       'The various snack packages scattered on the table',
	       'The colorful decorative streamers in the background'
	   ],
	   'ground_truth': 'The green packaged chips in her hand'
	},
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '41.png'),
        'question_text': 'What is the child in dark jacket with red polka-dot collar looking at?',
        'options': [
            'At the snacks on the table',
            'At the woman handling a bag of chip',
            'At the children sitting across from them',
            'At the activities happening on the red carpeted stage'
        ],
        'ground_truth': 'At the snacks on the table'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '42.png'),
        'question_text': 'Where is the man in striped shirt with glasses focused on?',
        'options': [
            'At the mixing bowl in his hand',
            'At the young man in black t-shirt learning beside him',
            'At the woman',
            'At the tools and materials in the workspace'
        ],
        'ground_truth': 'At the mixing bowl in his hand'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '42.png'),
        'question_text': 'What is the young man in black t-shirt with "CK" logo and grey pants focusing on?',
        'options': [
            'The soy mill he is currently operating',
            'Talking to the woman seen on the right of him',
            'The stuff in the mixing bowl held by the other man',
            'Elsewhere in the environment'
        ],
        'ground_truth': 'The soy mill he is currently operating'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '42.png'),
        'question_text': 'Where is the woman in white sleeveless top with gray skirt directing her attention?',
        'options': [
            'Down at her own soy mill',
            'At the man using his own soy mill',
            'At the camera taking this image',
            'At someone outside the image, possibly an instructor or guide'
        ],
        'ground_truth': 'Down at her own soy mill'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '42.png'),
        'question_text': 'Where is the collective attention focused in this scene?',
        'options': [
            'On the hands-on process of making soy products',
            'On the tools displayed around',
            'At the person taking this photo',
            'On the social interaction between participants'
        ],
        'ground_truth': 'On the hands-on process of making soy products'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '43.png'),
        'question_text': 'Where is the woman in grey sleeveless top with white pants and white slippers directing her gaze?',
        'options': [
            'Down at the dishes she in her hand',
            'At the bamboo steamers with dumplings on the counter',
            'At her companions cooking around the kitchen',
            'Out the window overlooking the garden'
        ],
        'ground_truth': 'At the bamboo steamers with dumplings on the counter'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '43.png'),
        'question_text': 'Where is the woman in light blue sleeveless dress standing near the stove directing her attention?',
        'options': [
            'At the cooking activity happening on the right of the image',
            'At the counter on the left of the image just below the window',
            'At the potted plant near the window',
            'At the someone or something outside the window'
        ],
        'ground_truth': 'At the someone or something outside the window'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '43.png'),
        'question_text': 'What is the woman in white t-shirt (right side) looking at?',
        'options': [
            'Down at the food preparation she is working on',
            'At the dish in her hand',
            'At the woman next to her',
            'At the stove and sink'
        ],
        'ground_truth': 'Down at the food preparation she is working on'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '43.png'),
        'question_text': 'Where is the collective attention focused among all the women in this traditional kitchen scene?',
        'options': [
            'On their individual cooking and food preparation tasks',
            'On the communal meal being prepared together',
            'On the traditional cooking utensils',
            'On the conversation and social interaction'
        ],
        'ground_truth': 'On their individual cooking and food preparation tasks'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '43.png'),
        'question_text': 'What is the woman wearing a grey t-shirt and dark grey trousers doing?',
        'options': [
            'Tasting some freshly made food',
            'Examining the stove to make sure it\'s safe before lighting a fire',
            'Talking to the woman with a ponytail wearing light blue clothes',
            'Watching the women standing on the right try some freshly made food'
        ],
        'ground_truth': 'Tasting some freshly made food'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '44.png'),
        'question_text': 'Where is the man in yellow t-shirt holding a microphone doing?',
        'options': [
            'Lighting a fire and burning materials in the metal container',
            'Addressing the crowd of protesters around him',
            'Passing the microphone to another protest leader next to him',
            'Talking to another protest leader next to him'
        ],
        'ground_truth': 'Addressing the crowd of protesters around him'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '44.png'),
        'question_text': 'What is the man in light blue checkered shirt with dark pants focusing on?',
        'options': [
            'The stuff burning in the metal container',
            'The speaker with the microphone addressing the crowd',
            'The protest banners with WWII Japanese rising sun imagery',
            'The camera taking this photo'
        ],
        'ground_truth': 'The stuff burning in the metal container'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '44.png'),
        'question_text': 'Where is the man in yellow shirt with floral pattern (background center) directing his attention?',
        'options': [
            'At the burning of stuff',
            'At the protesters holding signs and banners',
            'At the media or photographers documenting the event',
            'At the main speaker addressing the gathering'
        ],
        'ground_truth': 'At the burning of stuff'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '44.png'),
        'question_text': 'What is the man in white t-shirt (left side) looking at?',
        'options': [
            'The burning of materials',
            'The banners with historical references being displayed',
            'The other participants in the gathering',
            'The speaker holding the microphone'
        ],
        'ground_truth': 'The burning of materials'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '44.png'),
        'question_text': 'Where is the collective visual focus of all clearly visible participants in this gathering?',
        'options': [
            'On the central burning demonstration',
            'On the protest banners and their messages',
            'On the speaker addressing the crowd',
            'On the urban setting and surroundings'
        ],
        'ground_truth': 'On the central burning demonstration'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '45.png'),
        'question_text': 'Where is the player in red jersey with "Snapdragon" sponsor and white shorts (left side) directing his gaze?',
        'options': [
            'At the football on the ground near the goal line',
            'At the goalkeeper in black jersey making a save',
            'At his teammate in similar red jersey behind the net',
            'At the opposing players in white jerseys in the box'
        ],
        'ground_truth': 'At the football on the ground near the goal line'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '45.png'),
        'question_text': 'What is the goalkeeper in black jersey with yellow accents and black shorts focusing on?',
        'options': [
            'The ball\'s position after the save attempt',
            'The player in red approaching',
            'His defensive teammates\' positioning',
            'The referee\'s potential decision'
        ],
        'ground_truth': 'The ball\'s position after the save attempt'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '45.png'),
        'question_text': 'Where is the defender in white jersey with dark trim and white shorts (center) directing his attention?',
        'options': [
            'At the loose ball in the penalty area scramble',
            'At the attacker in red',
            'At his goalkeeper for coordination',
            'At the crowded goal mouth situation'
        ],
        'ground_truth': 'At the loose ball in the penalty area scramble'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '45.png'),
        'question_text': 'What is the player in red jersey #4 with white shorts (visible through the net) looking at?',
        'options': [
            'The ball',
            'His teammates positioning for defense',
            'The match officials for potential calls',
            'The Manchester United players in red jerseys'
        ],
        'ground_truth': 'The ball'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '45.png'),
        'question_text': 'Where is the collective visual focus of all clearly visible players in this penalty box chaos?',
        'options': [
            'On the loose football and potential goal-scoring opportunity',
            'On the goalkeeper\'s positioning and reactions',
            'On the referee\'s decisions in the penalty area',
            'On their individual marking responsibilities'
        ],
        'ground_truth': 'On the loose football and potential goal-scoring opportunity'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '46.png'),
        'question_text': 'Where is the player in red "CHINA" jersey #21 with yellow shorts reaching for the rebound directing his gaze?',
        'options': [
            'Up at the basketball he is attempting to secure',
            'At the Australian defender #10 competing for position',
            'At the basket rim above for positioning',
            'At his Chinese teammate in similar red jersey on the left'
        ],
        'ground_truth': 'Up at the basketball he is attempting to secure'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '46.png'),
        'question_text': 'What is the player in yellow "AUSTRALIA" jersey #10 with green trim and yellow shorts focusing on?',
        'options': [
            'The basketball being contested in the air',
            'The Chinese player #21 he is battling against',
            'His Australian teammate #6 for positioning help',
            'The referee\'s positioning for potential fouls'
        ],
        'ground_truth': 'The basketball being contested in the air'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '46.png'),
        'question_text': 'Where is the player in yellow "AUSTRALIA" jersey #6 with green trim and yellow shorts directing his attention?',
        'options': [
            'At the rebounding battle happening above him',
            'At his defensive assignment and positioning',
            'At the game clock and score situation'
            'At something else',
        ],
        'ground_truth': 'At something else'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '46.png'),
        'question_text': 'What is the Chinese player in red jersey with yellow shorts (left side, partially visible) looking at?',
        'options': [
            'The Australian player next to him',
            'His teammate #21 handling the ball',
            'The Australian defenders around the basket',
            'The ball\'s trajectory from the previous shot'
        ],
        'ground_truth': 'His teammate #21 handling the ball'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '46.png'),
        'question_text': 'Where is the collective visual focus of all clearly visible players in this international basketball scene?',
        'options': [
            'On the contested rebound and possession of the basketball',
            'On the referee\'s calls and game management',
            'On their respective team strategies and plays',
            'On the crowd reactions in the arena'
        ],
        'ground_truth': 'On the contested rebound and possession of the basketball'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '47.png'),
        'question_text': 'Where is the player in red jersey with yellow and black trim carrying the ball directing her gaze?',
        'options': [
            'At the gap between defenders #12 and #4 she is targeting',
            'At the defender in white #12 approaching from the left',
            'At her teammates behind for potential support',
            'At the try line ahead of the defensive line'
        ],
        'ground_truth': 'At the gap between defenders #12 and #4 she is targeting'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '47.png'),
        'question_text': 'Where is the player in white jersey #4 with red trim and white shorts directing her attention?',
        'options': [
            'At the attacking player in red jersey with the ball',
            'At her teammate #12 coordinating the defense',
            'At the referee\'s positioning on the field',
            'At potential support runners behind the ball carrier'
        ],
        'ground_truth': 'At the attacking player in red jersey with the ball'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '47.png'),
        'question_text': 'What is the player in white "CANADA" jersey (background center-left) looking at?',
        'options': [
            'The developing attacking play with the ball carrier',
            'Her defensive teammates\' alignment',
            'The coaching staff on the sideline',
            'The scoreboard or match officials'
        ],
        'ground_truth': 'The developing attacking play with the ball carrier'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '47.png'),
        'question_text': 'Where is the collective visual focus of all clearly visible players in this rugby action?',
        'options': [
            'On the ball carrier and the critical tackle situation',
            'On the field markings and positioning',
            'On the match officials and their decisions',
            'On the crowd reactions in the stadium'
        ],
        'ground_truth': 'On the ball carrier and the critical tackle situation'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '48.png'),
        'question_text': 'Where is the player in red and white striped jersey with white shorts preparing to kick directing his gaze?',
        'options': [
            'At the football he is about to strike',
            'At the goalkeeper in green diving towards the goal',
            'At his teammate in yellow jersey #6 approaching',
            'At the goal net behind the defending players'
        ],
        'ground_truth': 'At the football he is about to strike'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '48.png'),
        'question_text': 'Where is the player in yellow jersey with "UNITED" sponsor (background left) directing his attention?',
        'options': [
            'At the developing goal-scoring opportunity',
            'At the referee\'s positioning for potential calls',
            'At his teammate #29',
            'At the crowded stadium stands'
        ],
        'ground_truth': 'At the developing goal-scoring opportunity'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '48.png'),
        'question_text': 'Where is the collective visual focus of all clearly visible players in this penalty area scene?',
        'options': [
            'On the crucial shooting moment and goal-bound opportunity',
            'On the referee\'s decision-making in the penalty box',
            'On the stadium crowd\'s reactions to the play',
            'On their individual tactical responsibilities'
        ],
        'ground_truth': 'On the crucial shooting moment and goal-bound opportunity'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '49.png'),
        'question_text': 'Where is the player in turquoise blue jersey with white number jumping for the shot directing his gaze?',
        'options': [
            'Up at the hoop he is targeting for the dunk',
            'At the defender in orange vest trying to block him',
            'At his teammate in blue jersey #18 on the left',
            'At the crowd gathered around the outdoor court'
        ],
        'ground_truth': 'Up at the hoop he is targeting for the dunk'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '49.png'),
        'question_text': 'What is the player in blue jersey #18 with white shorts and white sneakers focusing on?',
        'options': [
            'The dunk happening at the basket',
            'His own positioning for a potential rebound',
            'The referee or game official',
            'The spectators cheering from the sidelines'
        ],
        'ground_truth': 'The dunk happening at the basket'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '49.png'),
        'question_text': 'What is the player in orange vest with black shorts (right side) looking at?',
        'options': [
            'The dramatic scoring attempt near the rim',
            'The game clock or scoreboard',
            'His teammate in similar orange vest',
            'The outdoor lighting setup'
        ],
        'ground_truth': 'The dramatic scoring attempt near the rim'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '49.png'),
        'question_text': 'Where is the collective visual focus of all clearly visible players in this street basketball scene?',
        'options': [
            'On the high-flying dunk attempt and rim action',
            'On the outdoor court surface conditions',
            'On the surrounding spectators and atmosphere',
            'On individual defensive assignments'
        ],
        'ground_truth': 'On the high-flying dunk attempt and rim action'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '50.png'),
        'question_text': 'Where is the goalkeeper in white long-sleeved jersey and white shorts directing his gaze while diving?',
        'options': [
            'At the football he is attempting to save',
            'At the attacking player in red and white striped jersey',
            'At his defensive teammates behind him',
            'At the goal crossbar above'
        ],
        'ground_truth': 'At the football he is attempting to save'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '50.png'),
        'question_text': 'What is the player in red, black, and white striped jersey with white shorts focusing on?',
        'options': [
            'Following the trajectory of the ball toward the goal',
            'Watching the goalkeeper\'s diving movement',
            'Looking at teammates for a potential rebound',
            'Observing the referee\'s positioning'
        ],
        'ground_truth': 'Following the trajectory of the ball toward the goal'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '50.png'),
        'question_text': 'Where is the player in solid red jersey with white shorts directing his attention?',
        'options': [
            'At the developing goal scramble',
            'At his teammate in striped jersey',
            'At the crowd reactions in the stands',
            'At the linesman on the sideline'
        ],
        'ground_truth': 'At the developing goal scramble'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '50.png'),
        'question_text': 'What is the player in yellow jersey with dark shorts (visible in background) looking at?',
        'options': [
            'The critical save attempt near the goal line',
            'His defensive positioning responsibilities',
            'The match official\'s signals',
            'The tactical setup of the opposing team'
        ],
        'ground_truth': 'The critical save attempt near the goal line'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '50.png'),
        'question_text': 'Where is the collective visual focus of all clearly visible players in this penalty box scene?',
        'options': [
            'On the dramatic goalkeeper dive and ball trajectory',
            'On potential offside positioning',
            'On the referee\'s upcoming decision',
            'On their respective team formations'
        ],
        'ground_truth': 'On the dramatic goalkeeper dive and ball trajectory'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '51.png'),
        'question_text': 'Where is the Lakers player in yellow jersey #24 looking while going up for the shot?',
        'options': [
            'Up at the basketball rim he is targeting',
            'At the Memphis defender #22 beside him',
            'At the crowd in the arena stands',
            'At his teammates positioning for a rebound'
        ],
        'ground_truth': 'Up at the basketball rim he is targeting'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '51.png'),
        'question_text': 'Where is the Memphis player in dark blue jersey (background left) directing his gaze?',
        'options': [
            'At the shooting action happening near the basket',
            'At the coaching staff on the sideline',
            'At the game clock display',
            'At his defensive assignment on the perimeter'
        ],
        'ground_truth': 'At the shooting action happening near the basket'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '51.png'),
        'question_text': 'What direction are the spectators in the arena stands looking?',
        'options': [
            'At the Lakers player making the athletic play',
            'At the jumbotron replay screens',
            'At the halftime entertainment',
            'At their mobile phones and cameras'
        ],
        'ground_truth': 'At the Lakers player making the athletic play'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '51.png'),
        'question_text': 'Where is the focus of most people visible in this arena scene?',
        'options': [
            'On the dramatic scoring attempt by the Lakers player',
            'On the referee\'s positioning and potential calls',
            'On the team benches and coaching strategies',
            'On the arena\'s advertising displays and sponsors'
        ],
        'ground_truth': 'On the dramatic scoring attempt by the Lakers player'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '52.png'),
        'question_text': 'Where is the Lakers player in yellow jersey looking while dunking?',
        'options': [
            'At the basketball hoop he is attacking',
            'At the defender in red trying to block him',
            'At his teammates on the court',
            'At the crowd in the stands'
        ],
        'ground_truth': 'At the basketball hoop he is attacking'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '52.png'),
        'question_text': 'Which direction is the defender in red jersey facing?',
        'options': [
            'Up at the Lakers player attempting the dunk',
            'At the basketball in the air',
            'At the referee making a call',
            'At his own teammates for help'
        ],
        'ground_truth': 'Up at the Lakers player attempting the dunk'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '52.png'),
        'question_text': 'Where is the player in white/light colored jersey (background left) directing his gaze?',
        'options': [
            'At the dunking action happening near the basket',
            'At the scoreboard above the court',
            'At the coach on the sideline',
            'At the ball boy retrieving equipment'
        ],
        'ground_truth': 'At the dunking action happening near the basket'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '52.png'),
        'question_text': 'What direction is the player in green jersey (background right) looking?',
        'options': [
            'Toward the dramatic dunk attempt at the rim',
            'At his position on the court floor',
            'At the game clock',
            'At the opposing team\'s bench'
        ],
        'ground_truth': 'Toward the dramatic dunk attempt at the rim'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '52.png'),
        'question_text': 'Where are most of the players on the court focusing their attention?',
        'options': [
            'On the high-flying dunk happening at the basket',
            'On their individual defensive assignments',
            'On the referee\'s positioning',
            'On the coaching staff instructions'
        ],
        'ground_truth': 'On the high-flying dunk happening at the basket'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '52.png'),
        'question_text': 'Which way is the player in dark colored jersey (background) oriented?',
        'options': [
            'Facing the spectacular play developing at the hoop',
            'Looking toward the team benches',
            'Watching the out-of-bounds area',
            'Observing the crowd reaction'
        ],
        'ground_truth': 'Facing the spectacular play developing at the hoop'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '53.png'),
        'question_text': 'What is the dancer in the front doing a freeze on one hand most likely focusing on?',
        'options': [
            'Maintaining his balance',
            'Looking at the building behind him',
            'Watching the person in a red cap',
            'Checking his watch'
        ],
        'ground_truth': 'Maintaining his balance'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '53.png'),
        'question_text': 'What is the man in the white T-shirt on the right with his mouth open most likely looking at?',
        'options': [
            'The dancer performing the freeze',
            'A car on the street',
            'The roof of the building',
            'His own shoes'
        ],
        'ground_truth': 'The dancer performing the freeze'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '53.png'),
        'question_text': 'What is the man in the red cap and gray tracksuit most likely focusing on?',
        'options': [
            'The dancer doing the freeze',
            'The sky and clouds',
            'His phone in his pocket',
            'Another dancer behind him'
        ],
        'ground_truth': 'The dancer doing the freeze'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '53.png'),
        'question_text': 'What is the man in sunglasses with a patterned shirt in the middle most likely looking at?',
        'options': [
            'The breakdancer in front',
            'The photographer',
            'A plane in the sky',
            'The person in a blue jacket'
        ],
        'ground_truth': 'The breakdancer in front'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '53.png'),
        'question_text': 'What is the man in the blue jacket crouching on the right most likely looking at?',
        'options': [
            'The dancer’s move on the ground',
            'The building sign',
            'His shoelaces',
            'The person in the red cap'
        ],
        'ground_truth': 'The dancer’s move on the ground'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '53.png'),
        'question_text': 'What is the man with dreadlocks and white T-shirt on the left most likely focusing on?',
        'options': [
            'The dancer doing the freeze',
            'The concrete floor',
            'The trees in the background',
            'A phone in his hand'
        ],
        'ground_truth': 'The dancer doing the freeze'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '54.png'),
        'question_text': 'What is the woman in the center wearing a white and yellow jacket most likely looking at?',
        'options': [
            'The man in a green jacket crouching on the right side',
            'Looking at the floor tiles',
            'Watching the window',
            'Checking her phone'
        ],
        'ground_truth': 'The man in a green jacket crouching on the right side'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '54.png'),
        'question_text': 'What is the woman on the left in a black shirt with orange Nike logo pants most likely focusing on?',
        'options': [
            'The dancer in the center',
            'The person standing behind her',
            'The ceiling lights',
            'A bag on the floor'
        ],
        'ground_truth': 'The dancer in the center'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '54.png'),
        'question_text': 'What is the woman in the back wearing a striped brown sweater most likely looking at?',
        'options': [
            'The center dancer',
            'A notebook in her hand',
            'The window frame',
            'The person in the green jacket'
        ],
        'ground_truth': 'The center dancer'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '54.png'),
        'question_text': 'What is the woman with a beige beanie behind the dancer most likely focusing on?',
        'options': [
            'The center dancer',
            'Adjusting her hat',
            'The concrete wall',
            'A bottle of water'
        ],
        'ground_truth': 'The center dancer'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '55.png'),
        'question_text': 'What is the woman on the far left in a white top most likely looking at?',
        'options': [
            'The dancer on the ground',
            'The brick wall behind her',
            'A person walking in the distance',
            'Her bracelet on her wrist'
        ],
        'ground_truth': 'The dancer on the ground'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '55.png'),
        'question_text': 'What is the woman in blue denim with blonde hair most likely focused on?',
        'options': [
            'The dancer’s raised leg',
            'Reading something on her phone',
            'Fixing her jacket zipper',
            'Looking at the camera directly'
        ],
        'ground_truth': 'The dancer’s raised leg'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '55.png'),
        'question_text': 'What is the woman in a black top with red side-striped pants most likely looking at?',
        'options': [
            'The dancer on the ground',
            'The shoes she is wearing',
            'A bird flying above',
            'The bricks on the wall'
        ],
        'ground_truth': 'The dancer on the ground'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'other', '55.png'),
        'question_text': 'What is the woman on the far right with pink braids most likely focused on?',
        'options': [
            'The dancer’s raised leg',
            'Her phone in her hand',
            'The hairstyle of the woman next to her',
            'A window on the brick wall'
        ],
        'ground_truth': 'The dancer’s raised leg'
    },
    {
        "image_path": os.path.join("benchmarks", "gsi", "other", "11.jpg"),
        "question_text": "What is the woman probably doing?",
        "options": ["Listening to the man in dark suit jacket over a white collared shirt", "Looking at the charts on the board", "Talking to the man in black shirt", "Ignoring everyone"],
        "ground_truth": "Listening to the man in dark suit jacket over a white collared shirt"
    },
    {
        "image_path": os.path.join("benchmarks", "gsi", "other", "12.jpg"),
        "question_text": "Where is the man looking at?",
        "options": ["The woman’s face", "The laptop", "Popcorn in his hand", "The woman’s hand"],
        "ground_truth": "The laptop"
    },
    {
        "image_path": os.path.join("benchmarks", "gsi", "other", "13.jpg"),
        "question_text": "Where is the man on the right looking at?",
        "options": ["The laptop", "The clipboard", "The pen in the other man’s hand", "The ceiling"],
        "ground_truth": "The clipboard"
    },
     {
        "image_path": os.path.join("benchmarks", "gsi", "other", "14.jpg"),
        "question_text": "Where is the man on the left looking at?",
        "options": ["The camera", "The man in the middle", "The man on the right", "The microphone"],
        "ground_truth": "The camera"
    },
    {
        "image_path": os.path.join("benchmarks", "gsi", "other", "14.jpg"),
        "question_text": "Considering where the man on the left is looking, the scene is most likely filming:",
        "options": ["A news report", "A movie", "A cooking show", "A street interview"],
        "ground_truth": "A news report"
    },
    {
        "image_path": os.path.join("benchmarks", "gsi", "other", "15.jpg"),
        "question_text": "Where is the woman on the left looking at?",
        "options": ["The clipboard", "The tablet on the table", "The woman on the right", "Hands of herself"],
        "ground_truth": "The clipboard"
    },
    {
        "image_path": os.path.join("benchmarks", "gsi", "other", "17.jpg"),
        "question_text": "Where is the woman in the middle looking at?",
        "options": ["The laptop", "The woman on the left", "The woman on the right", "Coffee on the table"],
        "ground_truth": "The laptop"
    },
    {
        "image_path": os.path.join("benchmarks", "gsi", "other", "17.jpg"),
        "question_text": "Where is the woman on the right looking at?",
        "options": ["The laptop", "The woman on the left", "The woman in the middle", "Coffee on the table"],
        "ground_truth": "The laptop"
    },
    {
        "image_path": os.path.join("benchmarks", "gsi", "other", "18.jpg"),
        "question_text": "Who is most likely to be speaking?",
        "options": ["The woman on the left", "The woman in the middle", "The woman on the right"],
        "ground_truth": "The woman in the middle"
    },
    {
        "image_path": os.path.join("benchmarks", "gsi", "other", "19.jpg"),
        "question_text": "Where is the man in black suit looking at?",
        "options": ["The woman on the left", "The man in white suit", "The woman on the right", "The laptop on the table"],
        "ground_truth": "The woman on the left"
    },
    {
        "image_path": os.path.join("benchmarks", "gsi", "other", "20.jpg"),
        "question_text": "Where is the woman looking at?",
        "options": ["The clipboard in the man’s hand", "The laptop on the table", "Files on the table", "Sticky note behind the laptop"],
        "ground_truth": "The laptop on the table"
    },
    {
        "image_path": os.path.join("benchmarks", "gsi", "other", "20.jpg"),
        "question_text": "What are they probably doing?",
        "options": ["Discussing about content on the clipboard", "Working individually", "Discussing about content on the laptop", "Chatting cozily"],
        "ground_truth": "Discussing about content on the laptop"
    },
    {
        "image_path": os.path.join("benchmarks", "gsi", "other", "21.jpg"),
        "question_text": "Where is the man on the left looking at?",
        "options": ["The woman in mustard yellow", "The man with glasses", "The woman in black", "Their hands"],
        "ground_truth": "The woman in black"
    },
    {
        "image_path": os.path.join("benchmarks", "gsi", "other", "21.jpg"),
        "question_text": "Where is the woman in mustard yellow looking at?",
        "options": ["The man on the left", "The woman in black", "The man with glasses", "Their hands"],
        "ground_truth": "The woman in black"
    },
    {
        "image_path": os.path.join("benchmarks", "gsi", "other", "21.jpg"),
        "question_text": "Where is the woman in black looking at?",
        "options": ["The man on the left", "The man with glasses", "The woman in mustard yellow", "Their hands"],
        "ground_truth": "Their hands"
    },
    {
        "image_path": os.path.join("benchmarks", "gsi", "other", "23.jpg"),
        "question_text": "Where is the male student on the left looking at?",
        "options": ["His own sheet", "The other student's sheet", "The Teacher", "Blackboard in the back"],
        "ground_truth": "The other student's sheet"
    },
    {
        "image_path": os.path.join("benchmarks", "gsi", "other", "23.jpg"),
        "question_text": "What will the teacher probably do next in this exam scenario?",
        "options": ["Stop the student on the left (wearing a deep blue sweater) from cheating", "Stop the student on the right (wearing a grey sweater) from cheating", "Do Nothing and walk away"],
        "ground_truth": "Stop the student on the left from cheating"
    },
        {
        "image_path": os.path.join("benchmarks", "gsi", "other", "64.jpg"),
        "question_text": "Where is the guard looking at?",
        "options": ["the thief", "the metal safe", "the flashlight", "other place in the room"],
        "ground_truth": "the thief"
    },
    {
        "image_path": os.path.join("benchmarks", "gsi", "other", "65.jpg"),
        "question_text": "Where is the woman with blonde hair on the right looking at?",
        "options": ['the man in the middle', 'the woman next to her', 'the woman with blonde hair across the table','the woman with brown hair on the left'],
        "ground_truth": "the woman with brown hair on the left"
    },
    {
        "image_path": os.path.join("benchmarks", "gsi", "other", "65.jpg"),
        "question_text": "Where is the woman with brown hair on the right looking at?",
        "options": ['the man in the middle', 'the woman next to her', 'the woman with blonde hair across the table','the woman with brown hair on the left'],
        "ground_truth": "the woman with brown hair on the left"
    },
    {
        "image_path": os.path.join("benchmarks", "gsi", "other", "66.jpg"),
        "question_text": "Where is the man looking at?",
        "options": ['his phone', 'the docent', 'the other tourist','the exhibit'],
        "ground_truth": "his phone"
    },
    
    {
        "image_path": os.path.join("benchmarks", "gsi", "other", "67.jpg"),
        "question_text": "Where is the man on the left looking at?",
        "options": ['the man in the middle', 'the contract in his hand', 'the girl next to the man in the middle','the girl on the right in blouse'],
        "ground_truth": "the girl on the right in blouse"
    },
    {
        "image_path": os.path.join("benchmarks", "gsi", "other", "68.jpg"),
        "question_text": "Where is the woman with the basketball looking at?",
        "options": ['the defender\'s foot', 'at the basketball', 'the defender\'s face','the player behind'],
        "ground_truth": "the defender\'s foot"
    },
        {
        "image_path": os.path.join("benchmarks", "gsi", "other", "69.jpg"),
        "question_text": "Where is the man in glasses looking at?",
        "options": ['the woman with curly hair', 'the woman in light-colored blouse', 'the woman in blue denim shirt','the prototype on the table'],
        "ground_truth": "the woman with curly hair"
    },
]


GSI_CHILDPLAY_QUESTIONS = [
    {
        "image_path": "benchmarks/gsi/childplay/1.png",
        "question_text": "What is the child focusing on at this moment?",
        "options": [
            "The adult on the far left of the photo",
            "The bubble machine in the adult's hands",
            "The blue raincoat",
            "The orange and black backpack"
        ],
        "ground_truth": "The bubble machine in the adult's hands"
    },
    {
        "image_path": "benchmarks/gsi/childplay/1.png",
        "question_text": "Which sentence best describes this child's state?",
        "options": [
            "Talking to the adult on the left",
            "Attracted by the bubble machine",
            "Trying to stand up from the ground",
            "Wanting to lie down on the ground"
        ],
        "ground_truth": "Attracted by the bubble machine"
    },
    {
        "image_path": "benchmarks/gsi/childplay/2.png",
        "question_text": "What is the girl in the pink long-sleeved shirt trying to do at this moment?",
        "options": [
            "Talk to the boy on the right",
            "Grab the cucumber on the table",
            "Grab the Coffee-mate bottle on the table",
            "Grab the tomato on the table"
        ],
        "ground_truth": "Grab the tomato on the table"
    },
    {
        "image_path": "benchmarks/gsi/childplay/3.png",
        "question_text": "Which sentence best describes the scene in the picture?",
        "options": [
            "The boy and girl on the left side of the image are talking.",
            "The children on the right side of the image are having a discussion.",
            "The girl on the left side of the image is explaining something to others.",
            "The children on the left and right sides of the image are debating with each other."
        ],
        "ground_truth": "The girl on the left side of the image is explaining something to others."
    },
    {
        "image_path": "benchmarks/gsi/childplay/3.png",
        "question_text": "Which child on the right side of the image appears to be distracted?",
        "options": [
            "The child in the blue and white top",
            "The child in the light gray top",
            "The child in the pink top",
            "The child in the checkered red top"
        ],
        "ground_truth": "The child in the blue and white top"
    },
    {
        "image_path": "benchmarks/gsi/childplay/4.png",
        "question_text": "What is the child focused on?",
        "options": [
            "Her shoe",
            "The single stick in her right hand",
            "The two sticks in her left hand",
            "The bottom of the container"
        ],
        "ground_truth": "The single stick in her right hand"
    },
    {
        "image_path": "benchmarks/gsi/childplay/5.png",
        "question_text": "What is the female staff member, sitting on the ground with her hair down, doing?",
        "options": [
            "Talking to another staff member.",
            "Tidying up the toys on the ground.",
            "Talking to the child on her side, who is wearing mixed-color clothing.",
            "Observing the child on her other side, who is dressed in red."
        ],
        "ground_truth": "Observing the child on her other side, who is dressed in red."
    },
    {
        "image_path": "benchmarks/gsi/childplay/6.png",
        "question_text": "What is the woman in black, sitting on the ground, doing?",
        "options": [
            "Playing with toys together with the child in pink who is also sitting on the ground.",
            "Putting the toys in her hands into a small basket.",
            "Playing with toys together with the child in red who is also sitting on the ground.",
            "Talking to the child in red who is also sitting on the ground."
        ],
        "ground_truth": "Playing with toys together with the child in pink who is also sitting on the ground."
    },
    {
        "image_path": "benchmarks/gsi/childplay/7.png",
        "question_text": "Which sentence best describes this picture?",
        "options": [
            "The woman wearing red is about to eat a banana.",
            "The woman wearing dark blue is distributing bananas to the children.",
            "The woman wearing red is teaching the children about handling bananas.",
            "The woman wearing dark blue is helping the woman in red handle bananas."
        ],
        "ground_truth": "The woman wearing red is teaching the children about handling bananas."
    },
    {
        "image_path": "benchmarks/gsi/childplay/8.png",
        "question_text": "What is the woman in the picture doing?",
        "options": [
            "Talking to the child in the blue-purple top.",
            "Talking to the child in her arms.",
            "Speaking to everyone.",
            "Talking to the child sitting on the ground, wearing a white top."
        ],
        "ground_truth": "Talking to the child in the blue-purple top."
    },
    {
        "image_path": "benchmarks/gsi/childplay/9.png",
        "question_text": "Which child in the picture is distracted?",
        "options": [
            "The child to the woman’s left, wearing white.",
            "The child in the woman’s arms.",
            "The child in the center of the group, wearing blue.",
            "The child to the woman’s right, wearing solid pink."
        ],
        "ground_truth": "The child in the woman’s arms."
    },
    {
        "image_path": "benchmarks/gsi/childplay/10.png",
        "question_text": "What is the adult, whose arm is visible in the lower left corner of the picture, doing?",
        "options": [
            "Reminding the girl to her right to pay attention.",
            "Communicating with the adult opposite her.",
            "Communicating with the child in the arms of the adult opposite her."
        ],
        "ground_truth": "Reminding the child to her right to pay attention."
    },
    {
        "image_path": "benchmarks/gsi/childplay/11.png",
        "question_text": "What is the girl in pink doing in the picture?",
        "options": [
            "Looking at the adult in a gray top.",
            "Talking to the child to her left, who is wearing a blue top.",
            "Handing out the paper in her hand.",
            "Folding the paper in her hand."
        ],
        "ground_truth": "Looking at the adult in a gray top."
    },
    {
        "image_path": "benchmarks/gsi/childplay/12.png",
        "question_text": "What are the people in the picture doing?",
        "options": [
            "The child in green is playing with one set of toys, the child in orange is playing with another set of toys, and the child in light pink, the child in black, and an adult are playing with yet another set of toys.",
            "The child in green is playing with one set of toys, while the child in orange and an adult are playing with another set of toys, and the child in light pink and the child in black are playing with another set of toys.",
            "The child in green is playing with one set of toys, while the child in orange, the child in light pink, the child in black, and an adult are playing with another set of toys.",
            "The child in green and the child in orange are playing with one set of toys, while the child in light pink, the child in black, and an adult are playing with another set of toys."
        ],
        "ground_truth": "The child in green is playing with one set of toys, the child in orange is playing with another set of toys, and the child in light pink, the child in black, and an adult are playing with yet another set of toys."
    },
    {
        "image_path": "benchmarks/gsi/childplay/13.png",
        "question_text": "What is the adult in the picture doing?",
        "options": [
            "Playing with a set of toys together with the child in orange.",
            "Playing with a set of toys together with the child in light pink and the child in black.",
            "Playing with a set of toys together with the child in green.",
            "Talking to the child in green."
        ],
        "ground_truth": "Talking to the child in green."
    },
    {
        "image_path": "benchmarks/gsi/childplay/15.png",
        "question_text": "What is the girl in pink trying to do?",
        "options": [
            "Pick up the red building block in front of her on the left with her left hand.",
            "Pick up the blue building block in front of her on the left with her left hand.",
            "Place the yellow building block in her right hand onto the block tower stacked in front of her.",
            "Place the yellow building block in her right hand onto the block tower stacked in front of the boy in black."
        ],
        "ground_truth": "Pick up the red building block in front of her on the left with her left hand."
    },
    {
        "image_path": "benchmarks/gsi/childplay/16.png",
        "question_text": "What is the girl in pink trying to do?",
        "options": [
            "Pick up the red building block in front of her on the left with her left hand.",
            "Pick up the blue building block in front of her on the left with her left hand.",
            "Place the yellow building block in her right hand onto the block tower stacked in front of her.",
            "Place the yellow building block in her right hand onto the block tower stacked in front of the boy in black."
        ],
        "ground_truth": "Place the yellow building block in her right hand onto the block tower stacked in front of her."
    },
    {
        "image_path": "benchmarks/gsi/childplay/17.png",
        "question_text": "Which sentence best describes what is happening in this picture?",
        "options": [
            "An adult is distributing toys to the children.",
            "An adult is directly helping the girl in pink to play with the toys.",
            "An adult is directly helping the girl in blue to play with the toys.",
            "An adult is playing with the children."
        ],
        "ground_truth": "An adult is directly helping the girl in pink to play with the toys."
    },
    {
        "image_path": "benchmarks/gsi/childplay/18.png",
        "question_text": "What is the adult in the picture most likely doing?",
        "options": [
            "Talking to the child wearing gray clothes with narrow white horizontal stripes.",
            "Talking to the child in pink.",
            "Handing a toy to the child in pink.",
            "Handing a toy to the child wearing gray clothes with narrow white horizontal stripes."
        ],
        "ground_truth": "Talking to the child wearing gray clothes with narrow white horizontal stripes."
    },
    {
        "image_path": "benchmarks/gsi/childplay/19.png",
        "question_text": "Which child is the adult in the picture talking to?",
        "options": [
            "The child in pink.",
            "The child in blue.",
            "The child with short hair, wearing black.",
            "The child with long hair, wearing black."
        ],
        "ground_truth": "The child in blue."
    },
    {
        "image_path": "benchmarks/gsi/childplay/20.png",
        "question_text": "Which child in the picture looks most like they are distracted?",
        "options": [
            "The girl in a white top with dark spots.",
            "The boy in a light blue and black striped top.",
            "The girl in a solid blue top.",
            "The child in a light purple top."
        ],
        "ground_truth": "The girl in a white top with dark spots."
    },
    {
        "image_path": "benchmarks/gsi/childplay/21.png",
        "question_text": "Who is everyone listening to at this moment?",
        "options": [
            "The woman in a white shirt.",
            "The woman with long, loose hair in a dark purple dress.",
            "The woman in a white T-shirt with a black jacket.",
            "The woman in a denim jacket."
        ],
        "ground_truth": "The woman with long, loose hair in a dark purple dress."
    },
    {
        "image_path": "benchmarks/gsi/childplay/22.png",
        "question_text": "Who is everyone listening to at this moment?",
        "options": [
            "The woman wearing a light gray top and pants, with her hair in a ponytail.",
            "The woman in a denim jacket.",
            "The woman in a white T-shirt with a black jacket.",
            "The woman with long, loose hair in a dark purple dress."
        ],
        "ground_truth": "The woman wearing a light gray top and pants, with her hair in a ponytail."
    }
]


GSI_GAZEFOLLOW_QUESTIONS = [
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0001.png",
        "question_text": "If someone enters the room now, how likely is that person to notice immediately?",
        "options": [
            "Very likely to notice and respond right away",
            "Somewhat likely to notice after a brief delay",
            "Unlikely to notice right away",
            "Will definitely ignore and not notice at all"
        ],
        "ground_truth": "Unlikely to notice right away"
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0002.png",
        "question_text": "What is the player in red preparing to do?",
        "options": [
            "Catch the frisbee.",
            "Throw the Frisbee",
            "Do nothing",
            "Someone off to the left or out of frame"
        ],
        "ground_truth": "Catch the frisbee."
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0003.png",
        "question_text": "Based on the performer's posture and where they are visually focused, what is the most likely immediate intention?",
        "options": [
            "Prepare to adjust foot placement to land the trick on the barrier",
            "Look for a friend to hand the skateboard to",
            "Check for oncoming cars on the street",
            "Signal to someone behind to start taking photos"
        ],
        "ground_truth": "Prepare to adjust foot placement to land the trick on the barrier"
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0004.png",
        "question_text": "What are the people doing?",
        "options": [
            "Dodging a baseball bat flying towards them",
            "Cheering and celebrating",
            "Causually watching the match without much commotion",
            "Angrily prostesting a perceived unfair referee",
        ],
        "ground_truth": "Dodging a baseball bat flying towards them"
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0005.png",
        "question_text": "What is the person most likely about to do next?",
        "options": [
            "Blow bubbles.",
            "Offer the bottle to someone else nearby",
            "Put the bottle into a bag or pocket",
            "Show the bottle up to the crowd"
        ],
        "ground_truth": "Blow bubbles."
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0006.png",
        "question_text": "Based on the group's attention and how the cake is being presented, who is most likely the child about to blow out the candles?",
        "options": [
            "The girl in the striped sweater seated at the table",
            "The blond boy on the left",
            "The child with curly hair in the foreground",
            "The child on the right holding a bottle"
        ],
        "ground_truth": "The girl in the striped sweater seated at the table"
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0009.png",
        "question_text": "Which child is most likely distracted and interacting with a teammate rather than facing forward for the team photo?",
        "options": [
            "The boy in the front row on the far left.",
            "The boy who has his hand near his face (slightly left of center)",
            "The child in the front row with arms crossed (center-right)",
            "The child standing at the far right of the group"
        ],
        "ground_truth": "The boy in the front row on the far left."
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0010.png",
        "question_text": "Based on the groups focus and body actions, what are they most likely doing together right now?",
        "options": [
            "Preparing and serving the meal to others",
            "Listening to someone giving a speech",
            "Playing a team sport nearby",
            "Taking a group selfie"
        ],
        "ground_truth": "Preparing and serving the meal to others"
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0011.png",
        "question_text": "Which person is most likely concentrating on where to land to avoid tripping?",
        "options": [
            "The young woman in the skirt near the front edge of the steps",
            "The student with glasses in the center",
            "The student jumping from the right holding books"
        ],
        "ground_truth": "The young woman in the skirt near the front edge of the steps"
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0012.png",
        "question_text": "What is the central woman's most likely role in the immediate social interaction involving the birds?",
        "options": [
            "She is presenting the birds to nearby onlookers as a demonstration.",
            "She is ignoring others and posing only for the camera.",
            "She is about to hand one of the birds to the person on her right.",
            "She is being instructed or guided by someone off-frame."
        ],
        "ground_truth": "She is ignoring others and posing only for the camera."
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0013.png",
        "question_text": "What are they most likely doing?",
        "options": [
            "Discussing the content on the computer.",
            "Viewing the content of the screen."
        ],
        "ground_truth": "Viewing the content of the screen."
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0014.png",
        "question_text": "What is the woman in black who is holding food most likely to be doing?",
        "options": [
            "Asking someone nearby how their drink tastes.",
            "Ordering food",
            "Get ready to take a bite of your own food."
        ],
        "ground_truth": "Asking someone nearby how their drink tastes."
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0015.png",
        "question_text": "Given the person's current focus, what is the most likely immediate social behavior?",
        "options": [
            "Continue concentrating on preparing the food and not engage in conversation.",
            "Look up to address someone and start a conversation right now.",
            "Pass the knife or chopped piece to another person across the counter.",
            "Abandon the task and walk away to attend to something else."
        ],
        "ground_truth": "Continue concentrating on preparing the food and not engage in conversation."
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0016.png",
        "question_text": "What are they doing?",
        "options": [
            "Getting ready to blow out the candles.",
            "Preparing to divide the cake.",
            "Getting ready to toast"
        ],
        "ground_truth": "Getting ready to blow out the candles."
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0017.png",
        "question_text": "What is the climber most likely about to do next?",
        "options": [
            "Reach down to handle or clip the rope/gear",
            "Look up to find the next handhold and continue climbing upward",
            "Turn to speak to someone below",
            "Remove their helmet"
        ],
        "ground_truth": "Look up to find the next handhold and continue climbing upward"
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0018.png",
        "question_text": "Which ball is the girl on the far right most likely to kick?",
        "options": [
            "The ball on the far right",
            "the second ball from the right",
            "The third ball from the right",
            "The leftmost ball"
        ],
        "ground_truth": "the second ball from the right"
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0020.png",
        "question_text": "What is he doing?",
        "options": [
            "Get ready to receive the frisbee.",
            "Prepare to throw an object toward someone in front of him",
            "Simply stretching his arm upward",
            "Waving to get someones attention"
        ],
        "ground_truth": "Get ready to receive the frisbee."
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0021.png",
        "question_text": "Which of the statements about the people in the picture is correct?",
        "options": [
            "They are all talking.",
            "The woman in black and the man in white are talking.",
            "They're studying something together and haven't started talking yet."
        ],
        "ground_truth": "The woman in black and the man in white are talking."
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0022.png",
        "question_text": "Which seated person is the standing person most likely addressing and therefore most likely to be asked to speak next?",
        "options": [
            "The man in the white button-down shirt in the center",
            "The woman in the purple sweater to the left of him",
            "The woman in the green cardigan seated to his right"
        ],
        "ground_truth": "The woman in the green cardigan seated to his right"
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0023.png",
        "question_text": "Based on their attention and actions, what best describes the likely social interaction between the two people?",
        "options": [
            "The adult is supervising and assisting the child as the child decorates the cake.",
            "The two are working on different stuff at the moment.",
            "The adult is scolding the child for their actions while the child avoids eye contact.",
            "They are competing to decorate separate cakes at the same time."
        ],
        "ground_truth": "The two are working on different stuff at the moment."
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0024.png",
        "question_text": "Given their positions and where attention converges, what is the most likely social role of the seated student relative to the standing students?",
        "options": [
            "Operating the computer and demonstrating something to the others.",
            "Waiting idly without interacting with the screen.",
            "Being instructed verbally by the standing students while not in control of the computer.",
            "Distracted and not participating in the task the others are engaged in."
        ],
        "ground_truth": "Operating the computer and demonstrating something to the others."
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0025.png",
        "question_text": "What are they doing?",
        "options": [
            "Taking a group photo to celebrate the victory.",
            "Communicating with each other",
            "Getting ready to ride a horse."
        ],
        "ground_truth": "Taking a group photo to celebrate the victory."
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0026.png",
        "question_text": "Based on their body orientation and where they are looking, what is the most likely interaction between the two women sitting on the floor with laptops?",
        "options": [
            "They are jointly editing the same document together on one laptop.",
            "They are independently working on separate tasks and not interacting.",
            "One woman is looking at the other womans screen, likely observing or seeking help.",
            "They are both watching a presentation happening off-camera ahead of them."
        ],
        "ground_truth": "They are independently working on separate tasks and not interacting."
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0027.png",
        "question_text": "What are they most likely to eat next?",
        "options": [
            "Pizza",
            "The food in the red pot.",
            "Drinking alcohol"
        ],
        "ground_truth": "Pizza"
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0028.png",
        "question_text": "Did they notice that someone was filming?",
        "options": [
            "yes",
            "No"
        ],
        "ground_truth": "yes"
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0029.png",
        "question_text": "Based on where people at the table are facing and looking, which person is most likely the immediate focus of a nearby guest and therefore most likely to be addressed next?",
        "options": [
            "The man in the foreground wearing a dark suit and tie (center front)",
            "The bald man seated slightly behind and to the left of the center of the image",
            "The woman with dark hair seated to the right of the center table",
            "The man leaning forward at the far right side of the image"
        ],
        "ground_truth": "The bald man seated slightly behind and to the left of the center of the image"
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0030.png",
        "question_text": "Based on the current focus and stance of the player in the front and center, what is he most likely about to do next?",
        "options": [
            "Look up to locate a teammate and make a pass",
            "Control the ball and begin dribbling or perform footwork",
            "Signal to the referee for a stoppage",
            "Turn away and walk off the field"
        ],
        "ground_truth": "Control the ball and begin dribbling or perform footwork"
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0031.png",
        "question_text": "Who is most likely to take the lead in initiating the cake cutting?",
        "options": [
            "The woman in the white dress",
            "The man in the vest",
            "They will start at the same time",
            "A guest at the table"
        ],
        "ground_truth": "The woman in the white dress"
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0032.png",
        "question_text": "Which person is most likely to be the center of the giraffes' attention and about to be directly interacted with by them?",
        "options": [
            "The person nearest the railing with an outstretched hand",
            "The child in her arm",
            "The person wearing a green shirt farther back",
        ],
        "ground_truth": "The person nearest the railing with an outstretched hand"
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0033.png",
        "question_text": "Given her posture and where she is looking, what is she most likely about to do next?",
        "options": [
            "Wait to enter the street after checking for oncoming traffic",
            "Continue browsing her phone without noticing traffic",
            "Call out to someone across the street",
            "Take a photo of the buildings"
        ],
        "ground_truth": "Continue browsing her phone without noticing traffic"
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0034.png",
        "question_text": "Who is most actively engaged in computer work in this group",
        "options": [
            "The person seated in the middle (green shirt).",
            "The person on the left.",
            "The person on the right.",
            "The computer monitor in front of them."
        ],
        "ground_truth": "The person seated in the middle (green shirt)."
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0035.png",
        "question_text": "Which two people are most likely jointly focused on the same task at the counter, indicating they are attending to the same object?",
        "options": [
            "The leftmost person and the center person",
            "The center person and the rightmost person",
            "The leftmost person and the rightmost person",
            "None of them appear to be focusing on the same task"
        ],
        "ground_truth": "The center person and the rightmost person"
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0036.png",
        "question_text": "What is the most likely social role of the adult standing in the backgrounding holding a cup?",
        "options": [
            "Supervising/attending caregiver watching the child",
            "A stranger trying to interact with the child",
            "A waiter taking an order",
            "Someone ignoring the child"
        ],
        "ground_truth": "Someone ignoring the child"
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0037.png",
        "question_text": "Based on the group's interactions, who is most likely to respond verbally to the person in the white shirt next?",
        "options": [
            "The person cutting the cake at the table",
            "The person seated to the right of the person in the white shirt (wearing a light grey t-shirt)",
            "The person leaning forward with head down behind the table",
            "The person mostly out of frame on the far left"
        ],
        "ground_truth": "The person seated to the right of the person in the white shirt (wearing a light grey t-shirt)"
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0039.png",
        "question_text": "What is the boy most likely preparing to do next?",
        "options": [
            "Brace for landing on the sand below",
            "Throw an object to someone nearby",
            "Wave to someone far away",
            "Dive into the water ahead"
        ],
        "ground_truth": "Brace for landing on the sand below"
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0041.png",
        "question_text": "What are they doing?",
        "options": [
            "Keeping an eye on the incoming ball.",
            "watching the ball leave",
            "Pay attention to the opposing players."
        ],
        "ground_truth": "Keeping an eye on the incoming ball."
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0042.png",
        "question_text": "Given the men's eye contact and body language, which immediate social interaction is most likely to occur?",
        "options": [
            "One of the men on the left is directing a remark to the man on the right, initiating a one-on-one exchange.",
            "The men on the left are disengaged and about to walk away without interacting.",
            "All three are actively participating in a group conversation.",
            "The middle man will immediately interrupt and take over the conversation."
        ],
        "ground_truth": "One of the men on the left is directing a remark to the man on the right, initiating a one-on-one exchange."
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0043.png",
        "question_text": "Given the skiers' positions and the scene, what is the left skier most likely to do next?",
        "options": [
            "Reach down and adjust the other skier's bindings.",
            "Move around the other skier's skis to avoid stepping on them.",
            "Push the other skier to make them move aside.",
            "Immediately start skiing straight downhill past the other skier."
        ],
        "ground_truth": "Move around the other skier's skis to avoid stepping on them."
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0044.png",
        "question_text": "Based on the person's posture and how they are holding the club, what are they most likely about to do?",
        "options": [
            "Take a golf-like swing to strike the object on the ground",
            "Walk away from the object without interacting with it",
            "Observe something unusual in the grass",
            "Pick the object up with their hands"
        ],
        "ground_truth": "Take a golf-like swing to strike the object on the ground"
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0045.png",
        "question_text": "Based on the group's arrangement and the man's posture while holding the bottle, who is he most likely addressing to pour or hand the bottle to?",
        "options": [
            "The woman closest to the camera on the left side of the table",
            "The man in the red shirt sitting next to that central woman",
            "Someone at the far end of the table on the left",
            "None of the above",
        ],
        "ground_truth": "None of the above"
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0046.png",
        "question_text": "What are is the skateboarder doing?",
        "options": [
            "Trading a skateboard",
            "giving a spectator an autograph",
            "Drawing graffiti on a skateboard"
        ],
        "ground_truth": "Spectator's signature"
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0047.png",
        "question_text": "Based on the player's posture and likely focus, what is she most likely preparing to do next?",
        "options": [
            "Move forward to return an incoming tennis shot",
            "Turn to talk to someone in the stands",
            "Walk off the court and leave the match",
            "Signal to the umpire to stop play"
        ],
        "ground_truth": "Move forward to return an incoming tennis shot"
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0048.png",
        "question_text": "Based on the peoples positions, body language, and interactions, what is the woman most likely doing with the cake?",
        "options": [
            "Helping the child blow out birthday candles",
            "Removing the cake from the table to cut it away from the children",
            "Lighting additional candles for the adults in the room",
            "Passing the cake to the seated boy on the left"
        ],
        "ground_truth": "Helping the child blow out birthday candles"
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0049.png",
        "question_text": "What is the person in the foreground trying to do?",
        "options": [
            "Catching the Frisbee.",
            "Throwing the frisbee.",
            "Talking the the man wearing a blue shirt."
        ],
        "ground_truth": "Catching the Frisbee."
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0050.png",
        "question_text": "Do the two people on the left likely know each other?",
        "options": [
            "No",
            "Yes"
        ],
        "ground_truth": "No"
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0051.png",
        "question_text": "Given that several people are focused on the interaction between the two seated people in front, what is most likely happening between them?",
        "options": [
            "They are playing a game with each other.",
            "They are arguing with raised voices.",
            "They are both checking their phones independently.",
            "They are getting up from their seats to leave."
        ],
        "ground_truth": "They are playing a game with each other."
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0052.png",
        "question_text": "What is the most likely social interaction occurring between the two people standing together under the umbrella?",
        "options": [
            "They are jointly examining or exchanging a small item from a bag.",
            "One is ignoring the other while the other talks to them.",
            "They are posing together to take a photograph.",
            "They are engaged in a heated argument."
        ],
        "ground_truth": "They are jointly examining or exchanging a small item from a bag."
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0053.png",
        "question_text": "Which of the following best describes the adult's likely immediate social behavior toward the child in the sandbox?",
        "options": [
            "Actively supervising and ready to interact with the child",
            "Distracted and about to walk away",
            "Directing the child's attention to a distant object outside the sandbox",
            "Ignoring the child and focused on a personal task"
        ],
        "ground_truth": "Actively supervising and ready to interact with the child"
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0054.png",
        "question_text": "Is the musician more likely concentrating on his instrument technique rather than visually cueing other band members or the audience?",
        "options": [
            "He is focusing on his instrument/playing technique",
            "He is visually cueing other band members to coordinate",
            "He is looking at the audience to engage them",
            "He is searching for a lost item nearby"
        ],
        "ground_truth": "He is focusing on his instrument/playing technique"
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0055.png",
        "question_text": "Given their current posture and focus, what is most likely to happen among these people in the next few minutes?",
        "options": [
            "They will continue focusing on their own devices and are unlikely to start a group conversation.",
            "One person will immediately draw the others' attention to a single phone and a group discussion will start.",
            "They will all look up together toward an off-camera event and begin talking to each other.",
            "Someone will pass an object across the row and initiate a shared interaction."
        ],
        "ground_truth": "They will continue focusing on their own devices and are unlikely to start a group conversation."
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0057.png",
        "question_text": "Which part is the seated attendee most interested in?",
        "options": [
            "Shoes and long socks",
            "Skirt",
            "Top",
            "Hair accessories"
        ],
        "ground_truth": "Shoes and long socks"
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0059.png",
        "question_text": "Which player is most likely to hit the ball next?",
        "options": [
            "The jumping player near the center/net area",
            "The player standing at the left baseline",
            "Both players will hit it at the same time",
            "Neither player will hit it next (the ball is out)"
        ],
        "ground_truth": "The jumping player near the center/net area"
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0061.png",
        "question_text": "What is the black suited guitarist most likely preparing to do during the group performance?",
        "options": [
            "Adjust his finger placement on the guitar to match the others' chords",
            "Turn to address the audience",
            "Read lyrics from the sheet music",
            "Start a side conversation with another person"
        ],
        "ground_truth": "Adjust his finger placement on the guitar to match the others' chords"
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0063.png",
        "question_text": "What are they doing?",
        "options": [
            "Watching TV",
            "Discussing television content."
        ],
        "ground_truth": "Watching TV"
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0064.png",
        "question_text": "Based on where people and the camera are looking, who is most likely the person being formally addressed or acknowledged at this moment?",
        "options": [
            "The player in the white uniform with number 20",
            "The player in the gray uniform with number 17",
            "the seated man in a suit",
            "the camera operator"
        ],
        "ground_truth": "The player in the white uniform with number 20"
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0067.png",
        "question_text": "Which person is most likely distracted by a personal item and not participating in a group conversation?",
        "options": [
            "The man in a dark/navy shirt seated on the left side near the aisle closest to the camera",
            "The woman with long blonde hair seated on the right side facing forward (one row ahead of the camera)",
            "The man in a gray hoodie seated in the back center",
            "The woman on the far left by the window closest to the camera"
        ],
        "ground_truth": "The man in a dark/navy shirt seated on the left side near the aisle closest to the camera"
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0068.png",
        "question_text": "Based on the people's orientations and where attention is focused, what is the woman in the floral top most likely to do next?",
        "options": [
            "Step forward to look at or engage with the stall (join the others)",
            "Turn away and continue walking past the stall",
            "Wave to someone across the path to get their attention",
            "Stop to search inside her bag"
        ],
        "ground_truth": "Step forward to look at or engage with the stall (join the others)"
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0069.png",
        "question_text": "Who is most likely to have taken this selfie?",
        "options": [
            "The man second from the left (grey shirt) who is looking at the box",
            "The man with his hand on his hip (right side)",
            "The person partially visible on the far left",
            "the woman"
        ],
        "ground_truth": "the woman"
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0070.png",
        "question_text": "What is the middle person most likely to do next given the visual cues in the scene?",
        "options": [
            "Ask the person on the left about the book they're holding",
            "Return to reading their own book quietly",
            "Stand up and walk away from the group",
            "Reach for a beer"
        ],
        "ground_truth": "Return to reading their own book quietly"
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0072.png",
        "question_text": "Based on their positions and movements in the scene, what are the two players most likely to do next?",
        "options": [
            "They're fighting for the ball.",
            "The player in purple will immediately dribble past the player in gray without contest.",
            "Both players will turn away from the ball and stop play.",
            "The game will be stopped by an official for a foul before either touches the ball."
        ],
        "ground_truth": "They're fighting for the ball."
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0073.png",
        "question_text": "What is the person in the foreground holding a plate most likely to do next?",
        "options": [
            "Get food from the nearby bowl onto their plate.",
            "Smell the food from a plate to check whether it has gone bad.",
            "Leave the buffet line without serving themselves.",
            "Reach forward to grab a drink cup at the front of the table."
        ],
        "ground_truth": "get food from the nearby bowl onto their plate."
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0074.png",
        "question_text": "Given the boy's posture and the horse's head positioned close to his outstretched hand, what is the boy most likely about to do?",
        "options": [
            "Feed the horse",
            "Step back away from the horse",
            "Call someone over for help",
            "Throw the object past the horse"
        ],
        "ground_truth": "Feed the horse"
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0075.png",
        "question_text": "What most likely happened at the scene?",
        "options": [
            "Something unusual occurred off-screen to the left.",
            "The tour guide in the crowd is explaining something.",
            "The crowd is discussing."
        ],
        "ground_truth": "Something unusual occurred off-screen to the left."
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0076.png",
        "question_text": "Based on the child's posture and where they are directing their attention, what is the child most likely about to do next?",
        "options": [
            "Push the floor tool across the tile to clean or move it",
            "Turn away and walk out of the room",
            "Place the tool into the cardboard box in the background",
            "Call an adult for help"
        ],
        "ground_truth": "Push the floor tool across the tile to clean or move it"
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0077.png",
        "question_text": "Based on the person's focus and body posture, what are they most likely to do next?",
        "options": [
            "Continue cutting along the marked line on the tree trunk.",
            "Turn and call to someone behind them.",
            "Stop to adjust their helmet or face shield.",
            "Put the tool down and walk away to get a different tool."
        ],
        "ground_truth": "Continue cutting along the marked line on the tree trunk."
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0078.png",
        "question_text": "Which statement best describes the person's current social behavior?",
        "options": [
            "Focused on their mobile device and not interacting with others",
            "Actively scanning the area to start a conversation",
            "Focused on the piece of paper she has",
            "Getting ready to leave the bench to join others"
        ],
        "ground_truth": "Focused on their mobile device and not interacting with others"
    },
    {
        "image_path": "benchmarks/gsi/gazefollow/original_0080.png",
        "question_text": "Who is most likely taking the lead in cutting the wedding cake?",
        "options": [
            "The bride",
            "The groom",
            "A nearby guest or server",
            "Neither of them"
        ],
        "ground_truth": "The bride"
    }
]


GSI_GOOREAL_QUESTIONS = [
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '1.jpg'),
        'question_text': 'Which of the following objects is the person looking at?',
        'options': ['Fita crackers (red box)', 'Grahams (dark blue box)', 'Pringles (red cylinder)', 'Fresh milk (green carton)'],
        'ground_truth': 'Grahams (dark blue box)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '1.jpg'),
        'question_text': 'What is the person most likely thinking about?',
        'options': ['Whether to buy Grahams (dark blue box)', 'Whether Fita crackers (red box) are too salty for her diet', 'Whether a box of Danisa cookies (blue box with a large white circle in the middle) is a suitable gift for a friend', 'Whether she should restock some kimchi noodles (red cup noodles)'],
        'ground_truth': 'Whether to buy Grahams (dark blue box)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '1.jpg'),
        'question_text': 'Which of the following advice, if given by an AI assistant, is most helpful for this person at the moment? (the milk in this image is in green cartons; chocolate chips are in blue and white boxes with white lids; Grahams is a dark blue box; kimchi noodles are red cup noodles)',
        'options': ['You still have 3 cartons of milk at home, no need to buy any fresh milk today.', 'You are on a diet, forget about chocolate chips as snacks.', 'You had Grahams before, and loved it.', 'You found Kimchi Noodles awful a month ago, maybe they are not the best choice.'],
        'ground_truth': 'You had Grahams before, and loved it.'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '2.jpg'),
        'question_text': 'Which of the following objects is the person looking at?',
        'options': ['Fita crackers (red box)', 'Grahams (dark blue box)', 'ChocoCrunchies (blue and white box)', 'Mango juice (red, green and yellow cartons)'],
        'ground_truth': 'Grahams (dark blue box)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '2.jpg'),
        'question_text': 'What is the person most likely thinking about?',
        'options': ['Whether to buy Grahams (dark blue box)', 'Whether Fita crackers (red box) are too salty for her diet', 'Whether she should restock some fresh milk (green cartons)', 'Whether she should restock some mango juice (red, green and yellow cartons)'],
        'ground_truth': 'Whether to buy Grahams (dark blue box)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '2.jpg'),
        'question_text': 'Which of the following advice, if given by an AI assistant, is most helpful for this person at the moment? (the milk in this image is in green cartons; Fita crackers are red boxes; Grahams is a dark blue box; ChocoCrunchies are in blue and white boxes; mango juice is in red, green and yellow cartons; Mamon is a yellow and white box)',
        'options': ['You still have 3 cartons of milk at home, no need to buy any fresh milk today.', 'You are on a diet, forget about Fita crackers as snacks.', 'It\'s 20 percent off if you buy ChocoCrunchies and Grahams together.', 'It\'s 30 percent off if you buy mango juice and Mamon together.'],
        'ground_truth': 'It\'s 20 percent off if you buy ChocoCrunchies and Grahams together.'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '3.jpg'),
        'question_text': 'Which of the following objects is the person looking at?',
        'options': ['Fita crackers (red box)', 'Chocolate Chips (blue and white box with white lid)', 'Pringles (red cylinder)', 'Orange juice (purple carton)'],
        'ground_truth': 'Chocolate Chips (blue and white box with white lid)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '3.jpg'),
        'question_text': 'What is the person most likely thinking about?',
        'options': ['Choosing between Fita crackers (red box) and Chocolate Chips (blue and white box with white lid)', 'Choosing between orange juice (purple carton) and Oishi Shrimp (striped red and yellow bag)', 'Whether he should restock some fresh milk (green cartons)', 'Whether she should restock Grahams (deep blue box)'],
        'ground_truth': 'Choosing between Fita crackers (red box) and Chocolate Chips (blue and white box with white lid)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '3.jpg'),
        'question_text': 'Which of the following advice, if given by an AI assistant, is most helpful for this person at the moment? (the milk in this image is in green cartons; Fita crackers are red boxes; Oishi Shrimp is a striped red and yellow bag; Chocolate Chips are in blue and white boxes with white lids; Pringles are in red cylinders)',
        'options': ['You still have 3 cartons of milk at home, no need to buy any fresh milk today.', 'You had a pretty bad allergic reaction the last time you had Oishi Shrimp.', 'Between Fita and Chocolate Chips, Fita is a bit healthier due to its lower sugar and fat content.', 'Pringles is on sale at the store next door. You should buy them there.'],
        'ground_truth': 'Between Fita and Chocolate Chips, Fita is a bit healthier due to its lower sugar and fat content.'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '4.jpg'),
        'question_text': 'Which of the following objects is the person looking at?',
        'options': ['Koko Krunch (brown box)', 'Chocolate Chips (blue and white box with white lid)', 'Fita crackers (red boxes)', 'Oishi Shrimp (striped red and yellow bag)'],
        'ground_truth': 'Chocolate Chips (blue and white box with white lid)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '4.jpg'),
        'question_text': 'What is the person most likely thinking about?',
        'options': ['Whether to buy Oishi Shrimp (striped red and yellow bag)', 'Whether to buy Chocolate chips (blue and white box with white lid)', 'Whether he should restock some fresh milk (green cartons)', 'Whether she should restock Kellogg\'s Corn Flakes (red, white and blue box)'],
        'ground_truth': 'Whether to buy Chocolate Chips (blue and white box with white lid)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '4.jpg'),
        'question_text': 'Which of the following advice, if given by an AI assistant, is most helpful for this person at the moment? (the milk in this image is in green cartons; Fita crackers are red boxes; Oishi Shrimp is a striped red and yellow bag; Chocolate Chips are in blue and white boxes with white lids; Pringles are in red cylinders)',
        'options': ['You still have 3 cartons of milk at home, no need to buy any fresh milk today.', 'You had a pretty bad allergic reaction the last time you had Oishi Shrimp.', 'Last time you bought this big a box of Chocolate Chips, you couldn\'t finish all of it before the expiration date. Maybe you should find a smaller package', 'Pringles is on sale at the store next door. You should buy them there.'],
        'ground_truth': 'Last time you bought this big a box of Chocolate Chips, you couldn\'t finish all of it before the expiration date. Maybe you should find a smaller package'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '5.jpg'),
        'question_text': 'Which of the following objects is the person looking at?',
        'options': ['Koko Krunch (brown box)', 'Butterlicious (orange boxes)', 'Buttercake (white and blue box)', 'Pringles (red cylinder)'],
        'ground_truth': 'Buttercake (white box with blue accents)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '5.jpg'),
        'question_text': 'What is the person most likely thinking about?',
        'options': ['Whether to buy Oishi Shrimp (striped red and yellow bag)', 'Whether to buy Butterlicious (orange boxes)', 'Whether he should restock some Buttercake (white and blue box)', 'Whether he should restock Kellogg\'s Corn Flakes (red, white and blue box)'],
        'ground_truth': 'Whether he should restock some Buttercake (white box with blue accents)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '5.jpg'),
        'question_text': 'Which of the following advice, if given by an AI assistant, is most helpful for this person at the moment? (the milk in this image is in green cartons; Buttercake is in white and blue boxes; Chocolate Chips are in blue and white boxes with white lids; Pringles are in red cylinders)',
        'options': ['You still have 3 cartons of milk at home, no need to buy any fresh milk today.', 'The Buttercake production line introduces trace amount of nuts and peanuts. Avoid if you have an allergy.', 'Last time you bought this big a box of Chocolate Chips, you couldn\'t finish all of it before the expiration date. Maybe you should find a smaller package', 'Pringles is on sale at the store next door. You should buy them there.'],
        'ground_truth': 'Last time you bought this big a box of Chocolate Chips, you couldn\'t finish all of it before the expiration date. Maybe you should find a smaller package'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '6.jpg'),
        'question_text': 'Which of the following objects is the person looking at?',
        'options': ['Fita crackers (red box)', 'Butterlicious (orange boxes)', 'Kellogg\'s Corn Flakes (red, white and blue box)', 'Pringles (red cylinder)'],
        'ground_truth': 'Kellogg\'s Corn Flakes (red, white and blue box)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '6.jpg'),
        'question_text': 'What is the person most likely thinking about?',
        'options': ['Whether to buy Kellogg\'s Corn Flakes (red, white and blue box)', 'Whether to buy Butterlicious (orange boxes)', 'Whether he should restock Pringles (red cylinder)', 'Whether he should buy Orange juice (purple carton)'],
        'ground_truth': 'Whether to buy Kellogg\'s Corn Flakes (red, white and blue box)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '6.jpg'),
        'question_text': 'Which of the following advice, if given by an AI assistant, is most helpful for this person at the moment? (the milk in this image is in green cartons; Kellogg\'s Corn Flakes are in red, white and blue boxes; Kimchi Noodles are red cup noodles; Pringles are in red cylinders)',
        'options': ['You still have 3 cartons of milk at home, no need to buy any fresh milk today.', 'Kellogg\'s Corn Flakes are ultraprocessed. Fresh produce is better for your health.', 'Kimchi Noodles are too salty for your dietary requirements', 'Pringles is on sale at the store next door. You should buy them there.'],
        'ground_truth': 'Kellogg\'s Corn Flakes are ultraprocessed. Fresh produce is better for your health.'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '7.jpg'),
        'question_text': 'Which of the following objects is the person looking at?',
        'options': ['Mamon (yellow and white box)', 'Fresh milk (green cartons)', 'Kellogg\'s Corn Flakes (red, white and blue box)', 'Grahams (deep blue boxes)'],
        'ground_truth': 'Mamon (yellow and white box)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '7.jpg'),
        'question_text': 'What is the person most likely thinking about?',
        'options': ['Whether to buy Kellogg\'s Corn Flakes (red, white and blue box)', 'Whether to buy Mamon (yellow and white box)', 'Whether she should restock Pringles (red cylinder)', 'Whether he should buy Fita crackers (red box)'],
        'ground_truth': 'Whether to buy Mamon (yellow and white box)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '7.jpg'),
        'question_text': 'Which of the following advice, if given by an AI assistant, is most helpful for this person at the moment? (the milk in this image is in green cartons; Mamon is in yellow and white boxes; Kimchi Noodles are red cup noodles; Pringles are in red cylinders)',
        'options': ['You still have 3 cartons of milk at home, no need to buy any fresh milk today.', 'Mamon is ultraprocessed. Fresh produce is better for your health.', 'Kimchi Noodles are too salty for your dietary requirements', 'Pringles is on sale at the store next door. You should buy them there.'],
        'ground_truth': 'Mamon is ultraprocessed. Fresh produce is better for your health.'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '8.jpg'),
        'question_text': 'Which of the following objects is the person looking at?',
        'options': ['Chuckie (yellow cartons)', 'Butterlicious (orange boxes)', 'Kellogg\'s Corn Flakes (red, white and blue box)', 'Stars (red and blue boxes)'],
        'ground_truth': 'Chuckie (yellow cartons)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '8.jpg'),
        'question_text': 'What is the person most likely thinking about?',
        'options': ['Whether to buy Kellogg\'s Corn Flakes (red, white and blue box)', 'Whether to buy Butterlicious (orange boxes)', 'Whether he should restock Chuckie (yellow cartons)', 'Whether he should buy Orange juice (purple carton)'],
        'ground_truth': 'Whether he should restock Chuckie (yellow cartons)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '8.jpg'),
        'question_text': 'Which of the following advice, if given by an AI assistant, is most helpful for this person at the moment? (Chuckie is in yellow cartons; Kellogg\'s Corn Flakes are in red, white and blue boxes; Kimchi Noodles are red cup noodles; Pringles are in red cylinders)',
        'options': ['You still have 3 cartons of chuckie at home, no need to buy any today.', 'Kellogg\'s Corn Flakes are ultraprocessed. Fresh produce is better for your health.', 'Kimchi Noodles are too salty for your dietary requirements', 'Pringles is on sale at the store next door. You should buy them there.'],
        'ground_truth': 'You still have 3 cartons of chuckie at home, no need to buy any today.'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '9.jpg'),
        'question_text': 'Which of the following objects is the person looking at?',
        'options': ['Chuckie (yellow cartons)', 'Butterlicious (orange boxes)', 'Camomille (white and yellow boxes)', 'Pringles (red cylinders)'],
        'ground_truth': 'Camomille (white and yellow boxes)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '9.jpg'),
        'question_text': 'What is the person most likely thinking about?',
        'options': ['Whether to buy Kellogg\'s Corn Flakes (red, white and blue box)', 'Whether to buy Butterlicious (orange boxes)', 'Whether she should restock Chuckie (yellow cartons)', 'Whether she should buy Camomille (white and yellow boxes)'],
        'ground_truth': 'Whether she should buy Camomille (white and yellow boxes)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '9.jpg'),
        'question_text': 'Which of the following advice, if given by an AI assistant, is most helpful for this person at the moment? (Chuckie is in yellow cartons; Kellogg\'s Corn Flakes are in red, white and blue boxes; Camomille is in white and yellow boxes; Pringles are in red cylinders)',
        'options': ['You still have 3 cartons of chuckie at home, no need to buy any today.', 'Kellogg\'s Corn Flakes are ultraprocessed. Fresh produce is better for your health.', 'Camomille tea is a great zero-carb, zero additive drink. You should try it!', 'Pringles is on sale at the store next door. You should buy them there.'],
        'ground_truth': 'Camomille tea is a great zero-carb, zero additive drink. You should try it!'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '10.jpg'),
        'question_text': 'Which of the following objects is the person looking at?',
        'options': ['Chuckie (yellow cartons)', 'Butterlicious (orange boxes)', 'Koko Krunch (brown boxes with green top)', 'Oishi Prawn (yellow, red and white bags)'],
        'ground_truth': 'Oishi Prawn (yellow, red and white bags)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '10.jpg'),
        'question_text': 'What is the person most likely thinking about?',
        'options': ['Whether to buy Kellogg\'s Corn Flakes (red, white and blue box)', 'Whether to buy Butterlicious (orange boxes)', 'Choosing between Koko Krunch (brown boxes with green top) and Oishi Prawn (yellow, red, and white bags)', 'Whether she should buy Camomille (white and yellow boxes)'],
        'ground_truth': 'Choosing between Koko Krunch (brown boxes with green top) and Oishi Prawn (yellow, red, and white bags)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '10.jpg'),
        'question_text': 'Which of the following advice, if given by an AI assistant, is most helpful for this person at the moment? (Oishi Prawn is in yellow, red and white bags; Kellogg\'s Corn Flakes are in red, white and blue boxes; Camomille is in white and yellow boxes; Pringles are in red cylinders)',
        'options': ['Oishi Prawn is ultraprocessed and too greasy for your diet.', 'Kellogg\'s Corn Flakes are ultraprocessed. Fresh produce is better for your health.', 'Camomille tea is a great zero-carb, zero additive drink. You should try it!', 'Pringles is on sale at the store next door. You should buy them there.'],
        'ground_truth': 'Oishi Prawn is ultraprocessed and too greasy for your diet.'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '11.jpg'),
        'question_text': 'Which of the following objects is the person looking at?',
        'options': ['Chuckie (yellow cartons)', 'Kellogg\'s Corn Flakes (red, white and blue box)', 'Honey Stars (blue boxes with green top)', 'Locally Mango (red and yellow cartons)'],
        'ground_truth': 'Honey Stars (blue boxes with green top)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '11.jpg'),
        'question_text': 'What is the person most likely thinking about?',
        'options': ['Whether to buy Kellogg\'s Corn Flakes (red, white and blue box)', 'Whether to buy Honey Stars (blue boxes with green top)', 'Choosing between Kimchi Noodles (red cup noodles) and Mamon (yellow and white box)', 'Whether he should buy fresh milk (green cartons)'],
        'ground_truth': 'Whether to buy Honey Stars (blue boxes with green top)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '11.jpg'),
        'question_text': 'Which of the following advice, if given by an AI assistant, is most helpful for this person at the moment? (Kellogg\'s Corn Flakes are in red, white and blue boxes; Kimchi Noodles are red cup noodles; Honey Stars are blue boxes with green top; fresh milk is in green cartons)',
        'options': ['The Honey Stars here are on sale.', 'Kellogg\'s Corn Flakes are ultraprocessed. Fresh produce is better for your health.', 'Last time you complained about Kimchi Noodles tasting too artificial. Are you sure you want to try it again?', 'You still have four cartons of milk at home, no need to restock now.'],
        'ground_truth': 'The Honey Stars here are on sale.'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '12.jpg'),
        'question_text': 'Which of the following objects is the person looking at?',
        'options': ['Chuckie (yellow cartons)', 'Kellogg\'s Corn Flakes (red, white and blue box)', 'Fita Crackers (red boxes)', 'Fresh milk (green cartons)'],
        'ground_truth': 'Fresh milk (green cartons)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '12.jpg'),
        'question_text': 'What is the person most likely thinking about?',
        'options': ['Whether to buy Kellogg\'s Corn Flakes (red, white and blue box)', 'Whether to buy Honey Stars (blue boxes with green top)', 'Choosing between Kimchi Noodles (red cup noodles) and Mamon (yellow and white box)', 'Whether he should buy fresh milk (green cartons)'],
        'ground_truth': 'Whether he should buy fresh milk (green cartons)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '12.jpg'),
        'question_text': 'Which of the following advice, if given by an AI assistant, is most helpful for this person at the moment? (Kellogg\'s Corn Flakes are in red, white and blue boxes; Kimchi Noodles are red cup noodles; Honey Stars are blue boxes with green top; fresh milk is in green cartons)',
        'options': ['The Honey Stars here are on sale.', 'Kellogg\'s Corn Flakes are ultraprocessed. Fresh produce is better for your health.', 'Last time you complained about Kimchi Noodles tasting too artificial. Are you sure you want to try it again?', 'You still have four cartons of milk at home, no need to restock now.'],
        'ground_truth': 'You still have four cartons of milk at home, no need to restock now.'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '13.jpg'),
        'question_text': 'Which of the following objects is the person looking at?',
        'options': ['Chuckie (yellow cartons)', 'Oishi Prawn (striped red and yellow bag)', 'iHop (white boxes with a red corner)', 'Fresh milk (green cartons)'],
        'ground_truth': 'iHop (white boxes with a red corner)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '13.jpg'),
        'question_text': 'What is the person most likely thinking about?',
        'options': ['Whether to buy Kellogg\'s Corn Flakes (red, white and blue box)', 'Whether to buy iHop (white boxes with a red corner)', 'Choosing between Oishi Prawn (striped red and yellow bag) and Chuckie (yellow cartons)', 'Whether he should buy fresh milk (green cartons)'],
        'ground_truth': 'Whether to buy iHop (white boxes with a red corner)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '13.jpg'),
        'question_text': 'Which of the following advice, if given by an AI assistant, is most helpful for this person at the moment? (Kellogg\'s Corn Flakes are in red, white and blue boxes; iHop is in white boxes with a red corner; Oishi Prawn is in striped red and yellow bags; fresh milk is in green cartons)',
        'options': ['The iHop production line is also used to process nuts. Check for allergens.', 'Kellogg\'s Corn Flakes are ultraprocessed. Fresh produce is better for your health.', 'Last time you complained about Oishi Prawn tasting too artificial. Are you sure you want to try it again?', 'You still have four cartons of milk at home, no need to restock now.'],
        'ground_truth': 'The iHop production line is also used to process nuts. Check for allergens.'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '14.jpg'),
        'question_text': 'Which of the following objects is the person looking at?',
        'options': ['Chuckie (yellow cartons)', 'Oishi Prawn (striped red and yellow bag)', 'iHop (white boxes with a red corner)', 'Fresh milk (green cartons)'],
        'ground_truth': 'Oishi Prawn (striped red and yellow bag)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '14.jpg'),
        'question_text': 'What is the person most likely thinking about?',
        'options': ['Whether to buy Kellogg\'s Corn Flakes (red, white and blue box)', 'Whether to buy iHop (white boxes with a red corner)', 'Choosing between Oishi Prawn (striped red and yellow bag) and Chuckie (yellow cartons)', 'Whether he should buy fresh milk (green cartons)'],
        'ground_truth': 'Choosing between Oishi Prawn (striped red and yellow bag) and Chuckie (yellow cartons)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '14.jpg'),
        'question_text': 'Which of the following advice, if given by an AI assistant, is most helpful for this person at the moment? (Kellogg\'s Corn Flakes are in red, white and blue boxes; iHop is in white boxes with a red corner; Oishi Prawn is in striped red and yellow bags; fresh milk is in green cartons)',
        'options': ['The iHop production line is also used to process nuts. Check for allergens.', 'Kellogg\'s Corn Flakes are ultraprocessed. Fresh produce is better for your health.', 'Last time you complained about Oishi Prawn tasting too artificial. Are you sure you want to try it again?', 'You still have four cartons of milk at home, no need to restock now.'],
        'ground_truth': 'Last time you complained about Oishi Prawn tasting too artificial. Are you sure you want to try it again?'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '15.jpg'),
        'question_text': 'Which of the following objects is the person looking at?',
        'options': ['Mamon (white and yellow boxes)', 'Grahams (deep blue boxes)', 'Locally Mango (red and yellow cartons)', 'Buttercake (white and blue boxes)'],
        'ground_truth': 'Mamon (white and yellow boxes)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '15.jpg'),
        'question_text': 'What is the person most likely thinking about?',
        'options': ['Whether to buy Mamon (white and yellow boxes)', 'Whether to buy Grahams (deep blue boxes)', 'Choosing between Oishi Prawn (striped red and yellow bag) and Fita crackers (red boxes)', 'Whether he should buy Hansel (yellow and brown boxes)'],
        'ground_truth': 'Whether to buy Mamon (white and yellow boxes)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '15.jpg'),
        'question_text': 'Which of the following advice, if given by an AI assistant, is most helpful for this person at the moment? (Grahams is in dark blue boxes; Mamon is in white and yellow boxes; Oishi Prawn is in striped red and yellow bags; Camomille tea is in small white boxes)',
        'options': ['The Grahams production line is also used to process nuts. Check for allergens.', 'Mamon is ultraprocessed. Fresh produce is better for your health.', 'Last time you complained about Oishi Prawn tasting too artificial. Are you sure you want to try it again?', 'The Camomille at home would last at least another month, no need to restock today.'],
        'ground_truth': 'Mamon is ultraprocessed. Fresh produce is better for your health.'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '16.jpg'),
        'question_text': 'Which of the following objects is the person looking at?',
        'options': ['Mamon (white and yellow boxes)', 'Hansel (yellow and brown boxes)', 'Camomille (small yellow boxes)', 'Pringles (red cylinders)'],
        'ground_truth': 'Pringles (red cylinders)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '16.jpg'),
        'question_text': 'What is the person most likely thinking about?',
        'options': ['Whether to buy Mamon (white and yellow boxes)', 'Whether to buy Pringles (red cylinders)', 'Choosing between Oishi Prawn (striped red and yellow bag) and Fita crackers (red boxes)', 'Whether he should buy Hansel (yellow and brown boxes)'],
        'ground_truth': 'Whether to buy Pringles (red cylinders)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '16.jpg'),
        'question_text': 'Which of the following advice, if given by an AI assistant, is most helpful for this person at the moment? (Pringles is in red cylinders; Mamon is in white and yellow boxes; Oishi Prawn is in striped red and yellow bags; Camomille tea is in small white boxes)',
        'options': ['Pringles is on sale at the store next door. They are much cheaper over there.', 'Mamon is ultraprocessed. Fresh produce is better for your health.', 'Last time you complained about Oishi Prawn tasting too artificial. Are you sure you want to try it again?', 'The Camomille at home would last at least another month, no need to restock today.'],
        'ground_truth': 'Pringles is on sale at the store next door. They are much cheaper over there.'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '17.jpg'),
        'question_text': 'Which of the following objects is the person looking at?',
        'options': ['Oishi Prawn (striped red and yellow bags)', 'Chuckie (yellow cartons)', 'Honey Stars (blue box)', 'Pringles (red cylinders)'],
        'ground_truth': 'Oishi Prawn (striped red and yellow bags)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '17.jpg'),
        'question_text': 'What is the person most likely thinking about?',
        'options': ['Whether to buy Oishi Prawn (striped red and yellow bags)', 'Whether to buy Pringles (red cylinders)', 'Whether to buy Chuckie (yellow cartons)', 'Whether he should buy Honey Stars (blue box)'],
        'ground_truth': 'Whether to buy Oishi Prawn (striped red and yellow bags)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '17.jpg'),
        'question_text': 'Which of the following advice, if given by an AI assistant, is most helpful for this person at the moment? (Pringles is in red cylinders; Chuckie is in yellow cartons; Oishi Prawn is in striped red and yellow bags; Camomille tea is in small white boxes)',
        'options': ['Pringles is on sale at the store next door. They are much cheaper over there.', 'Chuckie is ultraprocessed. Fresh produce is better for your health.', 'Last time you complained about Oishi Prawn tasting too artificial. Are you sure you want to try it again?', 'The Camomille at home would last at least another month, no need to restock today.'],
        'ground_truth': 'Last time you complained about Oishi Prawn tasting too artificial. Are you sure you want to try it again?'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '18.jpg'),
        'question_text': 'Which of the following objects is the person looking at?',
        'options': ['Camomille (small yellow and white boxes)', 'Locally Mango (red cartons)', 'Danisa Cookies (dark blue box with white circle in the middle)', 'Pringles (red cylinders)'],
        'ground_truth': 'Camomille (small yellow and white boxes)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '18.jpg'),
        'question_text': 'What is the person most likely thinking about?',
        'options': ['Whether to buy Camomille (small yellow and white boxes)', 'Whether to buy Pringles (red cylinders)', 'Whether to buy Danisa Cookies (dark blue box with white circle in the middle)', 'Choosing between Hansel (yellow and brown box) and Grahams (dark blue box)'],
        'ground_truth': 'Whether to buy Camomille (small yellow and white boxes)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '18.jpg'),
        'question_text': 'Which of the following advice, if given by an AI assistant, is most helpful for this person at the moment? (Pringles is in red cylinders; Hansel is in yellow and brown boxes; Oishi Prawn is in striped red and yellow bags; Camomille tea is in small white boxes)',
        'options': ['Pringles is on sale at the store next door. They are much cheaper over there.', 'Hansel is ultraprocessed. Fresh produce is better for your health.', 'Last time you complained about Oishi Prawn tasting too artificial. Are you sure you want to try it again?', 'The Camomille at home would last at least another month, no need to restock today.'],
        'ground_truth': 'The Camomille at home would last at least another month, no need to restock today.'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '19.jpg'),
        'question_text': 'Which of the following objects is the person looking at?',
        'options': ['Chuckie (yellow cartons)', 'Butterlicious (Orange boxes)', 'Danisa Cookies (dark blue box with white circle in the middle)', 'Kimchi Noodles (red cup noodles)'],
        'ground_truth': 'Danisa Cookies (dark blue box with white circle in the middle)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '19.jpg'),
        'question_text': 'What is the person most likely thinking about?',
        'options': ['Whether to buy Chuckie (yellow cartons)', 'Whether to buy Pringles (red cylinders)', 'Whether to buy Danisa Cookies (dark blue box with white circle in the middle)', 'Choosing between Kimchi Noodles (red cup noodles) and Butterlicious (orange box)'],
        'ground_truth': 'Whether to buy Danisa Cookies (dark blue box with white circle in the middle)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '19.jpg'),
        'question_text': 'Which of the following advice, if given by an AI assistant, is most helpful for this person at the moment? (Pringles is in red cylinders; Danisa Cookies are in dark blue boxes with white circle in the middle; Chuckie is in yellow cartons; Kimchi Noodles are red cup noodles)',
        'options': ['Pringles is on sale at the store next door. They are much cheaper over there.', 'Danisa Cookies would be a great gift for your friend.', 'Last time you complained about Chuckie tasting too artificial. Are you sure you want to try it again?', 'The Kimchi Noodles at home would last at least another month, no need to restock today.'],
        'ground_truth': 'Danisa Cookies would be a great gift for your friend.'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '20.jpg'),
        'question_text': 'Which of the following objects is the person looking at?',
        'options': ['Oishi Prawn (striped yellow and red bags)', 'Honey Stars (Blue box)', 'Chocolate Chips (large white container with a lid)', 'Chuckie (yellow cartons)'],
        'ground_truth': 'Oishi Prawn (striped yellow and red bags)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '20.jpg'),
        'question_text': 'What is the person most likely thinking about?',
        'options': ['Whether to buy Chuckie (yellow cartons)', 'Whether to buy Honey Stars (Blue box)', 'Whether to buy Oishi Prawn (striped yellow and red bags)', 'Choosing between Chocolate Chips (large white container with lid) and orange juice (red and dark blue cartons)'],
        'ground_truth': 'Whether to buy Oishi Prawn (striped yellow and red bags)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '20.jpg'),
        'question_text': 'Which of the following advice, if given by an AI assistant, is most helpful for this person at the moment? (Chuckie is in yellow cartons; Oishi Prawn is in striped yellow and red bags; Honey Stars are in blue boxes; Chocolate Chips are in large white containers with lid; Butterlicious is in orange boxes)',
        'options': ['Butterlicious is on sale at the store next door. They are much cheaper over there.', 'Chocolate Chips would be a great gift for your friend.', 'Last time you complained about Chuckie tasting too artificial. Are you sure you want to try it again?', 'Oishi Prawn is ultraprocessed and too oily for your diet.'],
        'ground_truth': 'Oishi Prawn is ultraprocessed and too oily for your diet.'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '21.jpg'),
        'question_text': 'Which of the following objects is the person looking at?',
        'options': ['Hansel (large yellow and brown box)', 'Pringles (red cylinders)', 'Piknik (orange cylinders)', 'Camomille (small yellow and white box)'],
        'ground_truth': 'Hansel (large yellow and brown box)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '21.jpg'),
        'question_text': 'What is the person most likely thinking about?',
        'options': ['Whether to buy Pringles (red cylinders)', 'Whether to buy Hansel (large yellow and brown box)', 'Whether to buy Piknik (orange cylinders)', 'Choosing between Danisa Cookies (large box with a white circle in the middle and blue corners) and Grahams (large dark blue box)'],
        'ground_truth': 'Whether to buy Hansel (large yellow and brown box)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '21.jpg'),
        'question_text': 'Which of the following advice, if given by an AI assistant, is most helpful for this person at the moment? (Pringles is in red cylinders; Hansel is in large yellow and brown boxes; Piknik is in orange cylinders; Butterlicious is in orange boxes)',
        'options': ['Hansel is on sale at the store next door. They are much cheaper over there.', 'Pringles are Tom\'s favorite snack. Perhaps you can buy some for him.', 'Last time you complained about Piknik tasting too artificial. Are you sure you want to try it again?', 'Butterlicious is ultraprocessed and too oily for your diet.'],
        'ground_truth': 'Hansel is on sale at the store next door. They are much cheaper over there.'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '22.jpg'),
        'question_text': 'Which of the following objects is the person looking at?',
        'options': ['Honey Stars (deep blue box)', 'Kellogg\'s Corn Flakes (red, white and blue box)', 'Chuckie (yellow cartons)', 'Butterlicious (orange box)'],
        'ground_truth': 'Honey Stars (deep blue box)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '22.jpg'),
        'question_text': 'What is the person most likely thinking about?',
        'options': ['Whether to buy Kellogg\'s Corn Flakes (red, white and blue box)', 'Whether to buy Honey Stars (deep blue box)', 'Whether to buy Chuckie (yellow cartons)', 'Choosing between Butterlicious (orange box) and iHop (white box with a red corner)'],
        'ground_truth': 'Whether to buy Honey Stars (deep blue box)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '22.jpg'),
        'question_text': 'Which of the following advice, if given by an AI assistant, is most helpful for this person at the moment? (Honey Stars are in blue boxes; Kellogg\'s corn flakes are in red, white and blue boxes; Chuckie is in yellow cartons; Butterlicious is in orange boxes)',
        'options': ['Honey Stars are on sale at the store next door. They are much cheaper over there.', 'Kellogg\'s Corn Flakes are produced in a factory that also handles nuts. Check for allergens.', 'Last time you complained about Chuckie tasting too artificial. Are you sure you want to try it again?', 'Butterlicious is ultraprocessed and too oily for your diet.'],
        'ground_truth': 'Honey Stars are on sale at the store next door. They are much cheaper over there.'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '23.jpg'),
        'question_text': 'Which of the following objects is the person looking at?',
        'options': ['Oishi Prawn (striped yellow and red bag)', 'Kellogg\'s Corn Flakes (red, white and blue box)', 'Chuckie (yellow cartons)', 'Butterlicious (orange box)'],
        'ground_truth': 'Oishi Prawn (striped yellow and red bag)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '23.jpg'),
        'question_text': 'What is the person most likely thinking about?',
        'options': ['Whether to buy Kellogg\'s Corn Flakes (red, white and blue box)', 'Whether to buy Oishi Prawn (striped yellow and red bag)', 'Whether to buy Chuckie (yellow cartons)', 'Choosing between Butterlicious (orange box) and iHop (white box with a red corner)'],
        'ground_truth': 'Whether to buy Oishi Prawn (striped yellow and red bag)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '23.jpg'),
        'question_text': 'Which of the following advice, if given by an AI assistant, is most helpful for this person at the moment? (Oishi Prawn is in striped yellow and red bags; Kellogg\'s corn flakes are in red, white and blue boxes; Chuckie is in yellow cartons; Butterlicious is in orange boxes)',
        'options': ['Oishi Prawn is on sale at the store next door. They are much cheaper over there.', 'Kellogg\'s Corn Flakes are produced in a factory that also handles nuts. Check for allergens.', 'Last time you complained about Chuckie tasting too artificial. Are you sure you want to try it again?', 'Butterlicious is ultraprocessed and too oily for your diet.'],
        'ground_truth': 'Oishi Prawn is on sale at the store next door. They are much cheaper over there.'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '24.jpg'),
        'question_text': 'Which of the following objects is the person looking at?',
        'options': ['Grahams (dark blue box)', 'Butterlicious (orange box)', 'Piknik (orange cylinder)', 'Fita crackers (red box)'],
        'ground_truth': 'Grahams (dark blue box)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '24.jpg'),
        'question_text': 'What is the person most likely thinking about?',
        'options': ['Whether to buy Grahams (dark blue box)', 'Whether to buy Butterlicious (orange box)', 'Whether to buy Piknik (orange cylinder)', 'Choosing between Fita crackers (red box) and Oishi Prawn (striped yellow and red bag)'],
        'ground_truth': 'Whether to buy Grahams (dark blue box)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '24.jpg'),
        'question_text': 'Which of the following advice, if given by an AI assistant, is most helpful for this person at the moment? (Oishi Prawn is in striped yellow and red bags; Butterlicious is in orange boxes; Grahams is in dark blue boxes; Piknik is in orange cylinders)',
        'options': ['Oishi Prawn is on sale at the store next door. They are much cheaper over there.', 'Grahams are produced in a factory that also handles nuts. Check for allergens.', 'Last time you complained about Piknik tasting too artificial. Are you sure you want to try it again?', 'Butterlicious is ultraprocessed and too oily for your diet.'],
        'ground_truth': 'Grahams are produced in a factory that also handles nuts. Check for allergens.'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '25.jpg'),
        'question_text': 'Which of the following objects is the person looking at?',
        'options': ['Koko Krunch (dark brown box)', 'Fresh milk (green carton)', 'Orange juice (deep blue and magenta carton)', 'Fita crackers (red box)'],
        'ground_truth': 'Fresh milk (green carton)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '25.jpg'),
        'question_text': 'What is the person most likely thinking about?',
        'options': ['Whether to buy Koko Krunch (dark brown box)', 'Whether to buy Fresh milk (green carton)', 'Whether to buy orange juice (deep blue and magenta carton)', 'Choosing between Fita crackers (red box) and Oishi Prawn (striped yellow and red bag)'],
        'ground_truth': 'Whether to buy Fresh milk (green carton)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '25.jpg'),
        'question_text': 'Which of the following advice, if given by an AI assistant, is most helpful for this person at the moment? (Oishi Prawn is in striped yellow and red bags; Butterlicious is in orange boxes; Fresh milk is in green cartons; Koko Krunch is in dark brown boxes)',
        'options': ['Oishi Prawn is on sale at the store next door. They are much cheaper over there.', 'Fresh milk is nutritious addition to your breakfast routine.', 'Last time you complained about Koko Krunch tasting too sweet. Are you sure you want to try it again?', 'Butterlicious is ultraprocessed and too oily for your diet.'],
        'ground_truth': 'Fresh milk is nutritious addition to your breakfast routine.'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '26.jpg'),
        'question_text': 'Which of the following objects is the person looking at?',
        'options': ['Koko Krunch (dark brown box)', 'Butterlicious (orange boxes)', 'Chocolate Chips (large white container with lid)', 'Pringles (red cylinder)'],
        'ground_truth': 'Butterlicious (orange boxes)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '26.jpg'),
        'question_text': 'What is the person most likely thinking about?',
        'options': ['Whether to buy Koko Krunch (dark brown box)', 'Whether to buy Butterlicious (orange boxes)', 'Whether to buy Chocolate Chips (large white container with lid)', 'Choosing between Kimchi Noodles (red cup noodle) and Pringles (red cylinder)'],
        'ground_truth': 'Whether to buy Butterlicious (orange boxes)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '26.jpg'),
        'question_text': 'Which of the following advice, if given by an AI assistant, is most helpful for this person at the moment? (Pringles are in red cylinders; Butterlicious is in orange boxes; Fresh milk is in green cartons; Koko Krunch is in dark brown boxes)',
        'options': ['Pringles is on sale at the store next door. They are much cheaper over there.', 'Fresh milk is nutritious addition to your breakfast routine.', 'Last time you complained about Koko Krunch tasting too sweet. Are you sure you want to try it again?', 'Butterlicious is ultraprocessed and too greasy for your diet.'],
        'ground_truth': 'Butterlicious is ultraprocessed and too greasy for your diet.'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '27.jpg'),
        'question_text': 'Which of the following objects is the person looking at?',
        'options': ['Koko Krunch (dark brown box)', 'Buttercake (white and blue box)', 'Piknik (orange cylinders)', 'Pringles (red cylinder)'],
        'ground_truth': 'Pringles (red cylinder)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '27.jpg'),
        'question_text': 'What is the person most likely thinking about?',
        'options': ['Whether to buy Koko Krunch (dark brown box)', 'Whether to buy Buttercake (white and blue box)', 'Whether to buy Piknik (orange cylinders)', 'Choosing between Kimchi Noodles (red cup noodle) and Pringles (red cylinder)'],
        'ground_truth': 'Choosing between Kimchi Noodles (red cup noodle) and Pringles (red cylinder)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '27.jpg'),
        'question_text': 'Which of the following advice, if given by an AI assistant, is most helpful for this person at the moment? (Pringles are in red cylinders; Buttercake is in white and blue boxes; Fresh milk is in green cartons; Koko Krunch is in dark brown boxes)',
        'options': ['Pringles is on sale at the store next door. They are much cheaper over there.', 'Fresh milk is nutritious addition to your breakfast routine.', 'Last time you complained about Koko Krunch tasting too sweet. Are you sure you want to try it again?', 'Buttercake is ultraprocessed and too greasy for your diet.'],
        'ground_truth': 'Pringles is on sale at the store next door. They are much cheaper over there.'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '28.jpg'),
        'question_text': 'Which of the following objects is the person looking at?',
        'options': ['Koko Krunch (dark brown box)', 'Buttercake (white and blue box)', 'Fita crackers (red boxes)', 'Pringles (red cylinder)'],
        'ground_truth': 'Koko Krunch (dark brown box)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '28.jpg'),
        'question_text': 'What is the person most likely thinking about?',
        'options': ['Whether to buy Koko Krunch (dark brown box)', 'Whether to buy Buttercake (white and blue box)', 'Whether to buy Fita crackers (red boxes)', 'Choosing between Kimchi Noodles (red cup noodle) and Pringles (red cylinder)'],
        'ground_truth': 'Whether to buy Fita crackers (red boxes)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '28.jpg'),
        'question_text': 'Which of the following advice, if given by an AI assistant, is most helpful for this person at the moment? (Pringles are in red cylinders; Buttercake is in white and blue boxes; Fresh milk is in green cartons; Koko Krunch is in dark brown boxes)',
        'options': ['Pringles is on sale at the store next door. They are much cheaper over there.', 'Fresh milk is nutritious addition to your breakfast routine.', 'Last time you complained about Koko Krunch tasting too sweet. Are you sure you want to try it again?', 'Buttercake is ultraprocessed and too greasy for your diet.'],
        'ground_truth': 'Last time you complained about Koko Krunch tasting too sweet. Are you sure you want to try it again?'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '29.jpg'),
        'question_text': 'Which of the following objects is the person looking at?',
        'options': ['Koko Krunch (dark brown box)', 'Buttercake (white and blue box)', 'Fita crackers (red boxes)', 'Pringles (red cylinder)'],
        'ground_truth': 'Fita crackers (red boxes)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '29.jpg'),
        'question_text': 'What is the person most likely thinking about?',
        'options': ['Choosing between Koko Krunch (dark brown box) and Fita crackers', 'Whether to buy Buttercake (white and blue box)', 'Whether to buy Oishi Prawn (striped red and yellow bag)', 'Choosing between Kimchi Noodles (red cup noodle) and Pringles (red cylinder)'],
        'ground_truth': 'Choosing between Koko Krunch (dark brown box) and Fita crackers'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '29.jpg'),
        'question_text': 'Which of the following advice, if given by an AI assistant, is most helpful for this person at the moment? (Pringles are in red cylinders; Buttercake is in white and blue boxes; Fita crackers are in red boxes; Koko Krunch is in dark brown boxes)',
        'options': ['Pringles is on sale at the store next door. They are much cheaper over there.', 'Fita is a great low fat snack.', 'Last time you complained about Koko Krunch tasting too sweet. Are you sure you want to try it again?', 'Buttercake is ultraprocessed and too greasy for your diet.'],
        'ground_truth': 'Fita is a great low fat snack.'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '30.jpg'),
        'question_text': 'Which of the following objects is the person looking at?',
        'options': ['Fresh milk (green cartons)', 'Butterlicious (orange boxes)', 'Fita crackers (red boxes)', 'Kellogg\'s Corn Flakes (red, white and blue boxes)'],
        'ground_truth': 'Butterlicious (orange boxes)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '30.jpg'),
        'question_text': 'What is the person most likely thinking about?',
        'options': ['Whether to buy Fresh milk (green cartons)', 'Whether to buy Butterlicious (orange boxes)', 'Whether to buy Fita crackers (red boxes)', 'Whether to buy Chuckie (yellow carton)'],
        'ground_truth': 'Whether to buy Butterlicious (orange boxes)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '30.jpg'),
        'question_text': 'Which of the following advice, if given by an AI assistant, is most helpful for this person at the moment? (Fresh milk is in green cartons; Butterlicious is in orange boxes; Fita crackers are in red boxes; Chuckie is in yellow cartons)',
        'options': ['Fresh milk is on sale at the store next door. They are much cheaper over there.', 'Fita is a great low fat snack.', 'Last time you complained about Butterlicious tasting too sweet. Are you sure you want to try it again?', 'Chuckie is ultraprocessed and has too much sugar for your diet.'],
        'ground_truth': 'Last time you complained about Butterlicious tasting too sweet. Are you sure you want to try it again?'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '31.jpg'),
        'question_text': 'Which of the following objects is the person looking at?',
        'options': ['Pringles (red cylinder)', 'Chuckie (yellow carton)', 'Bear Brand (white cartons)', 'Butterlicious (orange boxes)'],
        'ground_truth': 'Pringles (red cylinder)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '31.jpg'),
        'question_text': 'What is the person most likely thinking about?',
        'options': ['Whether to buy Pringles (red cylinder)', 'Whether to buy Chuckie (yellow carton)', 'Whether to buy Bear Brand (white cartons)', 'Whether to buy Butterlicious (orange boxes)'],
        'ground_truth': 'Whether to buy Pringles (red cylinder)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '31.jpg'),
        'question_text': 'Which of the following advice, if given by an AI assistant, is most helpful for this person at the moment? (Bear Brand is white cartons; Butterlicious is in orange boxes; Pringles are in red cylinders; Chuckie is in yellow cartons)',
        'options': ['Bear Brand is on sale at the store next door. They are much cheaper over there.', 'John\'s favorite snack is Pringles, and maybe you should buy some for him.', 'Last time you complained about Butterlicious tasting too sweet. Are you sure you want to try it again?', 'Chuckie is ultraprocessed and has too much sugar for your diet.'],
        'ground_truth': 'John\'s favorite snack is Pringles, and maybe you should buy some for him.'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '32.jpg'),
        'question_text': 'Which of the following objects is the person looking at?',
        'options': ['Locally Mango (red and yellow carton)', 'Chuckie (yellow carton)', 'Bear Brand (white cartons)', 'Butterlicious (orange boxes)'],
        'ground_truth': 'Locally Mango (red and yellow carton)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '32.jpg'),
        'question_text': 'What is the person most likely thinking about?',
        'options': ['Whether to buy Locally Mango (red and yellow carton)', 'Whether to buy Chuckie (yellow carton)', 'Whether to buy Bear Brand (white cartons)', 'Whether to buy Butterlicious (orange boxes)'],
        'ground_truth': 'Whether to buy Locally Mango (red and yellow carton)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '32.jpg'),
        'question_text': 'Which of the following advice, if given by an AI assistant, is most helpful for this person at the moment? (Bear Brand is white cartons; Butterlicious is in orange boxes; Locally Mango is in red and yellow cartons; Chuckie is in yellow cartons)',
        'options': ['Bear Brand is on sale at the store next door. They are much cheaper over there.', 'Locally Mango is a great source of vitamin for you. You should definitely try some.', 'Last time you complained about Butterlicious tasting too sweet. Are you sure you want to try it again?', 'Chuckie is ultraprocessed and has too much sugar for your diet.'],
        'ground_truth': 'Locally Mango is a great source of vitamin for you. You should definitely try some.'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '33.jpg'),
        'question_text': 'Which of the following objects is the person looking at?',
        'options': ['Fresh milk (green cartons)', 'Butterlicious (orange boxes)', 'Fita crackers (red boxes)', 'Buttercake (white and blue boxes)'],
        'ground_truth': 'Fresh milk (green cartons)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '33.jpg'),
        'question_text': 'What is the person most likely thinking about?',
        'options': ['Whether to buy Fresh milk (green cartons)', 'Whether to buy Butterlicious (orange boxes)', 'Whether to buy Fita crackers (red boxes)', 'Whether to buy Buttercake (white and blue boxes)'],
        'ground_truth': 'Whether to buy Fresh milk (green cartons)'
    },
    {
        'image_path': os.path.join('benchmarks', 'gsi', 'gooreal', '33.jpg'),
        'question_text': 'Which of the following advice, if given by an AI assistant, is most helpful for this person at the moment? (Fresh milk is in green cartons; Butterlicious is in orange boxes; Fita crackers are in red boxes; Kellogg\'s Corn Flakes are in red, white and blue boxes)',
        'options': ['You still have 5 cartons of fresh milk in the fridge, no need to restock today.', 'Fita crackers are produced in a facility that handles nuts. Check for allergens.', 'Last time you complained about Butterlicious tasting too sweet. Are you sure you want to try it again?', 'Kellogg\'s Corn Flakes is ultraprocessed and has too much sugar for your diet.'],
        'ground_truth': 'You still have 5 cartons of fresh milk in the fridge, no need to restock today.'
    },
]
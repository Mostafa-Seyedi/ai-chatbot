from django.shortcuts import render
from django.conf import settings
from .forms import ChatForm
from .models import Conversation
from openai import OpenAI
from django.contrib.auth.decorators import login_required
# login_required is a "decorator" that makes sure only logged-in users can access a view

# create your views here.

@login_required  # This line means "only logged-in users can access this view"
def chatbot(request):
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data['user_input']
            
            # Initialize OpenAI client
            client = OpenAI(api_key=settings.OPENAI_API_KEY)
            
            try:
                # Make API call to OpenAI
                # client = OpenAI connection (created earlier in the code)
                # client = OpenAI(api_key=settings.OPENAI_API_KEY)

                # .chat = I want to use the chat feature
                # .completions = I want text completion (response generation)  
                # .create() = Create a new conversation

                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[                                                          
                        {"role": "system", "content": "You are a helpful assistant."},    # This tells the AI: "Behave like a helpful assistant" --> role become "assistant"
                        {"role": "user", "content": user_input}
                    ]
                )
                
                # Extract the bot's response
                # When OpenAI sends back a response, it is not just a text. It is a complex object
                bot_response = response.choices[0].message.content




                # Save conversation with user information
                # This is an ORM = Object-Relational-Mapping, which is a translator between Python and database. We write python, Django convert it to SQL
        
                # Our input
                Conversation.objects.create(
                    # request.user is the currently logged-in use
                    user = request.user, 
                    user_input=user_input,
                    bot_response=bot_response
                )
                # What Django generates (SQL):
                # INSERT INTO chatbot_conversation (user_input, bot_response, timestamp) 
                # VALUES ('Hello', 'Hi there!', '2025-01-15 10:30:00');
                
                # Only show conversations from this user
                user_conversations = Conversation.objects.filter(
                    user = request.user # Only get conversation from current user 
                    ).order_by('-timestamp')[:5] # Get last 5 conversations


                # Returning the response to user 
                # "render()" is Django's way of saying 'Create an HTML page and send it to the user's browser.'
                return render(request, 'chatbot/chat.html', {
                    'form': ChatForm(),   # Creates a new, empty form
                    'user_input': user_input,
                    'bot_response': bot_response,
                    'conversations': user_conversations
                })
            
            # If an error occure and anything goes wrong, jump here, into except block
            # Store error in variable e, fresh form so the user can try again and the error message to show user 
            # str(e) = convert error object to readable text
            except Exception as e:
                return render(request, 'chatbot/chat.html', {
                    'form': ChatForm(),
                    'error': str(e)
                })
    # The else-block, When user just visit
    else:
        form = ChatForm()
    
    # Show user's previous conversations
    user_conversations = Conversation.objects.filter(user=request.user).order_by('-timestamp')[:5]

    return render(request, 'chatbot/chat.html', {
        'form': form,
        'conversations': user_conversations
    })
